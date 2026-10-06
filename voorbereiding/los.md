# Context engineering

Ik zou daarom expliciet een hoofdstuk toevoegen rond:

PRD's schrijven voor agents
Architecture Decision Records (ADR)
Agent Rules (.clinerules)
Specification Driven Development
Context Compression
Multi-agent workflows

Want in 2026 is dit wellicht waardevoller dan leren hoe Cline precies geïnstalleerd wordt.

Mijn ervaring is dat developers die goed zijn in:

requirements
architectuur
testing
reviewen

veel sneller productief worden met agentic coding dan developers die vooral sterk zijn in syntax en implementatiedetails. Dat is een mooie rode draad voor de volledige opleiding.


---
# principles
Principles: https://agentic-coding.github.io/


---

# mistakes to avoid

1/ One mega-chat for everything. Mixed topics bury the context and Claude loses the plot. Spin up a Project per recurring task with its own instructions ready to go.

2/ Always running the same model. Defaulting to one model burns your limits. Haiku for speed, Sonnet for daily work, Opus for the heavy stuff.

3/ Re-uploading the same files every time. Drop your core docs into Project knowledge once, then call them by name.

4/ One giant rambling prompt. A wall of text makes Claude guess. Ask it to interview you first so it builds on real context, not assumptions.

5/ Zero examples. Claude learns from what good looks like. Show it a strong output next to a weak one.

6/ Claude Code for everything. It's built for shipping. Save it for when you actually need to build something.

7/ Cowork for planning. Cowork executes. Think and explore in Chat first, then hand off the finished task.

8/ Skipping Connectors. Pasting context from Gmail or Notion every time is a tax on every prompt. Connect them once.

9/ Short vague prompts. Less input, worse output. Spell out what you need, who it's for, the format and what to skip.

10/ No "about me" file. Without context on you, Claude defaults to generic. Have it interview you and build one master .md with your role and preferences.

11/ Rebuilding the same task daily. Retyping yesterday's prompt is wasted effort. Turn anything you repeat into a Skill: QA checks, drafts, research summaries.

12/ Five asks in one prompt. Cram five and you get five half-answers. Break big tasks into steps and batch only the tightly related ones.

The Takeaway:
It almost always comes down to context.
Give Claude the right environment, the right instructions, and the right boundaries, and the output gets much better.

The bigger problem?
Those mistakes burn through your usage limit fast.
Claude ends up doing extra work, rewriting, retrying, and cleaning up tasks that could have been done properly the first time.

---

- inclusief setup MCP server - https://dev.to/thenomadevel/how-i-got-an-ai-agent-to-read-and-reply-on-whatsapp-automatically-am1
- https://agentskills.io/home
- https://www.youtube.com/watch?v=oblaHqULUHk
- setup gemini open AI API key testen in VS code
- Sandboxing in docker container env