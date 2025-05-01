2) Команда которая печатает Hello, DevOps! и записывает в файл hello.txt
```
echo 'Hello, DevOps!' | tee ~/hello.txt
```
3) 
```
cat /var/log/syslog | grep -i error | head -n 5
```