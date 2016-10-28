# regex_tester

From command line test regex in either Bash, Python2 or Python3

In file "regex" write your regex like this:
```
^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)((\.(0|[1-9][0-9]*))?(\-[0-9A-Za-z-]+(\.[0-9A-Za-z-]+)*)?(\+[0-9A-Za-z-]+(\.[0-9A-Za-z-]+)*)?)?$
```

In file "patterns" write strings you want to test, one per line:
```
2.0.0
2.0.0-rc.2
2.0.0-rc.1
1.0.0
1.0.0-beta
5.rc55
```

Then call script:
```
$ ./bash_r_t 
Testing the following bash regex
================================

^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)((\.(0|[1-9][0-9]*))?(\-[0-9A-Za-z-]+(\.[0-9A-Za-z-]+)*)?(\+[0-9A-Za-z-]+(\.[0-9A-Za-z-]+)*)?)?$

================================
2.0.0                      MATCHED    
2.0.0-rc.2                 MATCHED    
2.0.0-rc.1                 MATCHED    
1.0.0                      MATCHED    
1.0.0-beta                 MATCHED    
5.rc55                     NOT MATCHED 
```
or
```
$ ./python2_r_t
...
$ ./python3_r_t
```
