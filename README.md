# Mininet-Fat-Tree-Topology
This project aims to simulate a Data Center Network (DCN), using Fat tree topology proposed by M.Al-Fares, which is derived from Clos switching network; a multistage switching architecture that reduces the number of ports required in an interconnected fabric.
For simulation purposes, I will be using Mininet; a network emulator able to create virtual hosts, swictes, controllers, and links. Mininet supports Software Defined Networking (SDN) and OpenFlow for custom routing.

The project has been implemented for a custom value of the parameter 'k', i.e., number of ports of each switch. Due to computational restraints, I have implemented it for k=4.

For the purpose of this project, I have used a remote/external controller i.e., Ryu controller. This is due to the fact that Mininet’s default controller supports upto 16 individual switches. Our simulation for k=4 has 20 switches in total.  

