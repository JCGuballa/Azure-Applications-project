# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

### MY ANSWER

## Choosing between VM and WebApp ##
In a real world scenarion, I would recommend developing a two-tier approach for the resource options:
1. Initially implement a WebApp Service.
2. Switching to Virtual Machine (VM) if conditions change (e.g high availability, scalabity and redundancy) after project deployment to Production.

## Reasons for choosing WebApp service:
1. Cost Comparison
Azure App Service

Pricing is tied to the App Service Plan, with no OS licensing or patching overhead.
Multiple apps can share a single plan, improving overall cost efficiency.
Higher tiers support autoscaling, which optimizes cost during fluctuating demand.
Lower total operational cost due to minimal infrastructure maintenance.

Virtual Machine (VM)

Costs include compute, storage, OS licensing (for Windows), and ongoing maintenance.
VM resources run continuously unless manually stopped, leading to higher baseline cost.
Savings are possible through Spot VMs or shutting down during off-hours, but this requires active operational management.
Generally more expensive to operate long-term due to OS and server-level upkeep.


2. Scalability Comparison
Azure App Service

Built-in autoscaling based on CPU, memory, or custom metrics.
Scaling out is fast, seamless, and does not require deep infrastructure knowledge.
Deployment slots allow safe, zero‑downtime release pipelines.

Virtual Machine (VM)

Scaling requires a VM Scale Set with a load balancer and custom health checks.
Additional DevOps effort needed to maintain and monitor multiple instances.
Scaling actions take longer due to OS boot time and configuration requirements.


3. Availability Comparison
Azure App Service

Provides high availability by default without any additional configuration.
Platform-level redundancy and SLA-backed uptime are included automatically.
Supports multi-region deployment with Traffic Manager or Front Door for global resiliency.

Virtual Machine (VM)

Requires manual configuration of Availability Sets or Availability Zones to meet SLA commitments.
Achieving redundancy requires deploying multiple VMs and configuring load balancing.
Higher risk of downtime if the infrastructure is not configured correctly.


4. Workflow (Deployment & Operations) Comparison
Azure App Service

Integrated CI/CD support via GitHub Actions, Azure DevOps, and Visual Studio.
Zero OS maintenance—Azure handles patching, security updates, and runtime management.
Built-in diagnostic logs and monitoring simplify troubleshooting.
Ideal for fast deployments and efficient operational workflows.

Virtual Machine (VM)

Requires manual installation and configuration of the web server, runtime, security patches, and deployment agents.
CI/CD pipelines must be custom-built, increasing DevOps complexity.
Monitoring, patching, and troubleshooting require more technical involvement.
Slower deployment cycle and higher operational risk.


Final Recommendation
For this CMS application, Azure App Service is the optimal choice. It provides simpler operations, lower maintenance overhead, built-in scalability, and stronger availability without requiring complex infrastructure. From a business perspective, App Service minimizes deployment time, reduces operational risk, and offers more predictable cost control—making it the most efficient and effective solution for this scenario.

## Factors that would change my decision.

1. Scalability: If the WebApp’s storage or performance limits are exceeded, I may upgrade the App Service Plan or transition to a VM to better accommodate the workload.

2. Cost‑Benefit Evaluation: After moving to Production, if the operational costs outweigh the projected returns, shifting to a VM may offer better long‑term value.

2. Technical Growth: If future business requirements call for more robust infrastructure, scaling out to multiple VMs may become more appropriate—driven by business needs rather than technical preference alone.
