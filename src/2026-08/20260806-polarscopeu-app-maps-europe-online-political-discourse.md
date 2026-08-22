# PolarScopEU: The App That Maps Europe's Online Political Discourse
**Source**: https://cordis.europa.eu/article/id/466739-the-app-that-maps-europe-s-online-political-discourse
**Date**: 2026-08-06
**Author**: CORDIS, European Commission
**Keywords**: PolarScopEU, political discourse mapping, EU, online polarization, text analysis, Bluesky, MAPLE, sentiment analysis, European Research Council, computational social science

## Elevator pitch
An ERC-funded project called PolarScopEU has developed an app that maps the political and media environment across EU countries by analyzing social media content, detecting topics and sentiment, and visualizing polarization patterns in online political discourse.

## Takeaways
- PolarScopEU, funded by the European Research Council and hosted at the Institute of Social Sciences in Lisbon, has developed a breakthrough app for mapping online political discourse across EU countries
- Two main analytical strands: social media analysis (Bluesky content producing Bias Plots and similarity tables) and EU politicisation analysis using MAPLE's coding frameworks
- Topic detection uses a Polexlab language model fine-tuned to identify 21 policy topics from the Comparative Agendas Project
- Sentiment detection employs a multilingual cardiffnlp/twitter-xlm-roberta-base-sentiment model
- EU references identified through MAPLE's multilingual rule-based detector supporting seven languages
- The app provides more detailed EU politicisation analysis than existing studies, including identifying which EU dimension is being discussed (membership, constitutional structure, EU policy)
- Already adopted for current research, including analysis of Portuguese media articles about the EU

## Synthesis
Published on CORDIS (the European Commission's research results platform) on August 6, 2026, this article describes PolarScopEU, a project funded by the European Research Council that has developed a novel application for mapping and analyzing online political discourse across European Union countries. The project is coordinated by Marina Costa Lobo at the Institute of Social Sciences at the University of Lisbon.

The project addresses a pressing concern: the internet's impact on EU governance and democracy. While online platforms facilitate public service provision and political engagement, they also enable ideological polarization, echo chambers, and misinformation. PolarScopEU aims to improve the quality of online political communication by providing tools to monitor and analyze what political actors and their followers say online.

The app's technical architecture involves two main analytical strands. The first analyzes social media content from Bluesky, producing "Bias Plots" and similarity tables. Posts are collected from specific handles and networks, then fed into automated text analysis tools. Topic detection relies on a Polexlab language model fine-tuned to identify 21 policy topics from the Comparative Agendas Project. Sentiment detection uses a multilingual cardiffnlp/twitter-xlm-roberta-base-sentiment model. EU references are identified through MAPLE's multilingual rule-based detector based on keyword and abbreviation searches, supporting seven languages.

The second strand provides EU politicisation analysis using MAPLE's coding frameworks. PolarScopEU created an automated coding framework combining rule-based EU keyword detection with fine-tuned classifiers that identify when the EU is central to text, assigning scores related to issues like conflict between actors. As researcher Tiago Casal da Silva explains, this offers more detailed analysis than existing studies, including identifying which EU dimension is being discussed — membership, constitutional structure, or EU policy.

The project adapted its approach after changes to Twitter (now X) and the rise of machine/deep learning technologies altered the social media landscape. The system works well as a descriptive research tool, though testing highlighted the importance of careful interpretation and adequate computing infrastructure. The app is freely available online, and the team plans to extend language support, update models, and apply the tools to new case studies and comparative settings.