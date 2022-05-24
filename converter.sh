echo "Converting Hex..."

cat hex.txt |sed '1 s/../& /g' |sed '1 s/ /\\x/g' |awk '{print "\\x"$0}'  |sed 's/\\x$//'
