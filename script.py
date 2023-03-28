from rich.console import Console
from rich.tree import Tree

console = Console(record=True, width=120)

tree = Tree(
    "🐍 [link=https://cmeyer.fr/]Corentin Meyer", guide_style="bold bright_black"
)

main_projects = tree.add("📦 Main Projects", guide_style="bright_black")
main_projects.add(
    "[bold link=https://github.com/lambda-science/MyoQuant]myoquant🔬[/]          - [bright_black]automatically quantify pathological features in muscle fiber histology images"
)
main_projects.add(
    "[bold link=https://github.com/lambda-science/NLMyo]nlmyo🔧[/]          - [bright_black]a toolbox built to leverage the power of Large Language Models (llms) to exploit histology text reports."
)
main_projects.add(
    "[bold link=https://github.com/lambda-science/IMPatienT]impatient🗂️[/]          - [bright_black]web application to digitize, process and explore multimodal patient data"
)
main_projects.add(
    "[bold link=https://github.com/lambda-science/MyoQuant-Streamlit]myoquant-streamlit[/]  - [bright_black]web demo of myoquant using streamlit"
)
main_projects.add(
    "[bold link=https://github.com/lambda-science/STREAMLINE]streamline[/]          - [bright_black]fork of the Streamline autoML pipeline for multiclass classification"
)
main_projects.add(
    "[bold link=https://github.com/lambda-science/stage-thompson]primate proteins[/]    - [bright_black]analysis of gene prediction errors in the proteome of 11 primates"
)
main_projects.add(
    "[bold link=https://github.com/lambda-science/droso-analysis]drosophila proteins[/] - [bright_black]analysis of gene prediction errors in the proteome of drosophilas"
)

wip_tree = tree.add("🛠️ Work In Progess", guide_style="bright_black")
wip_tree.add(
    "[bold link=https://github.com/lambda-science/thesis]thesis[/]          - [bright_black]my thesis in writing"
)
wip_tree.add(
    "[bold link=https://github.com/lambda-science/PredEx]predex[/]              - [bright_black]train and visualize learning classier systems (lcs) for explainable models"
)
wip_tree.add(
    "[bold link=https://github.com/lambda-science/dnd-qa]dnd-qa🗡️[/]               - [bright_black]chatbot to answer questions about dungeons and dragons spells"
)

web_tree = tree.add("🔗 My Websites", guide_style="bright_black")
web_tree.add(
    "[bold link=https://cmeyer.fr]cmeyer.fr[/]           - [bright_black]personal linktree"
)
web_tree.add(
    "[bold link=https://cmeyer.fr/blog/]cmeyer.fr/blog[/]      - [bright_black]personal blog"
)
web_tree.add(
    "[bold link=https://impatient.lbgi.fr]impatient.lbgi.fr[/]   - [bright_black]impatient web demo"
)
web_tree.add(
    "[bold link=https://lbgi.fr/MyoQuant]lbgi.fr/MyoQuant[/]    - [bright_black]myoquant web demo"
)
web_tree.add(
    "[bold link=https://lbgi.fr/MyoQuant]lbgi.fr/NLMyo[/]    - [bright_black]nlmyo web demo"
)
web_tree.add(
    "[bold link=https://status.cmeyer.fr/]status.cmeyer.fr[/]    - [bright_black]website status page"
)
online_tree = tree.add("📚 Teaching and Internships", guide_style="bright_black")
online_tree.add(
    "[bold link=https://github.com/lambda-science/machine-learning-introduction]ml intro lecture[/]    - [bright_black]1st machine-learning introduction lecture at the biotechnology school of strasbourg (esbs)"
)
online_tree.add(
    "[bold link=https://github.com/lambda-science/Machine-Learning-TD-ESBS]ml 1st practical[/]    - [bright_black]1st machine-learning practical at the esbs"
)
online_tree.add(
    "[bold link=https://github.com/lambda-science/ML-TD-ESBS-2]ml 2nd practical[/]    - [bright_black]2nd machine-learning practical at the esbs"
)
online_tree.add(
    "[bold link=https://github.com/lambda-science/stage-afaf]afaf intern[/]         - [bright_black]code for afaf internship"
)
online_tree.add(
    "[bold link=https://github.com/lambda-science/stage-ines-jeremy]ines intern[/]         - [bright_black]code for ines and jeremy internship"
)

old_tree = tree.add("⚰️ Dead and old projects", guide_style="bright_black")
old_tree.add(
    "[bold link=https://github.com/lambda-science/pcr-primer-finder]pcr-primer-finer[/]    - [bright_black]tool to find optimal primers for pcr"
)
old_tree.add(
    "[bold link=https://github.com/lambda-science/genetics]genetics[/]            - [bright_black]a web application for genetic sequence analysis"
)
old_tree.add(
    "[bold link=https://github.com/lambda-science/genetics-GUI]genetics-gui[/]        - [bright_black]a gui app. for genetic sequence analysis"
)
old_tree.add(
    "[bold link=https://github.com/lambda-science/stage-merienne]huntington-rnaseq[/]   - [bright_black]hungtington disease RNA-seq analysis internship"
)
old_tree.add(
    "[bold link=https://github.com/lambda-science/Hara-twitterbot]twitter-bot[/]         - [bright_black]small twitter bot to tweet pictures of cute shibas"
)

console.print(tree)
console.print("")
console.print(
    "[green]Follow me on twitter [bold link=https://twitter.com/corentinm_py]@corentinm_py[/] and on my website [bold link=https://cmeyer.fr]cmeyer.fr[/]"
)

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("tree.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
