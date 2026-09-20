# AI Skills Collection · 中文 AI 技能合集

面向 Codex 与兼容 Agent 的 **16 个可下载技能包**：自然中文写作、AI 产品逆向分析、豆包 GEO 内容运营、互联网搜索、可编辑 HTML 幻灯片和任务记忆管理。

**7 个个人创作／定制维护技能 + 5 个 GEO 整合包技能 + 4 个第三方技能。** 本仓库由 miseon-stack 整理维护；第三方版权与许可证保留。GEO 组的许可状态单独标注，不能将整个合集统一视为 MIT 授权。

[下载 ZIP](https://github.com/miseon-stack/ai-skills-collection/archive/refs/heads/main.zip) · [技能目录](#技能目录) · [来源和许可](NOTICE.md) · [版本发布](https://github.com/miseon-stack/ai-skills-collection/releases)

## 技能目录

| Skill | 中文名称 | 用途 | 分类 |
|---|---|---|---|
| [write-natural-chinese](skills/write-natural-chinese/SKILL.md) | 自然中文创作 | 从选题、研究、观点辩论到写作、配图与复审 | 个人创作／维护 |
| [map-user-journey](skills/map-user-journey/SKILL.md) | 用户旅程梳理 | 基于页面和截图重建产品用户旅程 | 个人创作／维护 |
| [map-agent-contracts](skills/map-agent-contracts/SKILL.md) | Agent 契约梳理 | 分析输入输出、工具、上下文和协作交接 | 个人创作／维护 |
| [rebuild-agent-prompt](skills/rebuild-agent-prompt/SKILL.md) | Agent 提示词还原 | 重建可追溯的功能等价提示词 | 个人创作／维护 |
| [map-product-architecture](skills/map-product-architecture/SKILL.md) | 产品架构梳理 | 整理 Agent、工具、上下文、资产和状态 | 个人创作／维护 |
| [reverse-ai-product](skills/reverse-ai-product/SKILL.md) | AI 产品逆向 | 串联四份产品拆解报告的完整流程 | 个人创作／维护 |
| [github-publish](skills/github-publish/SKILL.md) | GitHub 发布 | 利用已有浏览器登录会话发布并核对文件 | 个人创作／维护 |
| [doubao-geo-publisher](skills/doubao-geo-publisher/SKILL.md) | 豆包 GEO 工作流 | 客户诊断、内容规划、发布素材和效果复盘 | GEO 整合包 |
| [geo-keyword-miner](skills/geo-keyword-miner/SKILL.md) | GEO 关键词挖掘 | 客户资料转关键词、意图和优先级 | GEO 整合包 |
| [geo-article-writer](skills/geo-article-writer/SKILL.md) | GEO 文章写作 | 基于客户资料和证据生成文章 | GEO 整合包 |
| [geo-platform-adapter](skills/geo-platform-adapter/SKILL.md) | 多平台内容适配 | 头条、搜狐、知乎等平台版本改写 | GEO 整合包 |
| [geo-doubao-research](skills/geo-doubao-research/SKILL.md) | 豆包搜索研究 | 发布前后诊断、引用追踪和竞品信源分析 | GEO 整合包 |
| [agent-reach](skills/agent-reach/SKILL.md) | 互联网搜索与读取 | 多平台搜索与内容读取路由 | 第三方 |
| [humanize-chinese](skills/humanize-chinese/SKILL.md) | 中文去 AI 味 | 去除翻译腔、机械表达和模板化文风 | 第三方 |
| [frontend-slides-editable](skills/frontend-slides-editable/SKILL.md) | 可编辑 HTML 幻灯片 | 生成可在浏览器中编辑的演示文稿 | 第三方 |
| [codex-memory-guard](skills/codex-memory-guard/SKILL.md) | Codex 记忆管理 | 任务边界、关键决策和压缩后恢复 | 第三方 |

## 下载与安装

无需登录即可通过上方 ZIP 链接下载，或克隆仓库：

```bash
git clone https://github.com/miseon-stack/ai-skills-collection.git
cd ai-skills-collection
```

每个技能都是独立目录，入口为 `skills/<名称>/SKILL.md`，参考资料、模板和脚本随目录一并提供。

在 macOS / Linux 的 Codex 环境，可复制需要的目录到个人技能目录。例如首次安装自然中文创作：

```bash
mkdir -p ~/.codex/skills
cp -R skills/write-natural-chinese ~/.codex/skills/
```

若已经安装同名技能，请先备份已有目录，再决定是否替换。安装后重新打开任务，让环境重新发现技能。其他 Agent 的安装位置和支持能力请遵循对应环境说明。

完整使用 AI 产品逆向套件时，请将以下 5 个目录一起安装，保持同级目录关系：

- `reverse-ai-product`
- `map-user-journey`
- `map-agent-contracts`
- `rebuild-agent-prompt`
- `map-product-architecture`

GEO 五个技能也会相互协作，建议一起查看。

## 典型用法

- 自然中文创作：从一个想法开始，研究、讨论并完成文章。
- AI 产品逆向：根据截图和可见页面，输出用户旅程、Agent 契约、提示词重建和产品架构报告。
- 豆包 GEO：整理客户资料、挖掘关键词、写稿、适配平台，再检查搜索表现。
- 中文去 AI 味：审阅现有中文稿并改掉机械表达。
- 可编辑 HTML 幻灯片：生成可以继续拖拽和编辑的演示文稿。

在支持显式技能调用的环境中，可按入口名称选择技能。

## 运行要求与边界

- Skill 是工作流程与配套资源；下载不会自动安装外部 CLI、依赖、浏览器授权或模型服务。
- Agent Reach 的完整平台能力需要按其上游文档另外配置。
- GitHub 发布技能适用于已有浏览器登录会话的发布流程；本仓库无需该技能即可下载。
- Codex Memory Guard 的安装脚本面向 Windows PowerShell；目录中的文档可阅读，但不能据此认为 macOS 已启用 Hook。
- 自然中文创作的公开副本将原作者电脑上的固定保存目录改为当前工作目录下的 `outputs/articles`；可按自己的工作环境调整。
- GEO 模板中的品牌、电话、数据和案例是示例，使用时必须替换并核验。
- 可编辑幻灯片的样例图、模板和脚本随包提供；具体依赖见该技能的 README。

## 来源与许可证

个人维护技能与本仓库新增整理文档采用 MIT License；已有许可证继续有效。第三方内容保留原作者署名和许可证，包括幻灯片内嵌模板的独立许可证。

GEO 五个技能来自用户提供的整合包，源包没有独立许可证，作者／授权范围尚未核实。本仓库公开这些文件供查看和下载，但未替其原作者授予额外许可；复制、修改和再分发应先确认对应授权。详见 [NOTICE.md](NOTICE.md) 和 [技能清单](catalog.json)。

## 贡献与反馈

欢迎通过 Issues 提交使用反馈、失效链接和来源信息。贡献新技能时，请提供入口文件、用途说明、必要资源、明确来源与许可，避免包含个人账号资料。

## English

A curated collection of 16 Chinese-oriented AI agent skills for writing, product reverse engineering, GEO workflows, web research, editable HTML presentations, and context management. Browse the catalog, download the ZIP, or clone this repository. Individual licenses apply; the five GEO packages have unverified licensing and are not covered by the repository MIT grant.
