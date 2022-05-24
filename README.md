# shellcode-generator
generate shellcode to get a reverse shell

made by ghostfaceee


utilisez le convertisseur pour que le SC tienne en une ligne
```sh
cat hex.txt |sed '1 s/../& /g' |sed '1 s/ /\\x/g' |awk '{print "\\x"$0}'  |sed 's/\\x$//'
```
