## Build steps
0. Apply patch
1. Build L4Re
2. Build package by invoking in this directory: `make O=../path/to/l4re/snapshot/obj/l4/arm-v7/`
3. `make` again inside snapshot directory.

## Sample output
```
U-Boot> fatload mmc 0 0x0c000000 bootstrap_ank_server_client_rpi4.elf
2187024 bytes read in 138 ms (15.1 MiB/s)
U-Boot> bootelf 0x0c000000
## Starting application at 0x01000000 ...

L4 Bootstrapper
  Build: #23 Tue Apr  4 23:04:53 BST 2023, 10.2.1 20210110
  Limiting 'RAM' region   [ 40200000,  fbffffff] { bbe00000} to   [ 40200000,  bcffffff] { 7ce00000} due to 3024 MB address limit
  Raspberry Pi Model 4B, Rev 1.1, 4096MB, SoC BCM2711 [c03111]
  Warranty intact, OTP reading allowed, OTP programming allowed, Overvoltage allowed
  RAM: 0000000000000000 - 000000003b3fffff: 970752kB
  RAM: 0000000040200000 - 00000000bcffffff: 2045952kB
  Total RAM: 2946MB
  Scanning fiasco
  Scanning sigma0
  Scanning moe
  Moving up to 8 modules behind 1100000
  moving module 07 { 1174000-1194717 } -> { 125f000-127f717 } [132888]
  moving module 06 { 1151000-1173723 } -> { 123c000-125e723 } [141092]
  moving module 05 { 1150000-11502b3 } -> { 123b000-123b2b3 } [692]
  moving module 04 { 10e6000-114f74f } -> { 11d1000-123a74f } [431952]
  moving module 03 { 10d0000-10e54f7 } -> { 11bb000-11d04f7 } [87288]
  moving module 02 { 10a7000-10cf523 } -> { 1192000-11ba523 } [165156]
  moving module 01 { 10a0000-10a63b7 } -> { 118b000-11913b7 } [25528]
  moving module 00 { 1015000-109f4c7 } -> { 1100000-118a4c7 } [566472]
  Loading fiasco
  find kernel info page...
  found kernel info page (via ELF) at 2000
  Loading sigma0
  Loading moe
Regions of list 'regions'
    [        0,       fff] {     1000} Arch   mpspin
    [     1000,     95fff] {    95000} Kern   fiasco
    [    96000,     96fff] {     1000} Root   mbi_rt
    [   100000,    10b22f] {     b230} Sigma0 sigma0
    [   140000,    167acb] {    27acc} Root   moe
    [   168f7c,    174577] {     b5fc} Root   moe
    [  1000000,   10135df] {    135e0} Boot   bootstrap
    [  10000d0,   1000143] {       74} Root   cpu_boot
    [  1014198,   10147a3] {      60c} Boot   modinfo
    [  11bb000,   127f717] {    c4718} Root   Module
  found kernel options (via ELF) at 3000
  Sigma0 config    ip:001003c0 sp:00000000
  Roottask config  ip:00141a68 sp:00000000
  Starting kernel fiasco at 00001254
Hello from Startup::stage2
Number of IRQs available at this GIC: 256
FPU: Initialize
FPU0: Subarch: 3, Part: 40, Rev: 0, Var: 8, Impl: 41
ARM generic timer: freq=54000000 interval=54000 cnt=2169860417
SERIAL ESC: allocated IRQ 125 for serial uart
Not using serial hack in slow timer handler.
Welcome to L4/Fiasco.OC!
L4/Fiasco.OC microkernel on arm
Rev: unknown compiled with gcc 10.2.1 20210110 for RPi4 (Broadcom 2711)    []
Build: #1 Tue Apr  4 22:02:42 BST 2023

Allocate ARM PPI 27 to virtual 1
FPU1: Subarch: 3, Part: 40, Rev: 0, Var: 8, Impl: 41
Allocate ARM PPI 27 to virtual 1
FPU2: Subarch: 3, Part: 40, Rev: 0, Var: 8, Impl: 41
Cache config: ON
FPU3: Subarch: 3, Part: 40, Rev: 0, Var: 8, Impl: 41
Allocate ARM PPI 27 to virtual 1
ID_PCFaRl[brat  g timer loop... Cach0e0 000nfig: 131ON
0A0l0locate ARM PPI 1217011 dtoon evirtual
1
ID_PFR[01]:   ID0_0[0DA]FR0: 13103 010066 0001100010100000MCDaBc:huseonage size:
ON30

 ID_[DA]FR0: 0MDB: use page size: 320110066
 00IM0DD0BMFR[e page size: 01210201105

40I0D0_0P0R[01]:   0000013011 260000 000110011210221S1
  ID_[DA]FR0: G03M010066 A000000000:
 Hello!
ID_MMFR[04]: 10201105 40000000 01260000 02102211
ID _MMFR[04]:  10201105 KI40000000 P 01@260000  0221002211
00
  allocated 4KB for maintenance structures
SIGMA0: Dump of all resource maps
RAM:------------------------
[4:RWX:96000;96fff]
[0:RWX:97000;fffff]
[0:RWX:10c000;13ffff]
[4:R-X:140000;167fff]
[4:RW-:168000;174fff]
[0:RWX:175000;ffffff]
[4:---:1000000;1000fff]
[0:RWX:1001000;11bafff]
[4:RWX:11bb000;127ffff]
[0:RWX:1280000;3b3fffff]
[0:RWX:40200000;bbffffff]
IOMEM:----------------------
[0:RW-:0;fff]
[0:RW-:3b400000;401fffff]
[0:RW-:bd000000;ffffffff]
MOE: Hello world
MOE: found 2998672 KByte free memory
MOE: found RAM from 96000 to bc000000
MOE: allocated 3007 KByte for the page array @0x175000
MOE: virtual user address space [0-ffffffff]
MOE: rom name space cap -> [C:103000]
MOE: rwfs name space cap -> [C:105000]
  BOOTFS: [11bb000-11d04f8] [C:107000] l4re
  BOOTFS: [11d1000-123a750] [C:109000] ned
  BOOTFS: [123b000-123b2b4] [C:10b000] client_server.cfg
  BOOTFS: [123c000-125e724] [C:10d000] ank_server
  BOOTFS: [125f000-127f718] [C:10f000] ank_client
MOE: cmdline: moe rom/client_server.cfg
MOE: Starting: rom/ned rom/client_server.cfg
MOE: loading 'rom/ned'
Ned says: Hi World!
Ned: loading file: 'rom/client_server.cfg'
client  | Welcome to client
server  | Welcome to the 'mtadd_server' multi-threaded server
client  | Asking for 4 + 8
server  | Thread adding: 4 + 8
server  | Received: 12
client  | Result: 12

```
