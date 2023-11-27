# reconkul
---
This script was created with the goal of providing a Draconmap that, like Zenmap, is both beginner-friendly and expert-friendly. Active research and development day and night
---
### Table of contents
- How to use
    - [specification](#specification)
        - [Usage](#Usage)
        - [explanation](#explanation)

# specification
![](https://raw.githubusercontent.com/SakuraSystemz/reconkul/master/IMG/reconkul-img1.png)
reconkul is an automation program that run port scanning using Nmap as core engine, it in a menu style similar to Draconmap. We currently support vulnerability scanning using Nmap scripts.

### Usage
The operation method is very simple, so will explain it with an image. but, will explain in detail about the timing template.

![](https://raw.githubusercontent.com/SakuraSystemz/reconkul/master/IMG/reconkul-img2.png)

As you can see, after selecting the menu number, after setting the hostname or IP address, set any number from 0 to 5.

##### What timing template
timing template are one of Nmap's features that control the number of packets represented by the option "-T". The default is -T3.

```
nmap -vvv -T3 ...
```
Basically, the higher this number, the faster the scan, but at the expense of accuracy. This is because the number of packets is large. A high number of packets is more likely to be detected by the target's defense system, making it less likely to yield satisfactory results. Currently, Quick Scan makes -T optional and operates with -F option. Template recommends level 4


### explanation
Currently reconkul has 5 scan options.
```
1. Quick Scan
2. Full Scan
3. Port Scan
4. SYN Scan(need root)
5. Vuln Scan
```
explain these in turn.

#### Quick Scan
This is exactly the same as "nmap -vvv -Pn -T4 -F hosts" (if you choose -T4)....

# Coming Soon
