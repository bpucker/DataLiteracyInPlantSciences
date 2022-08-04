### Boas Pucker ###
### b.pucker@tu-braunschweig.de ###


__version__ = "v0.1"

__usage__ = """
					python3 statistic_test.py
					--input <DATA_FILE>
					
					optional:
					--test <TEST_SELECTION>[u]
					--paired (activates paired test)
					"""

import os, re, sys, math
from operator import itemgetter
from scipy import stats

# --- end of imports --- #

def load_datasets( input_file ):
	"""! @brief load data sets from given input file """
	
	data = { "A": [], "B": [] }
	with open( input_file, "r" ) as f:
		header = f.readline()
		line = f.readline()
		while line:
			parts = line.strip().split('\t')
			if len( parts ) == 2:
				data["A"].append( float( parts[0] ) )
				data["B"].append( float( parts[1] ) )
			elif len( parts ) == 1:
				data["A"].append( float( parts[0] ) )
			else:
				print ( "ERROR: " + str( parts ) )
			line = f.readline()
	return data


def main( arguments ):
	"""! @brief run everything """
	
	if '--input' in arguments:
		input_file = arguments[ arguments.index('--input')+1 ]
	else:
		input_file = arguments[ arguments.index('--in')+1 ]
	
	if '--test' in arguments:
		test = arguments[ arguments.index('--test')+1 ]
		if test not in "utwxsp":	#u= U-test, t = t-test, w = W-test, x = Chi-Square-test, s = Spearman, p = Pearson, 
			test = "u"
	else:
		test = "u"

	data = load_datasets( input_file )
	
	if '--paired' in arguments:
		paired = True
		if len( data["A"] ) != len( data["B"] ):
			sys.exit( "ERROR: Paired samples have different numbers of observations" )
	else:
		paired = False
	
	
	# --- test for normal distribution --- #
	stat_A, p_A = stats.shapiro( data["A"] )
	if p_A > 0.05:
		print( "First sample probably Gaussian" )
	else:
		print( "First sample probably not Gaussian" )
	stat_B, p_B = stats.shapiro( data["B"] )
	if p_B > 0.05:
		print( "Second sample probably Gaussian" )
	else:
		print( "Second sample probably not Gaussian" )
	
	
	if test == "t":
		if paired:	# --- paired t-test --- #
			stat, p = stats.ttest_rel( data["A"], data["B"] )
			print( "Test statistic: " + str( round( stat, 4 ) ) + "; p-value: " + str( round( p, 4 ) ) )
		else:	# --- unpaired t-test --- #
			stat, p = stats.ttest_ind( data["A"], data["B"] )
			print( "Test statistic: " + str( round( stat, 4 ) ) + "; p-value: " + str( round( p, 4 ) ) )
	
	if test == "u":	# --- U-test --- #
		stat, p = stats.mannwhitneyu( data["A"], data["B"] )
		print( "Test statistic: " + str( round( stat, 4 ) ) + "; p-value: " + str( round( p, 4 ) ) )
	
	if test == "w":	# --- W-test --- #
		stat, p = stats.wilcoxon( data["A"], data["B"] )
		print( "Test statistic: " + str( round( stat, 4 ) ) + "; p-value: " + str( round( p, 4 ) ) )
	
	if test == "x":	# --- x-test --- #
		stat, p = stats.chi2_contigency( data["A"], data["B"] )
		print( "Test statistic: " + str( round( stat, 4 ) ) + "; p-value: " + str( round( p, 4 ) ) )
	
	if test == "s":	# --- s-test (Spearman) --- #
		stat, p = stats.spearmanr( data["A"], data["B"] )
		print( "Test statistic: " + str( round( stat, 4 ) ) + "; p-value: " + str( round( p, 4 ) ) )
	
	if test == "p":	# --- p-test (Pearson) --- #
		stat, p = stats.pearsonr( data["A"], data["B"] )
		print( "Test statistic: " + str( round( stat, 4 ) ) + "; p-value: " + str( round( p, 4 ) ) )


if '--input' in sys.argv:
	main( sys.argv )
elif '--in' in sys.argv:
	main( sys.argv )
else:
	sys.exit( __usage__ )
