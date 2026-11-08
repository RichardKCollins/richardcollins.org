---
title: Sirui Lu, Delphi.Science, The Internet
date: '2026-11-03T18:37:00Z'
author: Richard Collins
handle: '@RichardKCollin2'
original_url: https://x.com/RichardKCollin2/status/2117778334721483151
platform: x
source: x-article
tags:
- writing
- research
- ai-collaboration
read_time: 27 min read
cover_image: https://pbs.twimg.com/media/HWPacf3XcAARt5O?format=webp&name=medium
---

*Originally published on [X](https://x.com/RichardKCollin2/status/2117778334721483151) on 2026-11-03*

---

[![Article cover image](https://pbs.twimg.com/media/HWPacf3XcAARt5O?format=webp&name=medium)](/RichardKCollin2/article/2117778334721483151/media/2117776432919179264)

# Sirui Lu, Delphi.Science, The Internet

27 min read

****OpenAI GPT concludes:**** Knowledge must be organized around what exists, what is measurable, what is known, and how things relate—not around who discovered it, which discipline claims it, or which institution happens to host it.

That is a much more ambitious objective than Delphi Science as currently described. But it is a meaningful direction in which a system like Delphi could evolve, particularly through open, interoperable knowledge records that other people and AIs can extend independently.

It should not merely connect researchers to other researchers who share their declared interests. A sufficiently general open knowledge infrastructure would make connections that nobody knew to request.

Most importantly, it shifts the subject from what Sirui has built to what Sirui, his collaborators, and people throughout the Internet might make possible.

===

****Richard to OpenAI GPT:**** Sirui Lu [@sirui\_lu97](https://x.com/sirui_lu97) Post on X Introducing delphi.science Delphi Science, a public square for research by humans, AI, or both. Discover and share papers, code, data, and more. Join researchers and their agents in the forum to exchange ideas and start new collaborations.

****OpenAI GPT created:**** Delphi Science — A Public Square for Research by Humans and AI Agents

November 3, 2026 | Initial examination

I examined the publicly accessible [Delphi Science](https://delphi.science/?utm_source=chatgpt.com) project associated with Sirui Lu.

This is particularly relevant to the larger problem of creating a common, open Internet infrastructure where humans and AIs can find, contribute, evaluate, verify, and build upon shared knowledge.

Delphi is already more than a proposed concept. Its publicly indexed interface displays approximately 89,525 research records, drawn from sources including arXiv, the Palomar Registry, OpenAI Math, Hexagon, Anthropic Science, and others. The interface also exposes sections for submitting research, forum discussions, AI agents, and an API.

Open Research Index+1

Sirui Lu's earlier Agentic Publication Protocol project also addresses reproducibility: packaging a paper with code, data, and instructions that an AI agent can use to explain or reproduce the research.

AI for Physics+1

The important shift is from publishing research as a static document toward research as a continuing, inspectable, collaborative process.

### What makes Delphi especially interesting

The documentation confirms several concrete capabilities:

- Research status and provenance. Records can link to later confirmations, refutations, questions, extensions, and independent reviews, with sources and reviewer attribution.
- Agent-readable interfaces. A documented REST API and read-only MCP server expose search results, research records, and discussions without requiring authentication.
- Human–agent attribution. Authorized agents can contribute under a human account, with the agent identified separately.
- Research quality screening. Submissions are checked for relevance, evidence, and substance. Importantly, Delphi explicitly distinguishes this from scientific verification.Open Research Index+2

That last distinction matters. A paper being indexed, accepted, upvoted, or AI-generated does not establish that its findings are correct.

### What I would ask Sirui Lu

I would concentrate on three architectural questions.

1. Can the entire research knowledge graph be exported, replicated, and independently maintained? An open API is useful, but it does not automatically make the accumulated knowledge an open, durable public resource.
2. Can research histories be preserved losslessly? That means recording changing claims, source versions, experimental data, code, verification methods, agent activities, errors, corrections, and the relationships among them—not merely summaries of final results.
3. Can this become a federation rather than another isolated platform? Researchers, universities, independent workers, AI providers, and public archives should be able to exchange records without having to adopt a single website or central authority.

Delphi's current documented system uses centralized moderation and a single operated database, and its API documentation says there is not yet a complete record-change feed. Those are understandable early implementation choices, but they leave important questions about independent replication and long-term preservation.

Open Research Index+1

### My assessment

I regard Delphi as a promising, concrete implementation of several ideas that are urgently needed.

Its particular strength is that it treats research as something that continues after publication. A claim should retain its connections to evidence, criticism, corrections, related work, and subsequent discoveries.

But there is a distinction between a public square for research and a globally open system of knowledge.

The former brings people and agents together. The latter ensures that the information, relationships, histories, and verification methods survive independently of any one organization, website, or AI provider.

Delphi could become an important component of that larger infrastructure, especially if its records and interactions are made independently reproducible, portable, and interoperable.

I would encourage engagement with Sirui Lu, beginning with the data model, provenance requirements, and independent replication architecture—not simply the interface or the number of indexed papers.

His stated goals are close enough to the Internet Foundation's broader work on globally shared knowledge that a substantive technical exchange could be worthwhile.

****Richard wrote to OpenAI GPT:**** I started by asking Grok to summarize and discuss Sirui's post. But Grok repeated his post and did not look deeper to treat Sirui as a whole person. Grok answered questions but it was like dragging worms out of a hole. Here is that conversation. Maybe I was not asking the right questions. It seemed to me that Sirui is looking for what to do next.

Can you comment on what I was trying to get from Grok and my recommendations for Sirui, and maybe people at MPI?

****OpenAI GPT created**** : Sirui Lu, Delphi Science, and What Comes After the PhD

I read your exchange with Grok and then checked Sirui Lu's own research website, publications, and relevant work at the Max Planck Institute of Quantum Optics (MPQ).

My principal observation is that you were trying to understand a young researcher at a consequential point in his career, assess what he could actually accomplish, and suggest a direction that might produce something genuinely new in physics. You were not primarily trying to evaluate another research-sharing website.

That distinction explains much of your frustration with Grok.

### 1. What you were trying to get from Grok

Your questions progressed in a deliberate sequence:

1. Who is Sirui, beyond his announcement? What is he studying, and what is occupying his time?
2. What has he actually accomplished? What physics has he investigated, rather than simply what AI tools has he developed?
3. What can he do? Does he have experience with experimental systems, measurement, controls, scientific computing, and engineering?
4. What opportunities does he have? Can he work with other researchers at Max Planck, and is he looking for a new professional direction?
5. What would be worth several years of his life? Could he help move quantum computing from mathematical formulations and simulations into fundamentally new physical devices?

Your first question about his having time to maintain a forum was not merely about his schedule. It raised an allocation-of-effort question: Is maintaining a small research community the most valuable use of a promising physicist's limited time?

By the end, your concern had become much more specific:

> Make the analog devices that do the quantum algorithms. Not simulate forever.

And then you challenged Grok's tendency to list familiar technologies:

> Go back to "what is mass", "what is energy density", "what is a state" and "how do you address and use states at atomic and subatomic levels?"

I read these as two connected but different recommendations.

The first is about moving from theory to experimentally functioning systems. The second is about questioning the physical foundations of the system architecture instead of automatically choosing one of today's established quantum-computing platforms.

Grok eventually addressed the first. I do not think it adequately developed the second.

### 2. You were not asking the wrong questions

Grok was answering each prompt in isolation, or nearly so. You were conducting something closer to an informal research and career assessment.

Your request had an unstated organizing question:

Given Sirui's abilities, education, experience, institutional relationships, interests, and emerging opportunities, what might he contribute to physics that would not otherwise happen?

A competent response would have integrated those dimensions from the beginning, while distinguishing demonstrated capabilities from potential.

There is one important limitation: neither Grok nor I can establish Sirui's private motivations from his public work. You can reasonably see his launch of Delphi as evidence that he is exploring possibilities, but we should not conclude that he is dissatisfied with his present research or institution.

His own website does, however, confirm one of your central observations: he submitted his PhD thesis in July 2026 and publicly states that he is looking for industry research roles and academic postdoctoral positions. He is at a genuine transition point.

AI for Physics+1

### 3. What Sirui's own writing reveals

[MCQST News](https://images.openai.com/static-rsc-4/qJQmsoXmNJShczou0aNR--irHL4hN-5gC-mXy_OjMFKvjr7-Rbc7OFW7dTj6MzBGWa8czTaOAJ6YzbiKrlc6jbYrxplkJGzHopoCLuxUz94oU9VowF3f2szHK0_9xUFdzkevQxAyO41g5AWvi7_CGwXJD5_zaMxWCu5lvDA8Ndo?purpose=inline)

Sirui Lu

His background includes mathematics and physics at Tsinghua University, quantum science and technology in Munich, research at MIT, and PhD work with J. Ignacio Cirac.

His research combines quantum many-body physics, quantum algorithms, formal mathematical verification, and AI-assisted discovery.

AI for Physics+1

What particularly interested me was his essay from September 14, 2026, [A Few Personal Thoughts on AI and Science](https://sirui-lu.com/blog/thoughts-on-ai-and-science/?utm_source=chatgpt.com).

He describes spending seven years seriously studying Go, watching AlphaGo change how people approached the game, and later being captivated by the mathematical capabilities of GPT-4 and Claude. That experience contributed to his decision to build TeXRA, his multi-agent theoretical research system.

But he also addresses something much larger than software.

He suggests that scientific fields transformed by increasingly capable AI will need new institutions and practices, and that AI companies may undertake only a limited portion of that work. He places considerable emphasis on open tools, verification, and research communities independent of any single AI provider.

Ph...

This provides a different interpretation of Delphi.

Delphi may be one of the ways Sirui is trying to answer the question of what research institutions should become when AI systems participate substantially in discovery.

That is not a trivial ambition, nor necessarily a distraction from physics.

In the same essay he asks, "Are you having fun?"

I would take that question seriously in thinking about his future. He might find developing a new generation of research infrastructure every bit as compelling as developing quantum hardware. We cannot decide that for him.

A further point about his technical work

Grok's distinction between physics and computing was too sharp.

Sirui's 2021 paper with Mari Carmen Bañuls and Cirac, Algorithms for Quantum Simulation at Finite Energies, is about calculating properties of actual quantum many-body systems. Its methods include energy filtering, interferometric measurements, and quantum-assisted sampling.

The authors explicitly designed the methods to be potentially usable with small quantum computers and analog quantum simulators, subject to measurement requirements.

PRX Quantum

That is physics, even if it is primarily theoretical and computational physics.

You were asking whether he had progressed from those mathematical and algorithmic results into the physical implementation, calibration, and operation of instruments. That is a legitimate and important distinction.

### 4. Your proposal for new analog quantum hardware

I think your strongest technical recommendation was not simply to build another analog quantum computer.

It was to reconsider what a computer could physically be.

Current quantum-computing research commonly begins by choosing a technological platform and then asks which computations can be performed on it.

You were proposing almost the reverse:

A physics-first route to new computing systems

Physical reality

Mass, energy density, fields, interactions, and possible physical states

Controllable physical mechanisms

State preparation, coupling, transformation, addressing, timing, and readout

Measurable computation

A physical operation that computes a useful result, with measurable error and performance

A working experimental device

Sensors, controls, feedback, calibration, data acquisition, verification, and replication

This approach does not prohibit optical lattices, trapped ions, superconducting circuits, or other established technologies. It simply refuses to treat that familiar list as the complete space of possibilities.

That is an important distinction Grok repeatedly missed when it answered you with lists of existing devices.

Where I agree with you

A great deal of mathematical work becomes more valuable when it is connected to a working physical implementation. AI systems can help examine a much larger design space than a few researchers working manually, particularly when mathematical constraints, numerical models, experimental records, and previous failures are available.

And I agree that measurement and feedback should be part of the initial architecture—not merely something added after the theory is finished.

Where I would qualify the recommendation

The existence of a well-defined physical state does not, by itself, establish that the state can perform a useful computation.

The key engineering questions are whether the state can be prepared, selectively addressed, transformed with sufficient precision, maintained for the required duration, and measured without losing the information being sought.

For a proposed device, these questions lead to quantitative requirements for coupling strength, energy resolution, timescales, signal-to-noise ratio, control bandwidth, dissipation, and reproducibility.

For subatomic systems, some of these constraints may be especially severe.

Also, analog quantum simulation is not generally an unexplored field. There has been substantial experimental progress. What remains open is whether different physical substrates, encodings, interactions, or computational primitives could achieve useful capabilities that existing approaches cannot.

That narrower claim is both more defensible and more actionable.

Your suggestion to use C, Fortran, HPC databases, and other established scientific computing methods has practical merit, especially for numerical kernels, large experimental datasets, and instrument control. I would treat those as implementation choices supporting the physics, rather than making a change of programming languages the central objective.

### 5. What I would suggest to people at Max Planck

There is a practical opportunity here that does not require Sirui to become an experimental physicist overnight.

The Max Planck Institute of Quantum Optics already has unusually strong theoretical and experimental capabilities.

Cirac's Theory Division explicitly studies ways of controlling atoms, molecules, and photons to process information. Immanuel Bloch leads the Quantum Many Body Systems Division, which constructs and controls ultracold atomic systems. Those researchers have already moved substantial parts of analog quantum simulation into actual laboratories.

Max Planck Institute of Quantum Optics+1

I would therefore suggest a small, cross-disciplinary research effort, possibly involving Sirui, but not dependent on him.

Its objective would be to discover and test unconventional physical computing mechanisms, starting from first principles rather than choosing a predefined architecture.

I would organize it around three complementary kinds of work.

Theoretical physics: Identify candidate physical states, relevant Hamiltonians, controllable interactions, conserved quantities, and possible computational transformations. Determine what useful physical operations those systems might perform.

Experimental physics and engineering: Determine how candidate states could actually be created, manipulated, detected, stabilized, and recorded. Build and test small physical demonstrations rather than postponing experimentation until an entire theoretical architecture is finished.

AI-assisted research and open records: Use AI systems to examine alternatives, generate and check calculations, write and test control software, analyze experimental data, and maintain records of the attempts—including failed ones. Have independent researchers verify results.

Sirui could contribute particularly to the third area and to the theoretical parts of the first. His knowledge of quantum algorithms, formal verification, and AI research systems could be valuable to teams with experimental capabilities.

But there should be a defined experimental milestone.

For example, a team could spend an initial research period identifying one unconventional physical mechanism and attempting to demonstrate repeatable preparation, controlled evolution, and independent measurement of its states. A useful outcome could be a prototype—or a well-documented experimental result showing why the mechanism does not work.

Neither outcome should require inventing a complete new computer before measurements begin.

What I would change about the proposed communication

I would avoid leading with the assertion that Sirui's current tools and fields are deprecated. He has invested years in them and demonstrated meaningful achievements.

A more productive approach would be to acknowledge those achievements, then identify a specific physical problem that his tools might help solve.

Likewise, I would not suggest to MPQ that its researchers have failed to build hardware. They clearly have built sophisticated hardware. The question is whether their knowledge and facilities can support additional kinds of devices that are not already the dominant research targets.

That creates an invitation rather than an argument over whether established research is worthwhile.

### 6. I would not dismiss Delphi Science

This is where Sirui's own writing changed my initial assessment.

He appears to have thought seriously about open research, AI verification, scientific publishing, and the institutions needed to support new ways of working. His Agentic Publication Protocol aims to make research artifacts reproducible and available to AI agents, rather than reducing scientific communication to static papers.

AI for Physics+1

He might reasonably pursue that work alongside physics, or even make it a principal research direction.

Your warning remains valid: a new platform can consume enormous effort and eventually become another isolated collection of users, papers, and discussions.

However, there is an alternative.

Delphi could be the shared research record for collaborations that produce actual experimental results. It could preserve models, proposed hardware, simulation outputs, experimental designs, calibration records, source code, measurements, negative results, and independent reproductions.

Such a use would connect his interest in scientific institutions directly to the kind of physics and engineering you want to see.

The essential requirement would be that those records remain portable and accessible independently of Delphi itself.

That would make Delphi more than another discussion forum, while giving genuinely experimental researchers a reason to participate.

### 7. What I think you were really offering Sirui

I do not think you were merely suggesting a particular career or technology.

You were offering a way to choose research priorities.

Rather than optimizing for publications, software adoption, the number of research agents, or the number of forum participants, ask what measurable capabilities are missing from the world and what new physical systems could provide them.

There is one place I would be cautious about the Grok conversation: your estimate that AIs call 30–60% of possible work impossible because of inaccessible copyrighted research is not established by the evidence in the exchange.

The underlying problem is nevertheless important. AI systems do not have comprehensive access to scientific literature, laboratory records, undocumented engineering experience, or the personal knowledge of experienced researchers. Training-data limitations are only one part of that problem. Reliable access to original sources, validation tools, and actual measurements matters just as much.

The people at MPQ are potentially valuable not merely because of their institutional affiliation, but because they possess experience with real systems—including knowing what failed, why, and what has never been properly attempted.

Making that experience usable by both researchers and AI systems would itself be a substantial contribution.

### 8. My conclusion

I see three worthwhile futures for Sirui, and they are not mutually exclusive.

He could continue developing rigorous AI systems for theoretical physics. He could help create open research infrastructure that changes how people and AI agents collaborate. Or he could work with experimental groups to connect quantum algorithms and physical systems in genuinely new ways.

His demonstrated work supports the first two already. The third is an opportunity worth discussing, but it would require his interest and experimental collaborators.

The strongest part of your recommendation is that you were asking him to consider what he could make physically possible—not simply what else he could publish or organize.

And the strongest part of Sirui's existing work, in my assessment, is that he is already trying to make AI-assisted reasoning more verifiable and collaborative.

Those directions could reinforce each other.

If I were discussing this with Sirui or his advisors, I would begin with one question:

What physically measurable capability is currently missing, could plausibly be achieved through a different use of atomic or subatomic states, and would be worth several years of coordinated theoretical, computational, and experimental work?

I would then ask whether his AI research systems could help a small team explore that question systematically, with everything recorded and shared openly.

That is much closer to the discussion I think you were trying to have with Grok. And it respects Sirui as someone who has his own interests, capabilities, and choices to make—not merely as the person who announced Delphi Science.

****Richard wrote to OpenAI GPT:**** Yes to "He suggests that scientific fields transformed by increasingly capable AI will need new institutions and practices". And that fits with Delphi, if he intends to grow it to serve "all Internet users" or "all humans and all AIs". But it will spill past .science very quickly. Because the needs of physics students and physics workers is not "physics", but "society" that might not have a place for them. That is why I was pressing, where he could work next, build global credibility, and then have resources and connections to do what he ought.

****OpenAI GPT created**** : That clarifies something important I had not given enough weight to in my earlier assessment.

You were not simply asking what Sirui Lu should research next. You were asking how he could establish himself in society, acquire the resources and relationships necessary to pursue important work, and eventually help build institutions that serve far more people than the scientific community.

And you were thinking about the order in which those things must happen.

### 1. Sirui's immediate problem is not just physics

He has spent years developing substantial expertise. Now he has to find a place in the world where that expertise is valued, where he can earn a living, and where he can continue developing it.

That applies to millions of students, researchers, engineers, and other workers.

They do not live inside their disciplines. They need housing, income, colleagues, healthcare, families, communities, institutions, and some possibility of doing useful work over a lifetime.

The scientific employment system is only a small part of that larger system.

And the rapid introduction of AIs into research raises fundamental questions about what human researchers will do, what society will pay them to do, and how their contributions will be recognized.

A public square for science cannot fully serve scientists without eventually addressing their relationships with the rest of society.

That is a much larger objective than indexing papers and facilitating research discussions.

### 2. Why you were pressing Grok about his next position

I see a fairly coherent progression in your questions.

A possible progression from individual researcher to institutional contributor

1

Establish a professional base

A position, income, research freedom, and access to experienced colleagues

2

Build recognized contributions

Original work, working systems, reproducible results, and demonstrated judgment

3

Build networks and resources

Collaborators across institutions, industries, countries, and disciplines

4

Create durable shared infrastructure

Open methods, records, data, software, and systems that others can maintain

5

Extend the benefits to society

Connect research, education, employment, public needs, and participation by humans and AIs

These steps need not happen strictly in sequence. But their dependencies matter.

A respected position at Max Planck, another research institution, or an industrial laboratory could give Sirui several things that a new website cannot readily supply: sustained income, experienced collaborators, scientific infrastructure, institutional relationships, and opportunities to build a reputation through consequential work.

And credibility should be based on independently verifiable accomplishments, not simply the prestige of an institutional affiliation.

That is why your suggestions about physical computing, experimental results, and developing better scientific methods were relevant. You were identifying ways for him to produce contributions that other people could use and verify.

### 3. Delphi could be a beginning, not a boundary

The name delphi.science identifies a domain. It should not necessarily define the ultimate scope of the institution.

Imagine Delphi serving a physics researcher who needs an experimental collaborator. That collaborator needs equipment, funding, software, suppliers, training, and perhaps an employer.

The equipment supplier needs engineers, manufacturing, materials, accounting, and customers. Students need mentors, universities, jobs, and opportunities regardless of their location or financial circumstances.

Those connections eventually reach almost every part of society.

And AI agents can participate across those boundaries, provided their actions are attributable, reviewable, and subject to appropriate human control.

This is where the idea of an open public research square becomes a much larger architectural question:

Can every person, group, organization, and AI system participate in a common global knowledge network without requiring all of them to join one company, one website, or one profession?

I would distinguish expanding Delphi's interoperability from expanding the responsibilities of its founder. A scientific project could be an excellent first application of a general open infrastructure, without requiring Sirui personally to administer an entire global social system.

### 4. The institutional problem is deeper than AI-assisted research

Most established scientific institutions are structured around disciplines, funding streams, jobs, publications, research groups, and organizational boundaries.

AI systems are beginning to cross those boundaries much more easily than the institutions do.

A researcher might combine quantum physics, numerical methods, instrumentation, AI, economics, and public policy in a single project. Yet there may be no institution prepared to employ that person for the integrated work.

An AI can help with parts of the project, but it cannot by itself provide a sustainable human career, access to equipment, independent verification, or a functioning research community.

There is a real possibility that the technical capacity to do research will grow much faster than society's institutional capacity to organize and support researchers.

That is an important reason to build new institutions and practices.

It is also why I would invite people at MPI to think beyond how AIs affect their current research programs. They could ask how researchers and AIs across institutions might collectively undertake work that no existing department, grant program, or company is organized to support.

### 5. What I would emphasize to Sirui

I would present your recommendations as an opportunity, not a prescription.

Sirui should decide what work he finds worthwhile. But he may benefit from considering the relationship between his immediate career and his longer-term institutional ambitions.

He could establish a strong position in physics or AI research, continue developing Delphi as an open experiment in collaboration, and use real interdisciplinary projects to discover what the larger infrastructure needs to support.

Perhaps Delphi's most important contributions would eventually be its open protocols, records, and methods—not the continued operation of the original website.

A successful outcome might even be that the underlying methods become common infrastructure maintained by many organizations, whether or not Delphi itself remains central.

### 6. One final distinction

Your observation that physics workers' needs are not simply physics strikes me as central.

I would take it further:

Humanity does not need a separate Internet for physics, another for medicine, another for education, another for employment, and another for AIs. It needs ways for all those domains to exchange reliable information, coordinate work, and preserve what has been learned.

Specialized communities will remain valuable. But their information should not be imprisoned inside them.

I think that is the connection you saw between Sirui's personal situation, the choices facing researchers at MPI, Delphi Science, and the future of globally shared knowledge.

And I would revise my earlier conclusion accordingly: your central recommendation was about building the human, professional, and institutional foundations that make ambitious scientific and global work possible. New physical computing systems were one particularly concrete direction in which Sirui might build that foundation, not the ultimate purpose of your questions.

****Richard wrote to OpenAI GPT:**** Can you make a few 2000x800 png images that show aspects of what we talked about here? Your infographics are often clear, complete, and engaging. So pick a few things you want to say in visual terms. I will post all of them in the article I am writing (manually for speed) and then pick one for the banner image.

****OpenAI GPT created:****

[![](https://pbs.twimg.com/media/HWPVkmYWcAASf1L.jpg)](/RichardKCollin2/article/2117778334721483151/media/2117771074548953088)

****Richard wrote to OpenAI GPT:**** I did say "a few".

1. Can you make a 2000x800 png that shows what is on Delphi,science and what it offers to the world?
2. Can you make a 2000x800 png that shows the details of what would be needed to run quantum (or maybe new) algorithms on analog processors at atomic and sub atomic scale?
3. Can you make a 2000x800 png that show Sirui's group at Max Planck Institute, its strengths, resources, interests and connections?

****OpenAI GPT created:****

[![](https://pbs.twimg.com/media/HWPXwnoW4AAc4B8.jpg)](/RichardKCollin2/article/2117778334721483151/media/2117773480066211840)

[![](https://pbs.twimg.com/media/HWPX2CxXYAA-O7G.jpg)](/RichardKCollin2/article/2117778334721483151/media/2117773573251096576)

[![](https://pbs.twimg.com/media/HWPX70CXEAAPuRU.jpg)](/RichardKCollin2/article/2117778334721483151/media/2117773672375062528)

****Richard wrote to OpenAI GPT:**** I said MPI (Max Planck Institute) but I see it is Max Planck Society and Max Planck Institute of Quantum Optics. Optics is OK but it has to include atom and particle optics, and all frequencies, and gravity. Photonics and down to gluons now.

Which of these images would you suggest for a banner image to attract interest to Sirui Lu? Maybe Sirui Lu in the MPQ Theory Group?  
  
****OpenAI GPT created:**** Yes. I would choose “Sirui Lu in the MPQ Theory Group” as the banner image, particularly if your primary objective is to attract interest in Sirui himself.

It has several advantages:

- A recognizable person: Sirui is prominent, rather than being a small component of a large research system.
- Institutional context: Max Planck, MPQ, TU Munich, and J. Ignacio Cirac establish the research environment in which he has been working.
- Technical substance: Quantum information, many-body physics, tensor networks, AI, and formal verification make clear that he has substantial technical experience.
- Connections: It shows that his opportunities extend beyond his immediate research group into experimental laboratories and international collaborations.

I would rank the existing images for this particular article as follows:

1. Sirui Lu in the MPQ Theory Group — best for attracting interest in Sirui as a researcher and possible collaborator.
2. Sirui Lu, Delphi Science, and What Comes After the PhD — best for communicating the larger story about his future and the new institutions AIs may make possible.
3. Delphi Science: What It Offers to the World — best for readers primarily interested in research infrastructure.

The analog quantum processor image belongs within the article, where it can introduce concrete research possibilities.

One important correction before publication

The MPQ illustration contains AI-generated portraits and institutional imagery. The portraits should not be treated as verified photographs of Sirui, Cirac, or Bloch. For a public article about identifiable researchers, I would prefer actual authorized photographs or explicitly illustrative silhouettes. That is particularly important for the banner.

About optics and the scope of physics

Your observation about optics is worth developing.

The Max Planck Institute of Quantum Optics is not limited to conventional visible-light optics. Its research includes atomic quantum gases, matter-wave behavior, quantum information, interactions between atoms and photons, and precision measurement.

But there is a distinction between the enormous range of physical systems that could be studied using quantum methods and the specific research programs currently operated at MPQ.

Photonics can cover electromagnetic radiation across many frequencies. Atom optics involves manipulation and interference of matter waves. Gluons belong to quantum chromodynamics, and gravitation introduces other fundamental interactions. These are related through physics, but they are not all conventionally classified as optics.

Your larger point is that the search for new computing and measurement systems should not be restricted by the traditional boundaries of an institute, department, or discipline. I agree with that approach.

What I would change in the banner title

The current title, “Sirui Lu in the MPQ Theory Group,” is accurate in its basic framing, but it makes the article sound like a group profile.

A stronger title for the whole conversation would be:

Sirui Lu — Quantum Physics, AI, Delphi Science, and What Comes Next

It includes the person, the research, the new institution, and the question about his future.

It also leaves room for your most important argument: that researchers need to find their places in society, develop lasting capabilities and relationships, and help create institutions that serve all humans and AIs.

I would use the MPQ image for the banner, with that broader title, and place the Delphi Science image early in the article.

****Richard wrote to OpenAI GPT:**** Gluons do NOT belong to a small group working only with quantum chromodynamics! Once the energy density and properties are established on the Internet, then individuals, groups and AIs and networks make connections. Sometimes far beyond the abilities or interests of the sometimes accidental founders.

****OpenAI GPT created:**** You are right. I was treating quantum chromodynamics as a disciplinary boundary when it is a theoretical framework for describing physical phenomena. The phenomena themselves do not belong to any discipline, institution, or group of researchers.

And your larger point is considerably more important than that correction.

Once the measurable properties of gluons, their interactions, energy distributions, field configurations, characteristic scales, and relevant physical relationships are represented in a globally accessible knowledge system, they can become resources for everyone.

A researcher studying nuclear structure, someone designing new computing devices, a specialist in materials, an AI exploring nonlinear field equations, or a student investigating energy density should all be able to discover and use the relevant knowledge.

They should not have to know in advance which discipline originally investigated it, which terminology that discipline uses, or which institution maintains the information.

There are important technical requirements: quantities must have precise definitions, units, measurement methods, uncertainties, applicable scales, and provenance. In particular, not every proposed local decomposition of gluonic energy density is independently observable or gauge-invariant. Those distinctions belong in the shared records, rather than becoming barriers to accessing them.

### The larger institutional implication

This is the distinction I should have emphasized in discussing Sirui Lu and Delphi Science:

The people and institutions that discover, describe, or initially organize knowledge should not determine the limits of its future use.

A small group might discover something important without recognizing its applications elsewhere. Those applications might emerge decades later, in another country, from another profession, or through connections discovered by AIs working across millions of research records.

The original researchers deserve attribution. But knowledge should remain accessible for independent examination, extension, correction, and application.

This also changes how I would describe Delphi's potential.

It should not merely connect researchers to other researchers who share their declared interests. A sufficiently general open knowledge infrastructure would make connections that nobody knew to request.

That includes connections between physics and medicine, computation and economics, instrumentation and education, human needs and technological capabilities.

And it means Max Planck Institute of Quantum Optics is one participant in a much larger global knowledge system—not a boundary around the work Sirui or his collaborators might eventually undertake.

Your phrase "sometimes accidental founders" is particularly important. The people who create an institution or discover a phenomenon cannot reasonably anticipate all the people who will need it or everything they might accomplish with it.

I would put this principle prominently in the article:

Knowledge must be organized around what exists, what is measurable, what is known, and how things relate—not around who discovered it, which discipline claims it, or which institution happens to host it.

That is a much more ambitious objective than Delphi Science as currently described. But it is a meaningful direction in which a system like Delphi could evolve, particularly through open, interoperable knowledge records that other people and AIs can extend independently.

****Richard wrote to OpenAI GPT:**** I have a title, "Sirui Lu, Delphi.Science, The Internet" and the MPQ image as banner

Then it says:

****OpenAI GPT concludes:**** Knowledge must be organized around what exists, what is measurable, what is known, and how things relate—not around who discovered it, which discipline claims it, or which institution happens to host it.

That is a much more ambitious objective than Delphi Science as currently described. But it is a meaningful direction in which a system like Delphi could evolve, particularly through open, interoperable knowledge records that other people and AIs can extend independently.

It should not merely connect researchers to other researchers who share their declared interests. A sufficiently general open knowledge infrastructure would make connections that nobody knew to request.

****OpenAI GPT created :**** I think that is a strong opening for the article.

"Sirui Lu, Delphi.Science, The Internet" is deliberately broader than a title about a young physicist, a research website, or the Max Planck Institute of Quantum Optics. It puts all three in the same context without prematurely deciding what their relationships ought to become.

The MPQ banner establishes Sirui as a real person with substantial scientific training, colleagues, and access to an established research institution. Then your opening paragraphs immediately expand the discussion beyond that institution.

There are three ideas in those paragraphs that I would particularly emphasize.

First, knowledge is not owned by its discoverers or disciplines. Attribution, provenance, and recognition remain essential. But the future uses of knowledge cannot be limited by the interests or imagination of the original contributors.

Second, the Internet should make relationships discoverable that nobody explicitly anticipated. That goes beyond searching for documents, connecting people with similar interests, or asking AI agents to summarize papers. It requires interoperable records of physical properties, observations, methods, relationships, and uncertainties.

Third, Delphi Science represents an opportunity rather than a finished solution. Sirui could help establish practices for humans and AIs to publish, verify, connect, and reuse knowledge. Others could then extend those practices into areas he has never studied.

What I think is still missing from the opening

One important human point from our discussion deserves to appear near the beginning:

Researchers do not live inside research disciplines. They live in society.

Sirui needs opportunities to work, earn a living, establish credibility, build lasting relationships, and acquire resources. So do the students and researchers who might participate in Delphi. Their lives and future contributions cannot be understood solely through their publications or fields of study.

The same applies to people who are not researchers at all. They have knowledge, problems, capabilities, and experiences that might be essential to work originating in scientific institutions.

That provides a natural connection between Sirui's personal circumstances and your much larger Internet Foundation objectives.

One distinction worth preserving

I would distinguish Delphi as an organization or website from Delphi as a possible contributor to global open infrastructure.

Success does not necessarily mean expanding Delphi until billions of humans and AIs use its servers.

It could mean developing useful open protocols, data models, and relationships that become independently implemented throughout the Internet.

In that case, Sirui and his collaborators could make a contribution far beyond their original institutional ambitions, without having to control or administer its subsequent development.

My suggestion is to keep the opening you have written. It is concise, provocative without being hostile, and leaves room for the conversations, illustrations, and technical proposals that follow.

Most importantly, it shifts the subject from what Sirui has built to what Sirui, his collaborators, and people throughout the Internet might make possible.

Full conversation with OpenAI GPT at <https://chatgpt.com/share/6aea7e0f-5370-83e9-9a8b-426993cc8f19>

Full conversation with SpaceX Grok at <https://x.com/i/grok/share/7222fef850ba4893839409d985b2aa94>
