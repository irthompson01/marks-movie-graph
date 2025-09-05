# BlastOne Industrial Painting & Blasting — Data Strategy and Investigation Project Proposal

Prepared for: BlastOne International (Industrial Painting & Blasting Contractors)  
Focus: Surface underlying data issues and deliver a phased plan to discover, validate, and resolve them; convert into a 40-hour/month operating cadence tied to revenue, margin, throughput, and safety outcomes.

---

## 1) Executive Summary

- Business context
  - BlastOne is a global specialist in corrosion control and protective coatings, providing engineered systems, equipment/consumables, rentals, service, calibration, and training. The brand promise is to help customers complete projects safer, faster, cleaner, and more profitably, supported by Productivity Squared (P2) methodology.
  - Core revenue engines: ecommerce product sales, rentals fleet, engineered systems/projects, and service/calibration programs. Operations span US, AU/NZ, and APAC.

- Problems we will investigate and resolve
  - Fragmented data across WooCommerce (web), CRM/HubSpot, ERP (orders, inventory, rentals, finance), ticketing/service, calibration, SharePoint (projects), and OT/SCADA historian.
  - Inventory accuracy and lead-time sync to ecommerce; rental asset utilization/maintenance visibility; service/warranty SLAs; project margin and risk visibility; calibration traceability; inconsistent KPI definitions; limited OT/IT convergence for P2 KPI capture.
  - Resulting impacts: backorders and conversion drag; margin leakage in rentals/projects; delayed SLA/warranty decisions; compliance burden; slower throughput improvement and sales cross-sell.

- Outcomes and business impact (90-day targets)
  - Revenue: +3–5 points rental utilization identified actions; 10% reduction in backorder incidents for top SKUs; enable cross-sell focus via Customer 360 for top 100 accounts.
  - Margin: Early visibility into rental turnaround, service warranty costs, and project risk; a baseline to reduce margin leakage.
  - Throughput: Standard KPI definitions for P2; plan for historian integration to measure sq ft/hr, abrasive consumption per sq ft, pressure stability.
  - Safety/Compliance: Weekly calibration due reminders with <1% fail rate; improved access to certificates.

- Our approach
  - Investigation-first with clear hypotheses, stakeholder interviews, access requests, data profiling, and lineage mapping. Build small but valuable pilots/POCs to validate assumptions, quantify benefits, and create a governance backbone.
  - Establish a lightweight data hub, canonical models, and Power BI datasets; formalize KPI catalog, data owners, and refresh SLAs.
  - Operate in a strict 40-hour/month cadence with biweekly demos and monthly governance checkpoints.

---

## 2) Current State and Gap Analysis

- Systems and data domains (inferred from public materials and typical industry patterns)
  - WooCommerce on WordPress: product catalog, pricing, customers, carts, quotes, orders.
  - CRM/Marketing: HubSpot (per Privacy Policy), possibly Salesforce; leads, contacts, companies, activities, opportunities, campaigns.
  - ERP (NetSuite or Microsoft Dynamics per careers signals): items/SKUs, inventory, orders/invoices, purchasing, GL/AP/AR, rentals, service, multi-entity/locations.
  - Rentals/fleet: module in ERP or adjacent system; assets, reservations/contracts, check-in/out, inspections, maintenance history.
  - Service/ticketing: helpdesk for cases, dispatch, RMAs, warranty adjudication, parts/labor; calibration repository for certificates/due dates.
  - PM/document control: SharePoint or similar for engineered projects (FAT/SAT, as-builts, QA/QC docs).
  - OT/SCADA/historian: PLC/HMI controls capturing airflow, pressure, humidity, cycle times, alarms, OEE, and consumables; used for production insights and P2 improvements.
  - Analytics: Power BI/Tableau used across Sales, Operations, Finance.

- Data flows (as-is)
  - Leads from web to HubSpot; ecommerce orders to ERP; rentals reserved/returned with inspections; service tickets into helpdesk and ERP for billing; project lifecycle across CRM→ERP→SharePoint; calibration managed by lab; limited historian-to-BI integration.

- Pain points and gaps
  - Customer 360: Duplicates and disconnected identity across WooCommerce, CRM, and ERP limit retention, cross-sell, and service history visibility.
  - Inventory/lead-time accuracy: Sync latency and custom Woo metadata may cause backorders and conversion loss.
  - Rentals: Split data between ERP, inspections, and service; underreported utilization, time-to-turn, and maintenance costs by asset/branch.
  - Service SLAs and warranty: Missing or inconsistent SLA calculations and parts/warranty attribution.
  - Project profitability: Budget vs actuals and change-order governance rely on manual reconciliation with PM docs; delayed margin-erosion alerts.
  - P2 KPI standardization: Inconsistent definitions and units for throughput, abrasive consumption, and environmental metrics; historian data siloed from BI.
  - Compliance burden: Calibration reminders, certificate access, and environmental/safety logs fragmented.

- Risks/compliance
  - OSHA/EPA recordkeeping, ISO 9001, and privacy obligations; calibration traceability; safe OT data egress and ISA/IEC 62443-aligned architectures.

---

## 3) Investigation Plan

- Hypotheses to test
  - H1: Stock status and lead-time in WooCommerce do not update quickly enough from ERP, causing preventable backorders and lower conversion.
  - H2: Rental asset utilization and margin per asset-day are not measured consistently; maintenance turn time and overdue returns create revenue loss.
  - H3: Customer and account duplication across WooCommerce, HubSpot, and ERP is >10% among top accounts, limiting sales efficiency and service context.
  - H4: Service SLA and warranty costs are not measured uniformly across branches; parts usage is not linked cleanly to installed base.
  - H5: P2 KPIs lack a standard schema and units; historian data is not accessible in BI, limiting throughput and quality optimization.

- Discovery activities
  - Stakeholder interviews: Ecommerce Manager, VP Sales/Marketing, Rentals Director, Service Manager, Calibration Lead, PMO, Controls Engineering, Finance Controller, IT/ERP Analyst.
  - Access requests: Read-only APIs/exports for WooCommerce (wc/v3), ERP (items, inventory, rentals, orders, customers), HubSpot (contacts/companies), ticketing, calibration repository; Power BI workspace and gateway.
  - Data profiling: Field-level completeness, duplicates, key integrity (SKUs, customer IDs), timestamp coverage, and refresh latency.
  - Lineage mapping: Order-to-cash, rentals dispatch/return, service ticket to invoice/warranty, project artifacts to ERP job, historian-to-report.
  - SLA and definition workshops: Agree on KPI definitions for Utilization, OTIF, FTFR, Inventory Accuracy, Warranty Rate, Time-to-Turn, and P2 metrics.
  - Security/governance review: Roles, least-privilege access, data handling of PII, and OT security zones.

- Deliverables from discovery
  - Source-to-model mapping, lineage diagrams, data contracts, KPI dictionary v0.1, DQ/latency baselines, and prioritized issues list with owners.

---

## 4) Pilots and Proofs of Concept

Pilot 1: Inventory Accuracy Monitor (WooCommerce vs ERP)
- Objective: Reduce backorders and increase web conversion by detecting and resolving stock/lead-time mismatches.
- Scope: Top 500 SKUs across key branches/DCs; daily refresh.
- Success criteria:
  - Daily exception list generated by 6 AM local; baseline mismatch rate reduced by 50% within 90 days for monitored SKUs.
  - 10% reduction in “order placed on backorder” incidents.
- Data needed: WooCommerce products/stock/metadata (including any custom fields for lead-time/backorder); ERP inventory availability and lead-time; item master mapping.
- Approach: ELT to a central staging; Power BI dashboard with exceptions, drill-through to item branch; owners and remediation workflow.
- Timeline: 3 weeks to v0; continuous improvement thereafter.
- Estimated hours: 16h initial (ELT 8h, model 4h, dashboard 4h); 2–3h/month to maintain.

Pilot 2: Rental Utilization and Margin v1
- Objective: Lift utilization and margin per asset-day; reduce overdue returns and improve time-to-turn.
- Scope: ≥90% of fleet; daily refresh; focus on top rental classes (dust collectors, vacuums, blast pots).
- Success criteria:
  - Baseline utilization by branch/asset class; identify actions to gain +3–5 points.
  - Overdue returns list and maintenance turn time trending; target 15% reduction in turn time over 90 days (where process changes applied).
- Data needed: ERP rental contracts (start/end, rate, location, asset), asset master, maintenance/inspection events, revenue and cost elements.
- Approach: Day-grain fact for asset availability and contract coverage; Time-to-Turn KPI; Power BI report with branch filters and export.
- Timeline: 4 weeks to v1.
- Estimated hours: 18h initial (ELT 8h, model 6h, dashboard 4h); 3–4h/month enhancements.

Pilot 3: Calibration Reminders and Certificate Index
- Objective: Reduce compliance risk by ensuring upcoming calibration due dates are proactively managed and certificates are easily retrievable.
- Scope: All instruments with due within 60/90 days; weekly batch email/CSV and optional customer notifications.
- Success criteria:
  - <1% reminder failure rate; spot-check accuracy on 20 instruments; certificate lookup time <1 minute via indexed links.
- Data needed: Calibration repository (assets, due dates, certificate URLs/IDs, customer).
- Approach: Scheduled job (Python/Power Automate) to generate lists and distribute; Power BI log for monitoring delivery and exceptions.
- Timeline: 2 weeks to go-live.
- Estimated hours: 8h initial; 1h/month maintenance.

Pilot 4: Customer 360 Slice (Top 100 Accounts)
- Objective: Enable cross-sell, retention, and service context by consolidating WooCommerce, HubSpot, and ERP identities and activity.
- Scope: Top 100 accounts; weekly refresh; dedupe rules using email/domain, mapping tables.
- Success criteria:
  - Duplicate rate <10%; ability to view orders, tickets, rentals per account; adoption by Sales and Service teams.
- Data needed: WooCommerce customers, HubSpot contacts/companies, ERP customers, orders, tickets summary.
- Approach: Identity resolution and conformed Account dimension; DQ report and stewardship workflow with owners.
- Timeline: 4–6 weeks to v0.1.
- Estimated hours: 22h initial (ELT 8h, model 10h, DQ and enablement 4h); 4h/month to iterate.

Pilot 5: Service SLA and Warranty v1
- Objective: Improve FTFR and reduce warranty costs by measuring response/resolve times and attributing parts/warranty to installed base.
- Scope: Ticketing covering ≥70% of volume; weekly refresh; link to assets/customers where possible.
- Success criteria:
  - SLA definition ratified; top 5 improvement opportunities identified; baseline FTFR and warranty rate per branch/customer.
- Data needed: Tickets (created/responded/resolved), parts used, warranty flags, asset and customer linkage from ERP.
- Approach: SLA fact table; FTFR and warranty rate calculations; PDF summary auto-emailed to Service leadership.
- Timeline: 4–5 weeks to v1.
- Estimated hours: 20h initial (ELT 6h, model 8h, dashboard 6h); 3h/month maintenance.

---

## 5) Recommended Architecture and Tooling Approach

- Integration pattern
  - Phase 1: Lightweight data hub (Azure SQL/SQL Server or lakehouse if available). ELT pulls from WooCommerce wc/v3, HubSpot, ERP (via API or scheduled exports), ticketing, calibration. Daily/weekly refresh per domain.
  - Phase 2: Event-driven ERP→WooCommerce updates for stock and lead-time, targeting <15-minute SLA for top SKUs.
  - Phase 3: OT onramp. Historian/PLC data connector into lakehouse for P2 KPIs; standard schema for pressures, airflow, RH, cycle times, alarms, OEE, abrasive consumption.

- Canonical data model (initial)
  - Dimensions: Customer/Account, Contact, Item/SKU, Asset (rental), Project, Location/Branch, Date/Time.
  - Facts: Inventory Snapshot, Orders, Rental Day Coverage, Tickets/SLA, Calibration Events, Ecommerce Sessions/Orders (optional), Warranty Claims.

- Analytics and reporting
  - Power BI datasets and workspaces per domain (Ecommerce, Rentals, Service, Exec Scorecard).
  - Row-level security by region/role; scheduled refresh via on-prem gateway or cloud.

- Tooling
  - ELT: Python/Node or Power Automate for API pulls and file ingestion; existing job scheduler.
  - Storage: Azure SQL or existing SQL Server; evolve to lakehouse for OT data.
  - Visualization: Power BI as standard.  
  - Security: Least-privilege service principals; credential vaulting; audit logging.

---

## 6) Governance, Quality, and Security Approach

- Governance controls
  - KPI catalog and data dictionary with business owners and update SLAs.
  - Data contracts per source (owner, cadence, fields, quality expectations, incident process).
  - Change management: Versioned models; acceptance templates; biweekly demo and monthly executive sign-off.

- Data quality
  - Monitors: Inventory accuracy, duplicate customer rate, rental coverage %, SLA data completeness, calibration reminder delivery.
  - Exception queues: SKU mismatches, duplicate accounts, overdue returns, missing ticket timestamps.

- Security and privacy
  - Align to privacy policy: control PII access, minimize extracts, enforce retention and deletion practices.
  - Role-based access, MFA, row-level security; OT data egress designed with ISA/IEC 62443 zones and conduits; historian read-only connectors.

- Ownership
  - Domain data owners: Ecommerce (WooCommerce), Sales/Marketing (HubSpot/CRM), Operations/Finance (ERP), Rentals, Service, Calibration, PMO, Controls Engineering.
  - BI and Data Hub stewardship: IT/ERP Analyst + BI Lead; this engagement provides design and QA.

- SLAs
  - Refresh SLAs documented by domain (e.g., daily inventory/rentals; weekly SLA/warranty; weekly calibration reminders).
  - Incident runbook: detection, triage within 4 business hours, resolution target within 2 business days unless upstream blockers.

---

## 7) Roadmap and Prioritized Backlog

- 30–60–90 day plan
  - Days 0–30: Access, ingestion for WooCommerce/ERP/calibration/rentals; Inventory Accuracy Monitor; Rental Utilization baseline; KPI catalog v0.1; calibration reminders live.
  - Days 31–60: Add HubSpot and ticketing extracts; Customer 360 v0.1; Ecommerce Availability Impact dashboard; Rental v1 (margin/time-to-turn); stewardship workflow.
  - Days 61–90: Service SLA and warranty dashboard; Executive KPI scorecard; ERP→WooCommerce event feed specification; P2 KPI schema and OT integration plan; governance ratified.

- Prioritized backlog (with impact/effort)
  - P1 (0–90 days):
    1) Inventory Accuracy Monitor — High impact, low-medium effort.
    2) Rental Utilization v1 — High impact, low-medium effort.
    3) Calibration reminders — Compliance-critical, low effort.
    4) Customer 360 v0.1 — High impact, medium effort.
    5) Service SLA v1 — High impact, medium effort.
    6) Executive KPI scorecard — High alignment, medium effort.
  - P2 (scope in 0–90; build months 4–6):
    7) ERP→WooCommerce near-real-time stock/lead-time — Very high impact, high effort.
    8) Installed Base master (Assets↔Customers↔Tickets↔Warranty) — High impact, medium-high effort.
    9) Project margin early warning (ERP + SharePoint) — High impact, medium-high effort.
  - P3 (strategic):
    10) P2 KPI standard model + historian pipeline (pilot) — Strategic impact, high effort.
    11) Rental check-in/out mobile inspections digitization — Medium-high impact, medium effort.

---

## 8) 40-Hour/Month Scope, Timeline, and Hour Allocation

Months 1–3 detailed allocation (40h/month)

- Month 1 (Quick wins and foundations)
  - Program management and stakeholder alignment: 6h
  - Ingestion: WooCommerce 6h; ERP items/inventory/rental 8h; Calibration 3h
  - Modeling: Item, Inventory Snapshot, Rental Asset/Contract: 6h
  - Analytics: Inventory Accuracy Monitor 5h; Rental Baseline 4h
  - Governance and documentation: KPI catalog v0.1 and SLAs 2h

- Month 2 (Customer 360 and ecommerce insights)
  - Program management: 5h
  - Ingestion: HubSpot + ticketing 6h; ERP orders/customers 5h
  - Modeling: Customer 360 v0.1 8h; Rental enrichment 3h
  - Analytics: Ecommerce Availability Impact 5h; Rental v1 enhancements 4h
  - Governance & enablement: Stewardship workflow + training 3h; docs/templates 1h

- Month 3 (Service reliability and exec alignment)
  - Program management: 5h
  - Ingestion: Ticketing SLA + warranty 5h
  - Modeling: Service SLA fact + Installed Base link 8h
  - Analytics: Service SLA v1 7h; Executive KPI Scorecard v1 6h
  - Integration readiness: ERP→Woo feed spec 5h; P2 KPI schema & OT plan 4h

Steady-state (after Month 3) typical month (40h)
- Ingestion/ELT: 12h
- Modeling/MDM-lite: 10h
- Analytics/BI: 10h
- Governance/quality: 4h
- Enablement/PM/demos: 4h

---

## 9) KPIs, SLAs, and Measurement Plan

- Ecommerce
  - KPIs: Conversion by availability status; AOV; backorder incident rate; % SKUs with accurate lead times; time-to-update inventory on site.
  - SLA: Inventory/lead-time data refresh daily (Phase 1); <15 minutes for top SKUs after event feed (Phase 2).
  - Target (90 days): 10% reduction in backorder incidents on top 500 SKUs.

- Rentals
  - KPIs: Utilization %, revenue per asset-day, time-to-turn, overdue returns %, maintenance cost/hour, margin per asset-day.
  - SLA: Daily refresh for rental day coverage and asset master.
  - Target (90 days): +3–5 points utilization improvement identified with actions; 15% reduction in turn time where process applied.

- Service
  - KPIs: Response time, resolve time, FTFR, warranty claim rate and cost; parts usage; SLA adherence.
  - SLA: Weekly refresh of SLA dataset; weekly PDF summary to leadership.
  - Target (90 days): Top 5 improvement opportunities actioned; FTFR +2–3 points baseline improvement where parts stocking actions are taken.

- Project delivery (scope in months 4–6)
  - KPIs: Project GM%, schedule adherence, CO rate, rework cost; early warning index.
  - SLA: Weekly refresh.

- P2/OT
  - KPIs: Throughput (sq ft/hr), abrasive consumption per sq ft, nozzle pressure stability, OEE, downtime by cause.
  - SLA: Pilot ingestion weekly in Month 6; move toward daily where feasible.
  - Target: Pilot site benchmark vs pre-implementation, establish variance and improvement levers.

- Compliance and calibration
  - KPIs: % instruments with on-time reminders; certificate retrieval time; audit readiness score.
  - SLA: Weekly reminder job with <1% failure; certificate index refreshed weekly.

- Governance adoption
  - KPIs: KPI catalog coverage (#KPIs standardized), data owner assignment rate, dashboard MAUs, incident MTTR.
  - Targets: 20+ KPIs standardized by Month 6; 50+ monthly active dashboard users.

Measurement approach
- Each dashboard includes clearly defined metrics, owners, refresh timestamps, and targets; monthly exec scorecard consolidates results and actions.

---

## 10) Implementation Plan with Estimates and Assumptions

- Environments and access (Weeks 1–2)
  - Provision read-only API keys/exports: WooCommerce wc/v3, ERP (items/inventory/rentals/orders/customers), HubSpot, ticketing, calibration.
  - Set up Power BI workspace, data gateway, role groups; provision SQL staging or use existing analytics DB.

- Build sequence (Weeks 1–12)
  - Weeks 1–3: ELT pipelines (Woo/ERP/calibration/rentals); Inventory Accuracy Monitor; calibration reminders.
  - Weeks 3–6: HubSpot/ticketing ingestion; Customer 360 v0.1; Ecommerce Availability Impact; Rental v1 (margin/time-to-turn).
  - Weeks 6–9: Service SLA and warranty dataset; Service SLA v1; Executive KPI Scorecard; governance ratification.
  - Weeks 9–12: ERP→WooCommerce event feed spec; P2 KPI schema and OT integration plan; backlog grooming for Months 4–6.

- Assumptions
  - Access granted within 10 business days; ERP supports API or scheduled extract; ticketing covers ≥70% of service volume.
  - Existing infrastructure for job scheduling; Power BI licensing in place.
  - Stakeholders available for weekly/biweekly decisions.

- Cost and effort (within 40h/month)
  - Months 1–3: 120 hours total as allocated above.
  - Months 4–6: Continue at 40h/month; allocate to building near-real-time ERP→Woo feed, Installed Base master, project margin early warning, and P2 pilot ingestion.

---

## 11) Risks, Assumptions, and Next Steps

- Key risks and mitigations
  - ERP throttling or schema drift: Use incremental extracts, schema validation tests, and retry logic; coordinate change windows with IT.
  - Data quality (duplicates, custom fields): MDM-lite rules; exception queues; focus on top accounts/SKUs first.
  - Scope creep vs. 40h cap: Timeboxed sprints; DoD/acceptance criteria per deliverable; backlog discipline.
  - Adoption: Biweekly demos; enablement for Sales, Rentals, Service; KPI owners named with targets.
  - OT security: Plan-first approach; adhere to ISA/IEC 62443; historian read-only; segregated networks.

- Assumptions and dependencies
  - Read-only access to systems; Power BI workspace/gateway available; SQL staging approved by IT; privacy and compliance policies followed.
  - One domain POC per function (Ecommerce, Rentals, Service, Finance, Controls) to expedite decisions.

- Next steps (Weeks 0–2)
  - Confirm executive sponsor and domain owners.
  - Approve this proposal and 90-day roadmap.
  - Provision credentials and environments.
  - Schedule discovery interviews and KPI definition workshops.
  - Kick off with a 60-minute alignment session; set biweekly demos and monthly executive checkpoint.

---

## 12) Governance Checkpoints and Communication Cadence

- Biweekly stakeholder review (30 minutes)
  - Demo new increments, decide on open questions, assign owners for exceptions.
- Monthly executive checkpoint (45–60 minutes)
  - Sign-off on deliverables vs DoD; KPI performance review; prioritize next month’s 40 hours.
- Quarterly steering (60 minutes)
  - Review outcomes vs revenue, margin, throughput, safety; approve strategic items (ERP→Woo real-time, Installed Base, P2 pilot expansion).

---

## 13) Appendix — Definitions, DoD, and References

- Definitions (examples)
  - Inventory Accuracy: % of SKUs where WooCommerce stock/lead-time matches ERP within defined thresholds.
  - Rental Utilization: Asset contract-covered days / available days, adjusted for maintenance holds.
  - Time-to-Turn: Days from asset return to next ready-for-dispatch status.
  - FTFR: % of service requests resolved on first onsite visit (parts availability considered).
  - Warranty Rate: Warranty claims / total service jobs, with cost attribution.

- DoD per deliverable (abbreviated)
  - Inventory Accuracy Monitor: Daily refreshed Power BI, exception workflow, owner assigned; validated on 25 sampled SKUs.
  - Rental v1: Utilization %, overdue list, revenue/asset-day; coverage ≥90% fleet; definitions approved by Rentals and Finance.
  - Calibration reminders: Weekly job; <1% failure; 20-record spot-check accuracy; certificate links resolvable.
  - Customer 360 v0.1: Top 100 accounts matched; duplicate rate <10%; DQ report; stewardship workflow signed off.
  - Service SLA v1: Ratified SLA formulas; PDF email; top 5 opportunities surfaced and assigned.
  - Exec Scorecard v1: 1-page consolidated KPIs with owners, targets, and trends; adopted in monthly ops review.
  - ERP→Woo Feed Spec: Payloads, transport, error handling, <15 min SLA for top SKUs; build estimate and plan.
  - P2 Schema & OT Plan: Standardized model for throughput/consumables/conditions; pilot site identified; security architecture outlined.

- Selected references (public)
  - About (company overview, mission): https://www.blastone.com/about/
  - Automation & Controls (metrics, data, PLC/SCADA): https://www.blastone.com/automation/
  - Rentals (fleet offerings): https://www.blastone.com/rentals/
  - Privacy Policy (HubSpot, analytics, platforms): https://www.blastone.com/privacy-policy/

---

This plan gives BlastOne a clear investigative path, tangible pilots tied to revenue and margin, a pragmatic architecture, and a disciplined 40-hour/month operating model with governance and security guardrails—accelerating conversion, utilization, throughput, and compliance.