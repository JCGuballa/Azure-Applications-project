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
1. Deploying a Virtual Machine (VM) appears to be more cost‑effective than using an Azure WebApp. A WebApp requires a paid App Service Plan, and if the application is not fully utilized, the subscription cost may outweigh its benefits. In contrast, VMs offer more granular cost‑control options such as selecting lower‑tier SKUs, using Spot instances, or shutting down the VM outside business hours to reduce compute costs. Additionally, Azure Cost Management tools—like budgets, cost alerts, usage analysis, and Azure Advisor recommendations can help track spending in real time and prevent unnecessary charges. If the project does not gain traction, the App Service Plan or VM can be deallocated or deleted to immediately stop billing.
2. While a VM offers strong advantage, such as flexibility, performance, and full control over hosting—it's important to assess whether these capabilities are truly required for the project. Since they likely aren’t, I’ve chosen to proceed with the simpler and more efficient alternative: using a WebApp.

## Factors that would change my decision.

1. Scalability: If the WebApp’s storage or performance limits are exceeded, I may upgrade the App Service Plan or transition to a VM to better accommodate the workload.

2. Cost‑Benefit Evaluation: After moving to Production, if the operational costs outweigh the projected returns, shifting to a VM may offer better long‑term value.

2. Technical Growth: If future business requirements call for more robust infrastructure, scaling out to multiple VMs may become more appropriate—driven by business needs rather than technical preference alone.
