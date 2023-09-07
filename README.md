# Fat-Tree Data Center Topology using Mininet

This project aims to emulate a Data Center Networ (DCN), using Fat tree topology proposed by M.Al-Fares, which is derived from Clos switching network; a multistage switching architecture that reduces the number of ports required in an interconnected fabric.

For emulation purposes, I have used Mininet; a network emulator able to create virtual hosts, swictes, controllers, and links. Mininet supports Software Defined Networking (SDN) and OpenFlow for custom routing.

## Fat Tree Topology

The Fat tree topology is based on leveraging commodity Ethernet switches for interconnecting cluster nodes to achieve full bisection bandwidth or oversubscription ratio of 1:1. This means that all hosts may potentially communicate with other hosts at full bandwidth of their network interface. The distinctive feature of this topology as pointed out by M. Al Fares is its cost-effectiveness. It is able to deliver scalable bandwidth at moderate cost as opposed to other existing techiniques.

I have implemented a three-tier fat tree for my project. This type of topology has three layers i.e., core, aggregation, and edge. Switches (used to define devices that perform layer-2 swicthing) eixsting at all three levels of the architecture. For the purpose of this project, all switches have been assumed to be identical with equal number of ports. 
The following diagram depicts a three-tier fat tree topology:

![Fat Tree Topology](https://user-images.githubusercontent.com/97694796/227652316-6e26a75a-674a-4492-b6b2-d2139e31cf59.png)

## Mininet

Mininet is a network emulator which creates a network of virtual hosts, switches, controllers and links. Mininet hosts run standard Linux network software and supports OpenFlow and Software Defined Networking (SDN) for flexible custom routing. However, there are a few limitations. Mininet-based networks cannot exceed the available bandwidth of a single server and cannot run non-Linux compatible applications.

## Software Defined Networking (SDN)

SDN is an approach to network architecture which allows the network to be centrally and logically controlled using using software applications. There are four core characteristics of this approach:
- Generalized flow based forwarding as opposed to the conventional destination based addressing (e.g. Openflow)
- Control and data plane seperation, with a remote controller interacting with local control agents to compute and distribute forwarding tables (centralized programming)
-  Control plane functions are transparent/external to the data plane switches (easier network management)
-  Programmable control applications allowing for open and flexible implementation.

### OpenFlow

The OpenFlow protocol is the standard communications protocol that defines the communication between the SDN controller and network agents i.e., data plane switches, routers etc. Through this interface, the SDN controller queries switch features, configures switch parameters, add, delete, modify flow entries in the flow-table.

## Topology

In order to construct such a topology, we must first know certain information. Each switch is identical for the purpose of this project with k number of ports. Thus, such a fat tree is also called k-port fat tree network topology. From the value of k, we can derive the number of core, aggregation, edge switches, and the maximum number of hosts that can be attached.

I have chosen k=4, i.e., each switch has exactly 4 ports. 
- Pods = 4
- Core switches = 4
- Aggregate switches per pod = 2, Total = 8
- Edge switches per pod = 2, Total = 8
- Hosts per pod = 4, Total = 16

![image](https://user-images.githubusercontent.com/97694796/227654311-286c3463-ef65-497e-9cb7-b07d786dce5b.png)

### Ryu Controller

I have used a remote/external controller i.e., Ryu controller. This is due to the fact that Mininet’s default controller supports upto 16 individual switches. Our simulation for k=4 has 20 switches in total.

The Ryu controller, implemented in Python is an open source project maintained by open Ryu community on Github. It is compatible with SDN and is designed to increase the agility of the network. The controller runs in the background (manually started and shut down) and is connected to the custom topology on mininet. This is achieved by invoking the RemoteController class, which acts as a proxy for the controller.

## Simulation Process

Follow the given steps to run the application:
- Start the controller in the background
- Implement simple_switch_stp_13.py
- Start the mininet fat tree topology
- Display all nodes and links
- Ping each host for connection establishment

## Results & Analysis

I have employed the use of Iperf, which is a tool used for active measurement of maximum achieveable bandwidth in IP networks. It supports various parameters and protocols. For each test it reports bandwidth, loss and other parameters. I have conducted two type of tests: TCP and UDP based tests.
Following parameters have been measured:
- Throughput
- Rounded Trip Time (RTT)
- Jitter
- Bisection Bandwidth

## Conclusion

The table below depicts the results that have been achieved.

![image](https://user-images.githubusercontent.com/97694796/227655310-fc8522a5-119a-4f84-863c-26fd7ecdbc25.png)

The throughput achieved is satisfactory. However, due to significant latency and jitter, it has been affected considerably. One way of addressing this and ensuring full bandwidth communication between arbitrary hosts, as described by in the paper ‘A Scalable, Commodity Data Center Network Architecture’ – is to employ multi-path routing techniques such as ECMP. 

I have modelled my topology to have fixed link bandwidth, this can cause the overall bandwidth to be limited by the bandwidth available at the root of the tree heirarchy. Single routing paths between source and destination can quickly lead to bottlenecks up and down the fat tree, limiting the overalll performance.

Often switches concentrate traffic to another subnet through a specific port even though other choices may exist with the same cost. This can cause congestion, especially if a small subclass of core switches are chosen as intermediary links between pods. Once again, a need for more fine-tuned traffic diffusion methodology is required which takes advantage of the fat tree structure.
