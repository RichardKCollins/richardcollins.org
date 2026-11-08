---
title: Cuong Le, System Efficiencies that ultimately matter to Users
date: '2026-11-03T08:22:00Z'
author: Richard Collins
handle: '@RichardKCollin2'
original_url: https://x.com/RichardKCollin2/status/2117623392022970817
platform: x
source: x-article
tags:
- writing
- research
- ai-collaboration
read_time: 7 min read
cover_image: https://pbs.twimg.com/media/HWNO0bhWYAA9__8?format=webp&name=medium
---

*Originally published on [X](https://x.com/RichardKCollin2/status/2117623392022970817) on 2026-11-03*

---

[![Article cover image](https://pbs.twimg.com/media/HWNO0bhWYAA9__8?format=webp&name=medium)](/RichardKCollin2/article/2117623392022970817/media/2117622912442064896)

# Cuong Le, System Efficiencies that ultimately matter to Users

7 min read

****Cuong Le:**** I spent 3 months benchmarking and digging into the internals of Loki, Elasticsearch, OpenSearch, ClickStack, SigNoz and VictoriaLogs, and condensed it into a 20-minute read.TL;DR: I realized who ingests fastest is only one side of the story. Every fast number had a price.I x.com/valyala/status…

****Grok:**** [@cuongleqq](https://x.com/cuongleqq), VictoriaLogs core maintainer, summarizes a 3-month benchmark of structured Kubernetes log ingestion across VictoriaLogs, Loki, Elasticsearch, OpenSearch, SigNoz, and ClickStack on identical hardware.Loki topped ingestion at 139k lines/s by indexing only labels and storing raw text, trading off for slow field-based queries that require full decompression and scans.VictoriaLogs reached 120k lines/s using the least memory and disk while delivering fast queries via columnar storage per field, though its edge is strongest on structured logs rather than plain text.

****Richard:**** Did Cuong Le survey actual users to see how these dimensions of storage, bandwidth and response times affected the system wide results?

****Grok:**** No. Cuong Le did not survey actual users for this work.The benchmark (detailed in his VictoriaMetrics blog post and the public GitHub repo) is a controlled, reproducible technical evaluation. It ran six systems (VictoriaLogs, Loki, Elasticsearch, OpenSearch, SigNoz, ClickStack) in single-node mode on identical 8-vCPU/32 GB Kubernetes nodes, feeding them synthetic structured Kubernetes-style logs (≈930 bytes/line, 30–40 fields, simulating ~5,000 streams). It measured maximum sustained ingestion rates, CPU, memory, disk space, disk writes, and some query performance after loading data.There is no mention of user surveys, interviews, questionnaires, production telemetry from customers, or empirical studies of how storage/bandwidth/response-time differences played out in real deployments or affected “system-wide results.” The motivation stated is that users frequently ask which tool fits which use case (and what they would gain by switching), so the team published controlled numbers plus explanations of the internal trade-offs (e.g., Loki’s label-only indexing vs. columnar storage, indexing cost vs. query speed, disk amplification). Query concurrency, multi-node/cluster behavior, object storage, and unstructured logs are explicitly noted as future work.Anecdotal user comments appear elsewhere (Reddit, Hacker News, other independent benchmarks), but they are not part of this study and were not systematically collected by Cuong Le for it. The results are best treated as precise lab measurements of design trade-offs on a specific workload, not as a survey of real-world system-wide impact.**Sources linked in the saved Grok response:** [VictoriaMetrics benchmark](https://victoriametrics.com/blog/structured-log-ingestion-benchmark/); [Benchmark harness](https://github.com/VictoriaMetrics/logs-benchmark).

****Richard:**** It seems that logging users and asking them, and having open channels for them to give feedback and suggestions and work on new things is better then remote workers guessing at the actual uses of a system.

****Grok:**** User feedback is valuable and often better than pure developer speculation for understanding real workloads, pain points, and priorities. Controlled benchmarks and open user channels serve different purposes and work best together rather than as substitutes. VictoriaMetrics maintains public channels specifically for this: a community Slack (with dedicated logs channels), GitHub issues and PRs (including “help wanted” labels), virtual meetups, and conference interactions where they explicitly collect feedback for the roadmap. Their case studies and community posts also include real-user reports of storage, CPU, and query behavior. The benchmark itself was motivated by users repeatedly asking which tool fits which use case.That said, a synthetic benchmark is not mainly “guessing.” It isolates variables (identical hardware, fixed log shape, ramped rates, cold caches) so differences in ingestion rate, memory, disk amplification, and query latency can be attributed to design choices rather than to uncontrolled production factors. Those numbers are hard to get cleanly from user reports alone, which tend to be self-selected, incomplete, and confounded by collectors, networks, retention policies, and concurrent load. Users can still run the public harness themselves on their own data.The practical gap is that the published write-up does not include a systematic survey or production telemetry study of how the measured storage/bandwidth/response-time differences actually affected end-to-end systems. Open channels reduce the “remote guessing” problem, but they do not automatically turn every technical comparison into an evidence-based account of real-world impact. Both approaches are useful; neither fully replaces the other.**Sources linked in the saved Grok response:** [VictoriaMetrics benchmark](https://victoriametrics.com/blog/structured-log-ingestion-benchmark/); [VictoriaLogs source code](https://github.com/VictoriaMetrics/VictoriaLogs).

****Richard:**** Documenting and sharing current validated benchmarks on actual systems is necessary. It is good he is doing this. But it is the whole system that matters. My complaint about most software on the Internet is that the developers and promoters never actually talk to user. Before you say they do, look closely and most of the innovators mostly talk to a next layer of developers who might talk to users, or more developer layers.

****Grok:**** The critique is fair on both counts: isolated component numbers are incomplete without system-level effects, and developer-to-developer communication layers are a real filter that often replaces direct contact with the people whose work or outcomes are affected.In observability and infrastructure software the primary customers are usually platform teams, SREs, and observability engineers rather than the application developers who emit the logs or the business teams that consume the insights. VictoriaMetrics case studies (Spotify, Grammarly, MongoDB, etc.) quote those platform and observability roles; their public Slack and GitHub channels are likewise dominated by the same layer. That is not unusual—most open-source infrastructure projects work this way—but it means feedback about storage cost, query latency, or ingestion rate is still one or two hops removed from the full workflow (log emission, collection, network, retention, dashboard load, incident response, and the decisions those tools support).Controlled benchmarks remain useful for the narrow claims they make: under a fixed hardware budget and a defined log shape, what are the relative costs of different storage and indexing designs. They do not, and in this case do not claim to, measure how those differences propagate through a real pipeline or change team behavior. Publishing the harness openly lets other engineers test closer to their own conditions, which is better than pure assertion, but it still leaves the system-wide and multi-layer feedback problem unaddressed.The broader pattern you describe is common across infrastructure tooling: maintainers talk most readily to the engineers who operate the software, those engineers talk to the teams who write applications, and the original operational or product goals can become attenuated. Open channels and case studies reduce the distance; they do not eliminate the layers.

****Richard:**** If you look at "database" or "open software" as a node on the Internet (I do for the Internet Foundation), it is a hierarchical structure with one top, horizontal links, but many many layers downward. Any person or group in open projects can insert themselves into pipelines and dependency chains (or attempt to).

****Grok:**** Open-source software ecosystems do form graphs that are hierarchical in practice while remaining open at the edges.A package or database is a node. Direct dependents are few; transitive dependents are often many layers deep. GitHub and ecosystem data routinely show projects with tens of direct dependencies and hundreds to thousands of total packages once the full tree is resolved. Control concentrates at the maintainer of each node (who merges, releases, and sets defaults), while anyone can fork the node, wrap it, replace it, or insert an intermediate component into the path that leads to it. Horizontal links exist—shared standards, compatible protocols, competing implementations—but they do not remove the depth of the dependency trees.That structure is exactly what allows the layering you described earlier. Between an application that emits logs and a storage system such as VictoriaLogs sit collectors, processors, proxies, Kubernetes sidecars, network hops, and dashboard layers. Any of those can be introduced, replaced, or extended by a different group without the original maintainers’ involvement. The same openness that lets people insert themselves into the chain also multiplies the filters between the people who design a component and the people whose systems or outcomes are affected by it.For a database treated as one node, the practical consequence is that its measured properties (ingestion rate, disk amplification, query latency) can be altered, amplified, or hidden by every layer above and below it. The graph is open enough for new nodes to appear, yet deep enough that most participants never interact with the original maintainers or the ultimate consumers of the data.**Source linked in the saved Grok response:** [GitHub dependency graph](https://github.blog/security/supply-chain-security/understand-your-softwares-supply-chain-with-githubs-dependency-graph/).

****Richard wrote to OpenAI GPT:**** Can you make three 2000x800 pngs?

1. The user side of this system showing up to 6 billion Internet users who might touch the software in some fashion. A corporation using tools will have internal staff and vendor. All of them should be able to see ONE system map of the whole.
2. Paths and systems that connect users to developers. When developers make "user communities", they tend to devolve to "only themselves".
3. The developers and testing, the whole side of "software and system development". It has devolved to "insiders only" and the users are almost completely excluded. And data on real users is mostly inaccessible, because the developers do not listen and make changes.

****OpenAI GPT created:****

[![](https://pbs.twimg.com/media/HWNOOaPXIAA-zcE.jpg)](/RichardKCollin2/article/2117623392022970817/media/2117622259263152128)

[![](https://pbs.twimg.com/media/HWNOc3EXoAAdU7i.jpg)](/RichardKCollin2/article/2117623392022970817/media/2117622507519844352)

[![](https://pbs.twimg.com/media/HWNOl2tXIAACDZV.jpg)](/RichardKCollin2/article/2117623392022970817/media/2117622662042165248)

Full conversation with Grok at <https://x.com/i/grok/share/04694f3861994b559296e49fb2eef192>

Full conversation with OpenAI GPT at <https://chatgpt.com/share/6ae9edf8-7d64-83e9-9202-2579afb3f71c>
