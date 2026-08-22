# Multi-AGV Task Scheduling and Dynamic Map Path Planning Based on Task Pre-Allocation
**Source**: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0352782
**Date**: 2026-07-24
**Author**: Gao J, Xie W, Liu H, Zhou J, Wang L, Liang J — Shandong University of Science and Technology
**Keywords**: AGV, dynamic map, path planning, task scheduling, Floyd algorithm, warehouse logistics, multi-AGV systems, path congestion, no-load rate

## Elevator pitch
A PLOS ONE research paper proposes an integrated optimization approach for multi-AGV systems that combines task pre-allocation scheduling with a dynamic map path planning mechanism using a localized Floyd update algorithm to reduce no-load rates and mitigate path congestion in warehouse environments.

## Takeaways
- The paper introduces a task segmentation strategy that decomposes complex tasks into long-distance transport and precision in-racking sub-tasks assigned to heterogeneous AGV types
- A task pre-allocation algorithm enables AGVs to receive new assignments before completing current tasks, reducing the system no-load rate
- A dynamic map path planning mechanism incorporates temporary path traffic control and a localized Floyd update algorithm for real-time path adjustment
- The localized Floyd algorithm reduces computational complexity by restricting updates to locally affected regions rather than recomputing the entire path network
- Comparative experiments in a multi-zone warehouse simulation demonstrate reduced no-load rates, mitigated path congestion, and enhanced overall operational performance

## Synthesis
Published on July 24, 2026, in PLOS ONE, this research paper from Shandong University of Science and Technology addresses critical challenges in multi-AGV (Automated Guided Vehicle) systems operating in complex warehouse environments. The authors identify three key problems: high system no-load rates, low task response efficiency, and imbalanced path utilization — all of which limit the operational efficiency of intelligent warehouse systems.

The proposed solution integrates three innovations. First, a task segmentation strategy decomposes complex warehouse tasks into long-distance transport sub-tasks and precision in-racking sub-tasks, which are then allocated to heterogeneous AGV types optimized for each sub-task category. This recognizes that different AGV designs excel at different operations, and matching task to vehicle type improves overall throughput.

Second, a task pre-allocation algorithm allows AGVs to participate in the next task assignment before completing their current task. This is a significant departure from conventional approaches where AGVs must complete their current task or return to a designated waiting station before receiving new assignments. By overlapping task completion with task assignment, the system reduces idle time and improves scheduling continuity.

Third, the dynamic map path planning mechanism represents the paper's core contribution to mapping science. The system maintains a dynamic map of the warehouse environment that updates in real-time. When congestion is detected on a path segment, a temporary traffic control module redirects AGVs to alternative routes. The localized Floyd update algorithm then recalculates shortest paths only for the affected region of the map, rather than recomputing the entire path network. This dramatically reduces computational overhead compared to a full Floyd-Warshall recalculation, making real-time path adjustment feasible in dynamic environments.

The experimental validation was conducted in a multi-zone warehouse simulation environment, where the proposed approach demonstrated measurable improvements in reducing no-load rates, mitigating path congestion, and enhancing overall system performance compared to existing methods. The research has implications beyond warehouse logistics, potentially applicable to any multi-agent system requiring dynamic path planning in changing environments.