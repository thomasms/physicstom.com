---
title: The epic software controlling an accelerator near you
date: "2021-10-07T14:54:44.562827"
readtime: 4 mins
tags: ['software', 'physics']
---

If you have ever built a particle accelerator before chances are you will know what EPICS is. If, however, like most people, you have not built a particle accelerator you will likely not know what EPICS is.
I am going assume you fall into the latter category, but even if you have built an accelerator before and/or know what EPICS is, these notes might be helpful anyway.

In short, if you want to build an accelerator, tokamak fusion device, or just even brew beer, you will need to control and monitor that system and doing so is not so trivial and requires some complex software. Enter EPICS.

[EPICS](https://epics-controls.org) (Experimental Physics and Industrial Control System) is a toolkit designed for distributed control systems. It provides a set of tools and components for creating a control system. **It is not an out-of-the-box solution** however.
It is a network based client-server model making use of TCP and UDP.

A quick bit of history.
EPICS was originally developed by Los Alamos and Oak Ridge national labs in the late 1980s. 
Back then it was discovered that many different laboratories and industrial control systems were being built independently but all sharing very common functionality. 
Many of existing solutions only supported their line of I/O and were not very extendable, nor were they open source. 
Around the time there were many debates on how to handle certain aspects - VMS vs Unix, I/O protocols, etc. 
If an open source, common set of tools were provided then this could save people a large amount of effort when writing a control system - EPICS was born.


After many years of trying to get EPICS open source, it is now open source, and has been for some years.
The license is very liberal and has a helpful and fairly big community (900+ subscribers). 
It has a strong history in use at major experiments globally and has a big international community and collaboration as a result. 
EPICS is now over 30 years old and still continues to be developed & released at the time of writing, with no intent to stop in the future.

It is multi-platform, supporting Linux, Windows, Mac.


## Well that's nice, so who uses it?

As I said before it is typically used in accelerators, but it is also used to control fusion reactors such as ITER and JET.
Besides this, it is also used in telescopes and it has even been used to [brew beer](https://epics.anl.gov/tech-talk/2014/msg01137.php).

To name a few places, big EPICS players are:

- ANL, US
- LANL, US
- ORNL, US
- SLAC, US
- PSI, Switzerland
- KEK, Japan
- DESY, German
- ITER, France
- Diamond Light Source, UK
- European Spallation Source (ESS), Sweden
- Australian Synchrotron, Australia


## OK, but what exactly is EPICS?

As mentioned previously, EPICS uses a client-server architecture, where clients are programs that require access to Process Variables (PVs - more on that later) to carry out their purpose.
The service that a server provides is access to a Process Variable.
Here we define a **Process Variable as a named piece of data** (integer, float, array, structure...) associated with a machine i.e. parameter, setpoint, readback, status, and it can be thought of as the basic data element of the architecture.

**PVs are the currency of EPICS.**

A few examples of PVs are shown in the table below.
|                      Name | Value          |
| ------------------------: | -------------- |
|            S1:VAC:reading | 5.63e-0.7 torr |
|     S3:DIPOLE:PS:setPoint | 98.42 amps     |
| BOOSTER:gateValuePosition | 'OPEN'         |
|      LINAC:BPM4:xPosition | -0.321 mm      |
|                  APS:Mode | 'Stored Beam'  |


Besides their value, whether it be a integer, float, string, double, array, ... a process variable also contains a set of attributes such as:

- Alarm Severity (e.g. NO_ALARM, MINOR, MAJOR, INVALID)
- Alarm Status (e.g. LOW, HI, LOLO, HIHI, READ_error)
- Alarm thresholds
- Timestamp
- Control limits
- Operating range
- Units (e.g. mm, Amps, degrees)

The entire set of PVs therefore establish a distributed database of information, control parameters, and machine status.

Two protocols are supported in EPICS - which are bespoke to EPICS - Channel Access (CA) is the original protocol introduced since the inception of EPICS, and since version 4 another protocol was introduced - PVAccess (PVA) - which is generally prefered due to performance and generic data structures.
For new projects certainly it is recommended to use PVA over CA, but there is a hot debate in the community on this, so let's not go into it here.
However, version 7 supports both protocols, this is the current major version. These protocols define how PV data is transferred between server and client and vice versa.

Any tool/program/application that abides by the CA or PVA protocols can be described as "EPICS compliant". Traditionally EPICS is a toolkit, providing small tools to use these protocols to "use EPICS", however, with recent versions some parts can be considered a library or set of APIs to build custom tools as well.


## Tell me more...

EPICS consists of a few major components:
- **IOC** - Input/Output Controller. The core of EPICS. Any platform that can support EPICS run time databases together with the other software components described in the manual. They are essentially servers, but can also be clients of other IOCs. One example is a workstation. Another example is a VME/VXI based system using vxWorks or RTEMS as the realtime operating system.
- **OPI** - Operator Interface. This is a workstation which can run various EPICS tools and is typically a client. This is normally a GUI.
- **LAN** - Local Area Network. This is the communication network which allows the IOCs and OPIs to communicate.


### IOC
The Input/Output Controller is a fundamental concept to EPICS and at the heart of each IOC is a memory resident **database** together with various memory resident structures describing the contents of the database.
EPICS supports a large and extensible set of record types, e.g. ai (Analog Input), ao (Analog Output), etc. An IOC will contain (besides the database) device support (modify DB and access hardware) and driver support. It is essentially a software process serving PVs, amongst other things (device support). It also provides a shell to interact with at run time (iocsh) - useful for debugging when operational.

In the database each record type (more on records later) has a fixed set of fields. Some fields are common to all record types and others are specific to particular record types.
Every record has a record name and every field has a field name. 
The first field of every database record holds the record name, which must be unique across all IOCs that are attached to the same TCP/IP subnet.

Record types that are not associated with hardware do not have device support or device drivers. We typically refer to these particular IOCs as "soft" or "softIOC". 
It just so happens that EPICS comes with a tool named "softIoc" which is a command line tool that can take a database as an argument (```-d``` argument) and at runtime setup an IOC based on software only (no devices or hardware). This is commonly used in examples.


#### What is a record?
A record is the basic unit of action in a database. A record contains fields and field values modify the action.

Record + field = Process Variable

- Records **do**
- Fields **store**

An example of a simple record is shown below.
```bash
record(ai, "mydummyrecord:v1"){
    field(DESC, "A description of my record")
    field(DTYP, "mydevicetype")
    # a comment!
    field(INP, "#C1 S7 @v")
}
```
In the above example the record type is `ai` (analogue in), `"mydummyrecord:v1"` is the record name, `field` is a field containing two parts: the name and the value (always use quote for value but for numerical values this can sometimes be omitted, but not recommended). For example, `DESC` is the field name which is actually a field name common to all records and the field value is then `"A description of my record"`. 

Note that whitespace is not important, nor do the curly braces need to be on the same line. You could actually write it all on the same line if you wanted, but for readibility it is good practice not to.

An important note regarding records, is that many people will use the term "Record scanning" where this actually has nothing to do with the `SCAN` field in a record but actually means to process, or execute, a record.


#### You said a database? Do I need to know SQL?
The process database is an object database with an integrated client (device support). It is not a traditional Relational Database (RDB) and no you don't need to use SQL here.
It is an in memory database defined in human readable text files (the collection of records as shown above).

If you want to think in terms of a RDB then we can loosely make the following mappings:
- EPICS record type &#8594; RDB table
- EPICS record &#8594; RDB row
- EPICS field &#8594; RDB column (field)
- EPICS link &#8594; RDB foriegn key

These are not direct mappings but can help when trying to understand the EPICS database terminolgy coming from an RDB background.
With respect to the last one - the foriegn key - is not quite the same but similar.


## Notes on PVA
**What is PVAccess (PVA)?**
The PVAccess network protocol is a hybrid supporting request/response, and publish/subscribe operations.

PVA is closely related to the Channel Access (CA) protocol (v3 EPICS), which may work alongside, and is intended to supersede (for new projects it is recommended to use PVA). Fundamentally PVA is similar to CA (name search with UDP + data transfer with TCP), but supports arbitrary data structures instead of DBR_* types. Also allows RPC operations!

Four protocol operations are supported by PVXS.

- **Get** - Fetch the present value of a PV.
- **Put** - Change the value of a PV.
- **Monitor** - Subscribe to changes in the value of a PV.
- **RPC** - A remote method call.

Get, Put, Monitor, and RPC are to the PVA protocol what GET, PUT, POST are to the HTTP protocol.


## OK, remind me again what a PV is?
As mentioned before, in the EPICS world a Process Variable (PV) refers to the idea of a globally addressed data structure.
An EPICS control system is composed of many PVs (in the millions for large facilities).
The present value of a PV is modified by a combination of remote operations via CA and/or PVA, and via local processing (eg. values read from local hardware).

A common example of a PV is a measurement value, for example a temperature measured by a particular sensor.
Another example would be an electromechanical relay, which may be opened or closed.
In this case a **Get** operation would poll the current open/closed state of the relay.
A **Monitor** operation (subscription) would receive notification when the relay state changes.
A **Put** operation would be used to command the relay to open or close, or perhaps toggle (the precise meaning of a Put is context dependent).

So the Get, Put, and Monitor operations on a given PV are conventionally operating on a common data structure.
The RPC operation is more arbitrary, and we need not have any relationship with a common data structure (eg. the open/closed state of the relay.)
RPC is generally not that common in EPICS and is a new addition since V4, but it opens the possibility to do more interesting things within EPICS.

**NOTE: In the context of the PVA or CA protocols, a "PV name" is an address string which uniquely identifies a Process Variable. All CA and PVA network operations begin with a “PV name” string.**

A "PV name" string is to the PVA and CA protocols what a URL is to the HTTP protocol.
The main difference being that while a URL is hierarchical, having a hostname and path string, a PV name is not. 
The namespace of PV names is by default all local IP subnets (broadcast domains). This can be made more complicated though the specifics of client-server network configuration.


## TCP & UDP
As mentioned previously, EPICS uses UDP & TCP to communicate over the distributed network. 
The Internet Protocol (IP) basically consists of UDP and TCP. 
Ports 5064 (CA port) & 5065 (CA beacon port) are apparently used for EPICS UDP sockets. 
For TCP sockets an arbitrary port is used, with the exact port number included in PV name search replies. 
Therefore a CA server will maintain at least two sockets - a UDP socket bound to the CA port (5064) listening for PV name search request broadcasts & another UDP socket, which periodically send beacons to the CA Beacon port (5065). 
PV name search replies are sent as unicast messages to the source of the broadcast. 

For PVA, the ports are 5075 and 5076 for server and beacons respectively.

**User Datagram Protocol (UDP)**
Sends a network packet from one port on one computer to one or more ports on one or more other computers...with one or more listeners on the target port.

- Fast!
- Checksum: If the packet arrives, it's OK.
- Not reliable: Packets get lost, arrive out-of-order, arrive more than once.

**Transmission Control Protocol (TCP)**
Sends a stream of bytes from one port on one computer to another port on
another computer, with exactly one listener on the target port.

- Reliable: Bytes arrive at the receiver in the correct order.
- Basically adds serial numbers to UDP packets, requesting repeats for missing packages.
- Slower, and message boundaries get lost:
  - "Hello Fred!" might arrive as "Hel" <pause> "lo F" <pause> "red!"


A TCP connection between an EPICS client and server is referred to as a Virtual Circuit.

Typically only one Circuit is opened between each client and server, however, a client may open more than one Circuit to the same server.


### Search request
The main mechanism for EPICS to find a PV given only its name is via a search request - essentially a broadcast to the whole subnet.

A series of UDP packets are sent out to the network (local subnet) or to a select list of IP addresses (```EPICS_CA_ADDR_LIST```).
According to some presentations on Channel Access this starts with a small interval (~30 ms) and doubles each time, until reaching 5 second intervals and stops after 100 packets (~8 minutes) or when it gets a response.
The mechanism is similar when using PVA but depending on the implementation of the protocol times can vary to the CA equivalent.

One important consequence of this is that non-existant PVs cause high traffic on the network and should therefore be avoided at all costs!


EPICS provides a set of environment variables to allow users to configure the search requests, with the most common being ```EPICS_CA_ADDR_LIST```, which is the list of IP addresses to search on. 
For multiple addresses these should be separated by whitespace i.e. 

```bash
export EPICS_CA_ADDR_LIST="123.45.1.255 123.45.2.14 123.45.2.108"
```

But generally these variables should not be changed from their defaults unless you know what you're doing....

## Anything else I should know about EPICS?
Yes, there is much more to learn about it and typically an EPICS training course can take a full week just to learn the basics.

Here are some nice links and references if you want to know more.

- [Introduction to EPICS](https://epics.nsls2.bnl.gov/training/ri-201011/Intro.pdf)
- [EPICS Process Database](https://epics.nsls2.bnl.gov/training/ri-201011/database-201011.pdf)
- [Running IOCs on Linux](https://epics.nsls2.bnl.gov/training/ri-201011/softiocs.pdf)
- [Channel Access Protocol Specification](https://epics.anl.gov/base/R3-16/0-docs/CAproto/index.html)
- [PVA Protocol Specification](http://epics-pvdata.sourceforge.net/pvAccess_Protocol_Specification.html)
- [Developer guide](https://epics.anl.gov/base/R3-15/5-docs/AppDevGuide/AppDevGuide.html)
- [EPICS Record Reference Manual](https://controlssoftware.sns.ornl.gov/training/2019_USPAS/Presentations/02a%20Recordref_3_13.pdf)
- [EPICS 7 is the latest version in the EPICS ecosystem](https://medium.com/control-sheet/epics-7-5d35df7355e4)


Training links:
- [USPAS (2019)](https://controlssoftware.sns.ornl.gov/training/2019_USPAS) - slides & examples with VM
- [NSLS-II EPICS Lecture series (2018)](https://www.bnl.gov/ps/epics/) -  links to YouTube video lectures, slides & examples
- [APS Lecture series (2015)](https://epics.anl.gov/docs/APS2015.php) - YouTube video lectures
- [APS Lecture series (2014)](https://epics.anl.gov/docs/APS2014.php) - YouTube video lectures


Now, get building that accelerator!
