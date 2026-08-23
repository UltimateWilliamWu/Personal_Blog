---
title: Computer Science
tags:
  - Type/Index
---

# 💻 Computer Science 知识体系

> 这里是**体系导航层** —— 只做「学科地图 + 学习路径」，**不放具体内容**。
> 具体笔记按 `Topic/*` 标签自动聚合，点各主题页里的标签即可看到全部相关笔记。

---

## 🗺 依赖关系图

```
┌─ 基础层 ────────────────────────────────────┐
│  DiscreteMath ─┐                            │
│                ├──▶ Data Structures & Algo  │
│  Programming ──┘                            │
└─────────────────────────────┬───────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
┌─ 系统层 ──────┐    ┌─ 数据层 ──────┐    ┌─ 智能层 ──────┐
│  Operating    │    │  Database     │    │  AI           │
│  Systems      │───▶│      ↓        │───▶│   ├ ML        │
│  Network      │    │  Big Data     │    │   ├ DL        │
└───────────────┘    └───────────────┘    │   ├ CV        │
                                          │   └ NLP       │
                                          └───────────────┘
```

**读法**：上游是下游的前置。数学和编程是一切的地基；系统与数据层支撑智能层的工程落地。

---

## 📚 主题入口

### 基础

| 主题 | 状态 | 对应课程 |
|---|---|---|
| **[[DiscreteMath]]** | ✅ 有笔记 | [[COMP 9020]] |
| **[[Programming]]** | ✅ 有笔记 | [[COMP 9021]] · [[COMP 6991]] |
| **[[Data Structures and Algorithms]]** | ✅ 有笔记 | [[COMP 9024]] |

### 系统

| 主题 | 状态 | 对应课程 |
|---|---|---|
| **[[NetWork]]** | ✅ 有笔记 | [[COMP 9331]] |
| **[[Operating Systems]]** | ⬜ **空白** | *UNSW 未修相关课* |

### 数据

| 主题 | 状态 | 对应课程 |
|---|---|---|
| **[[Database]]** | ✅ 有笔记 | [[COMP 9311]] · [[COMP 9315]] |
| Big Data | ✅ 有笔记 → `#Topic/BigData` | [[COMP 9313]] |
| Data Engineering | 🟡 少量 → `#Topic/DataEngineering` | COMP 9321 |

### 智能

| 主题 | 状态 | 对应课程 |
|---|---|---|
| **[[Artificial Intelligence]]** | ✅ 笔记最多 | [[COMP 9414]] · [[COMP 9417]] · [[COMP 9444]] · [[COMP 9517]] · [[COMP 6713]] |

### 其他

| 主题 | 状态 |
|---|---|
| **[[Blockchain]]** | ⬜ **空白** |
| Project Management | 🟡 少量 → `#Topic/ProjectManagement` |

---

## ⚠️ 关于这个体系与实际笔记的落差

UNSW 的课程是**按学期切分的碎片**，不是按知识体系组织的。所以：

- **体系里有、笔记里没有的**：Operating Systems、Blockchain、编译原理、软件工程 —— 这些没修过课，是**已知缺口**，保留在这里作为后续填补的提纲
- **笔记里有、体系里原本没有的**：Big Data、Project Management、Data Engineering —— 已补进上表
- **一门课跨多个主题**：如 COMP 9417 同时属于 ML 和 AI，靠**多标签**解决，不靠目录

> 💡 **维护原则**：新笔记只要打上 `Topic/*` 标签就会自动出现在对应标签页，**不需要回来改这个文件**。
> 这个文件只在「新增一个主题」或「学习路径变化」时才需要动。

---

## 🔗 其他知识库

- [[UNSW/index|UNSW 课程笔记]] —— 按**课程**维度组织的原始笔记（97 篇 / 16 门课）
- [[CFA Program]] —— 金融方向
- [[Work/LeetCode/index|LeetCode 题解]] —— 算法实战
