# 链环的部分推广：Hopf 纤维链环、环带卫星及连通和

任意非空有向 Hopf 纤维链环的全循环不可压复形 $`X`$ 都可缩。对全部平衡 $`H_{2m}`$，证明用等变高度插值、正则纤维弧流平均、完美匹配多面体的区域势共同取整，给出任意有限输入的包含零伦；解码沿零权面相容，能恢复真实输入单形的原重心坐标。不平衡者在规定生成类中纤维化，复形为一点。

环带卫星另有三种完整计算：满足 (SB) 时为锥；伴随为环面结时恰为一条边；伴随为 $`K_{7/19}`$ 时整个复形是树，标准环带仍不是锥顶。四纤维 Farey 树、声明输入下的全连通推广与 Banks 闭包组织这些结果。顶点包括全部不可压亏格，允许不连通和非范数极小；一般链环推广仍是部分结论。

## 目标与对象

目标为 Apex Intelligence 署名的比赛版 *Contractibility of the Complex of Incompressible Seifert Surfaces: The Knot Case of Kakimizu's Problem*，2026-09-11，48 页。引言第 2 页留下了一般链环推广，Theorem D 使用 linking-indecomposable 条件。PDF SHA-256：

```text
34f17d7d99780d3fd3626d9e5d7b35d6aa76661c404f191b6df341b300c0c06f
```

生成曲面有取向、逐分量不可压、无闭分量，每个带标签的实际边界环面恰有一条规定边界。同痕允许边界移动。边由整个补域的最小循环覆盖宽度一确定，再取旗复形；完整补域只能有一次共同 deck 平移。全连通情形与原始几何不交复形一致，不推断一般不连通情形的两种复形相同。

## 主要计算

**全部 Hopf 纤维链环。** 平衡 $`H_{2m}`$ 的顶点与 $`2m`$ 孔球面上的 $`m`$ 条正负匹配弧系统一一对应。规范叠图在同一个完整补块中的整数势给出 $`\delta=\max H-\min H`$，不受孔数限制。真实单形具有共同不交的规范弧代表；六孔的“不交即邻接”只保留为特例，不推广到任意孔数。六孔复形含四面体，四孔复形保留 Farey 树。

任意有限输入一次性选共同带、三角剖分及循环覆盖中的归一高度，再做凸插值。边界单调且次数为 $`\pm1`$，故每孔恰有一个正则端点；删除闭圈后仍有合法匹配。先在弧坐标上按相位长度平均，得到实际嵌入支撑图的 $`w\in P_G`$。

以参考匹配写出 $`w=m+D_Gu`$，共同取整 $`m+D_G\lfloor u+\theta\rfloor`$ 给出合法匹配；任意两阈值的差势振幅至多一，由完整补块公式得到真实单形。解码器连续、与删零边相容，且精确恢复每个原输入单形的重心坐标。固定图的诱导复形剖分整个 $`P_G`$，不必是一张单形。统一有限模板与零面规则处理相位碰撞和图变化，最终给出包含映射在有限输出中的零伦；有限输出本身不必可缩。

圆值映射、正则纤维及平均归于 Hatcher 2008 第二证明，第 5–6 页。平面二部匹配的面高度与分配格属于经典结构，背景引 Propp，arXiv:math/0209005v3，§3 Theorem 2 及第 21–22 页；这里所需势、取整、距离及粘合均自足证明。PS Theorem 1.1 的陈述已覆盖平衡族，本包的贡献是避开 PS §§4–7 的独立族证明；模型与距离仍用 §3。不平衡时 $`\phi(f)=\sum_i\epsilon_i\ne0`$，由 Seifert 水平分支纤维化，复形为一点。

**卫星的锥与边。** (SB) 要求：伴随外部中，非空边界全为首选经线的连通定向本质曲面只有一条边界。本质包括不可压和边界不可压。在此条件下，标准环带邻接每个其他顶点，整个复形为锥。环面结伴随还可完整分类并消去剩余扭转，顶点只有环带及两张反向伴随纤维加 reaching 环带，恰为一条边。

二桥结满足 (SB)，当且仅当每个零斜率 admissible 减号连分数载体都全偶。这包括 $`K_{(2m-1)/(4m-1)}`$，$`m\ge1`$，及镜像；$`m=2`$ 包含 $`5_2=K_{3/7}`$。未声称 $`5_2`$ 平行链环有无穷多顶点。

**超出 (SB) 的完整树。** $`K_{7/19}`$ 的两平行链环顶点为环带 $`A`$、唯一不连通顶点 $`G`$，以及亏格 $`3k`$ 的连通链。枕套参考图固定后，链坐标为

```math
k\ge1,\qquad 0\le a\lt2k,\qquad
\gcd(2a+1,2k)=1,\qquad t\in\mathbb Z,
```

没有额外扭转同痕识别。令 $`p=2a+1+4kt`$，链顶点恰对应奇分子的既约分数 $`p/k`$；$`A=1/0`$。链之间的边恰由 $`|pk'-p'k|=1`$ 给出。$`A`$ 邻接全部 $`k=1`$ 链和 $`G`$，$`G`$ 只是一片叶子。每个非根点有唯一低分母邻居，全图为树，旗完成没有高维单形。线性子族满足 $`\delta(A,F_k)=k`$，环带不是锥顶，但整个复形可缩。子午返回子群为零及三维曲面与标记弧之间双向边对应都有完整证明；镜像由反射继承。

## 组织定理、闭包与范围

因子集合为纽结、声明几何输入下的全连通类、全部平衡 $`H_{2m}`$（$`m\ge1`$，不平衡者属于纤维类）、规定生成类的纤维链环、(SB) 两平行链环，以及 $`K_{7/19}`$ 两平行链环及其镜像。有限次二元连通和每次连接两个原先不交块的指定分量；若原始非纤维因子数为 $`r`$，则

```math
r=0\Longrightarrow X(L)=\{*\},\qquad
r\ge1\Longrightarrow
|X(L)|\cong\prod_{J_i\ \mathrm{nonfibred}}|X(J_i)|\times\mathbb R^{r-1}.
```

采用 Banks 的有序乘积剖分。中间非分裂性、纤维性的双向条件及全不可压纤维因子吸收均有证明。$`m\ge2`$ 时，$`F_{2m-1}\to\mathbb Z`$ 的核有 $`2m-2`$ 组无限 Schreier 生成元，故平衡 $`H_{2m}`$ 非纤维；$`H_2`$ 则有环带生成纤维。卫星的注入环面群 $`\mathbb Z^2\subset\ker\phi`$ 排除带边界纤维的自由核。

在全部 $`2m`$ 条纤维上局部结入，令 $`I=\{i:K_i\text{ 为非纤维结}\}`$。$`m\ge2`$ 时，

```math
|X(H_{2m}\#_1K_1\cdots\#_{2m}K_{2m})|
\cong |X(H_{2m})|\times\prod_{i\in I}|X(K_i)|\times\mathbb R^{|I|}.
```

指数来自 $`r=1+|I|`$。$`m=1`$ 时 $`r=|I|`$：无非纤维结入则为一点，否则结因子乘积的欧氏指数为 $`|I|-1`$。纤维纽结不增加绕行坐标，不使用负指数。

独立连通性界 $`b_0(F)-1\le r_\phi(L)`$ 用 rational Alexander rank 检验全部生成曲面的连通性。继承原论文的连通多边界几何输入和组合 Theorem B 后，全连通复形及完整字典序复杂度下闭的非空全子复形可缩。精确辫证书给出链接数全零的实例；证明保留目标论文 §6.3 第 22 页的长度分类更正。

Seifert 的 $`k=\phi(f)=0`$ 分支给出竖直环带及 reduced 约定下的 $`X=MS`$。本包独立证明全部平衡 Hopf 纤维链环可缩；不平衡者由 $`k\ne0`$ 的水平乘积补域纤维化。带例外纤维的一般 $`k=0`$ 情形仍未纳入可缩性定理。

## PS 证书与文献边界

[反例说明](proof/ps-counterexample.md) 自成一体，给出 PS Lemma 6.1、Lemma 6.5 半径一顶点结论和 Theorem 7.2 的反例，以及两条类距离核验。有限根凸旗四环又包含在 $`[0,1]^{12}`$ 的有限填充中，最小范数层内也可填充；没有否定 Theorem 1.1 的整个复形可缩性陈述。因此主定理不加入全部最小曲面因子，只有各自另有独立可缩性证明时才可归入闭包。

Hopf 匹配模型与 Banks 接口保留声明的 PS §3、§5 结果。正面可缩性与闭包不消费 PS 的投影或一般收缩。纽结及全连通推广保留比赛论文的相应输入。Banks 乘积定理归于 Banks；圆映射方法归于 Hatcher，经典面高度背景归于 Propp。2026-10-07 的文献检索未找到 PS 2012 的勘误。Schultens 2017/2018 使用带权、自由边界框架，Seifert 空间的证明限于闭空间，不能直接替代这里固定边界、无权对象的证明。

## 导览

| 文件 | 内容 |
|---|---|
| [Hopf 匹配模型](proof/hopf-model.md) | 全部平衡孔数的顶点、编码、完整补块距离及六孔特例 |
| [全孔数 Hopf 收缩](proof/hopf-contraction.md) | 固定图多面体解码、精确起点、零面粘合及任意有限零伦 |
| [卫星锥](proof/parallel-satellites.md) | (SB)、同一代表不交及完整补块分离 |
| [环面结的一条边](proof/parallel-satellites-torus.md) | 全分类、联合纤维同痕和兼容粘合 |
| [二桥判据](proof/parallel-satellites-two-bridge.md) | 精确 (SB) 范围及无限伴随族 |
| [距离二实例](proof/parallel-satellites-obstruction.md) | 环带不是锥顶的亏格六见证 |
| [几何正规化](proof/parallel-satellites-normalisation.md) | 本质切片、乘积环带及保 T 比较 |
| [联合经线正规形](proof/parallel-satellites-k719-normal-forms.md) | HT 参数、纯堆叠、闭分量判据、几何同痕测试 |
| [完整卫星树](proof/parallel-satellites-k719-tree.md) | 零返回子群、坐标、全部边和整个收缩 |
| [PS 反例](proof/ps-counterexample.md) | 实际投影、九个距离、三条反例和十二维有限填充 |
| [对象](proof/objects.md) | 边界、完整补域、压缩 |
| [全连通推广](proof/connected-surfaces.md) | 连通性、两组精确例子 |
| [交换拓扑](proof/connected-surfaces-exchange.md) | 继承输入、固定输出类 |
| [collar 与收益](proof/connected-surfaces-collars.md) | 扰动、长度更正、面积 |
| [全连通结论](proof/connected-surfaces-contractibility.md) | 可缩性、下闭截断 |
| [四纤维树](proof/hopf-four.md) | 顶点、距离、树 |
| [Banks 接口](proof/connected-sum.md) | 全不可压乘积及纤维吸收 |
| [Seifert](proof/seifert.md) | 结构二分、分类与边界 |
| [主定理](proof/main-theorem.md) | 因子、闭包、非纤维性、全纤维结入和依赖表 |
| [范围](proof/scope.md) | 方法归属、保留输入、未证推广 |
| [文献](sources/bibliography.md) | 公开版本与实际核对页码 |
| [计算](scripts/README.md) | 随包分发的精确辫证书 |

## 核验、AI 声明与许可

各模型、收缩和卫星证明有独立全新上下文复核。本合并版本没有新增独立跨文稿复核或证明助手认证。随包计算使用精确算术，公式检查只认证语法。文献表记录版本和页码，`MANIFEST.sha256` 覆盖除自身外全部文件。

GPT-6.1 Sol, in OpenAI Codex under human direction, developed the proof, ran the computations where applicable, and drafted this text; a separate GPT-6.1 Sol session in a fresh context performed an adversarial review. Claude planned the work, checked key steps against the sources, and reviewed and edited the final text. No human expert has certified the work.

原创文字采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，`scripts/` 代码及证明中的可执行示例采用 [MIT](scripts/LICENSE)。外部论文不随包分发，保留其原有条款。详见 [LICENSE](LICENSE)。
