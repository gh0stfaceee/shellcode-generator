# shellcode-generator
generate shellcode to get a reverse shell

made by ghostfaceee


utilisez le convertisseur pour que le SC tienne en une ligne
```sh
cat hex.txt |sed '1 s/../& /g' |sed '1 s/ /\\x/g' |awk '{print "\\x"$0}'  |sed 's/\\x$//'
```

le script python remplace juste `\x11\x5c` avec `port_htons[4:]` et `port_htons[2:4]` et les octets correspondant à l'ip
