---
layout: default
title: Flow Matching
---

<section class="topic-hero" style="--accent: #28d8ff;">
  <div>
    <p class="eyebrow">Topic</p>
    <h1>Flow Matching</h1>
    <p class="topic-lede">Updated 2026.04.09 · 10 papers</p>
  </div>
  <a class="btn ghost" href="../index.html#topics">← Back to topics</a>
</section>

<section class="paper-grid">
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Flow Motion Policy: Manipulator Motion Planning with Flow Matching Models</span>
        <span class="paper-authors">Davood Soleymanzadeh, Xiao Liang, Minghui Zheng</span>
        <span class="paper-meta">Updated 2026-04-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Open-loop end-to-end neural motion planners have recently been proposed to improve motion planning for robotic manipulators. These methods enable planning directly from sensor observations without relying on a privileged collision checker during planning. However, many existing methods generate only a single path for a given workspace across different runs, and do not leverage their open-loop structure for inference-time optimization. To address this limitation, we introduce Flow Motion Policy, an open-loop, end-to-end neural motion planner for robotic manipulators that leverages the stochastic generative formulation of flow matching methods to capture the inherent multi-modality of planning datasets. By modeling a distribution over feasible paths, Flow Motion Policy enables efficient inference-time best-of-$N$ sampling. The method generates multiple end-to-end candidate paths, evaluates their collision status after planning, and executes the first collision-free solution. We benchmark the Flow Motion Policy against representative sampling-based and neural motion planning methods. Evaluation results demonstrate that Flow Motion Policy improves planning success and efficiency, highlighting the effectiveness of stochastic generative policies for end-to-end motion planning and inference-time optimization. Experimental evaluation videos are available via this \href{https://zh.engr.tamu.edu/wp-content/uploads/sites/310/2026/03/FMP-Website.mp4}{link}.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.07084">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.07084.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.07084.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FlowInOne:Unifying Multimodal Generation as Image-in, Image-out Flow Matching</span>
        <span class="paper-authors">Junchao Yi, Rui Zhao, Jiahao Tang, Weixian Lei, Linjie Li, Qisheng Su, Zhengyuan Yang, Lijuan Wang, Xiaofeng Zhu, Alex Jinpeng Wang</span>
        <span class="paper-meta">Updated 2026-04-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Multimodal generation has long been dominated by text-driven pipelines where language dictates vision but cannot reason or create within it. We challenge this paradigm by asking whether all modalities, including textual descriptions, spatial layouts, and editing instructions, can be unified into a single visual representation. We present FlowInOne, a framework that reformulates multimodal generation as a purely visual flow, converting all inputs into visual prompts and enabling a clean image-in, image-out pipeline governed by a single flow matching model. This vision-centric formulation naturally eliminates cross-modal alignment bottlenecks, noise scheduling, and task-specific architectural branches, unifying text-to-image generation, layout-guided editing, and visual instruction following under one coherent paradigm. To support this, we introduce VisPrompt-5M, a large-scale dataset of 5 million visual prompt pairs spanning diverse tasks including physics-aware force dynamics and trajectory prediction, alongside VP-Bench, a rigorously curated benchmark assessing instruction faithfulness, spatial precision, visual realism, and content consistency. Extensive experiments demonstrate that FlowInOne achieves state-of-the-art performance across all unified generation tasks, surpassing both open-source models and competitive commercial systems, establishing a new foundation for fully vision-centric generative modeling where perception and creation coexist within a single continuous visual space.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.06757">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.06757.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.06757.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model</span>
        <span class="paper-authors">Kaidong Zhang, Jian Zhang, Rongtao Xu, Yu Sun, Shuoshuo Xue, Youpeng Wen, Xiaoyu Guo, Minghao Guo, Weijia Liufu, Liu Zihou, Kangyi Ji, Yangsong Zhang, Jiarun Zhu, Jingzhi Liu, Zihang Li, Ruiyi Chen, Meng Cao, Jingming Zhang, Shen Zhao, Xiaojun Chang, Feng Zheng, Ivan Laptev, Xiaodan Liang</span>
        <span class="paper-meta">Updated 2026-04-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Vision-Language-Action (VLA) models have emerged as a powerful paradigm for open-world robot manipulation, but their practical deployment is often constrained by cost: billion-scale VLM backbones and iterative diffusion/flow-based action heads incur high latency and compute, making real-time control expensive on commodity hardware. We present A1, a fully open-source and transparent VLA framework designed for low-cost, high-throughput inference without sacrificing manipulation success; Our approach leverages pretrained VLMs that provide implicit affordance priors for action generation. We release the full training stack (training code, data/data-processing pipeline, intermediate checkpoints, and evaluation scripts) to enable end-to-end reproducibility. Beyond optimizing the VLM alone, A1 targets the full inference pipeline by introducing a budget-aware adaptive inference scheme that jointly accelerates the backbone and the action head. Specifically, we monitor action consistency across intermediate VLM layers to trigger early termination, and propose Inter-Layer Truncated Flow Matching that warm-starts denoising across layers, enabling accurate actions with substantially fewer effective denoising iterations. Across simulation benchmarks (LIBERO, VLABench) and real robots (Franka, AgiBot), A1 achieves state-of-the-art success rates while significantly reducing inference cost (e.g., up to 72% lower per-episode latency for flow-matching inference and up to 76.6% backbone computation reduction with minor performance degradation). On RoboChallenge, A1 achieves an average success rate of 29.00%, outperforming baselines including pi0(28.33%), X-VLA (21.33%), and RDT-1B (15.00%).</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.05672">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.05672.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.05672.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Discrete Flow Matching Policy Optimization</span>
        <span class="paper-authors">Maojiang Su, Po-Chung Hsieh, Weimin Wu, Mingcheng Lu, Jiunhau Chen, Jerry Yao-Chieh Hu, Han Liu</span>
        <span class="paper-meta">Updated 2026-04-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We introduce Discrete flow Matching policy Optimization (DoMinO), a unified framework for Reinforcement Learning (RL) fine-tuning Discrete Flow Matching (DFM) models under a broad class of policy gradient methods. Our key idea is to view the DFM sampling procedure as a multi-step Markov Decision Process. This perspective provides a simple and transparent reformulation of fine-tuning reward maximization as a robust RL objective. Consequently, it not only preserves the original DFM samplers but also avoids biased auxiliary estimators and likelihood surrogates used by many prior RL fine-tuning methods. To prevent policy collapse, we also introduce new total-variation regularizers to keep the fine-tuned distribution close to the pretrained one. Theoretically, we establish an upper bound on the discretization error of DoMinO and tractable upper bounds for the regularizers. Experimentally, we evaluate DoMinO on regulatory DNA sequence design. DoMinO achieves stronger predicted enhancer activity and better sequence naturalness than the previous best reward-driven baselines. The regularization further improves alignment with the natural sequence distribution while preserving strong functional performance. These results establish DoMinO as an useful framework for controllable discrete sequence generation.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.06491">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.06491.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.06491.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ODE-free Neural Flow Matching for One-Step Generative Modeling</span>
        <span class="paper-authors">Xiao Shou</span>
        <span class="paper-meta">Updated 2026-04-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Diffusion and flow matching models generate samples by learning time-dependent vector fields whose integration transports noise to data, requiring tens to hundreds of network evaluations at inference. We instead learn the transport map directly. We propose Optimal Transport Neural Flow Matching (OT-NFM), an ODE-free generative framework that parameterizes the flow map with neural flows, enabling true one-step generation with a single forward pass. We show that naive flow-map training suffers from mean collapse, where inconsistent noise-data pairings drive all outputs toward the data mean. We prove that consistent coupling is necessary for non-degenerate learning and address this using optimal transport pairings with scalable minibatch and online coupling strategies. Experiments on synthetic benchmarks and image generation tasks (MNIST and CIFAR-10) demonstrate competitive sample quality while reducing inference to a single network evaluation.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.06413">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.06413.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.06413.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Lipschitz regularity in Flow Matching and Diffusion Models: sharp sampling rates and functional inequalities</span>
        <span class="paper-authors">Arthur Stéphanovitch</span>
        <span class="paper-meta">Updated 2026-04-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Under general assumptions on the target distribution $p^\star$, we establish a sharp Lipschitz regularity theory for flow-matching vector fields and diffusion-model scores, with optimal dependence on time and dimension. As applications, we obtain Wasserstein discretization bounds for Euler-type samplers in dimension $d$: with $N$ discretization steps, the error achieves the optimal rate $\sqrt{d}/N$ up to logarithmic factors. Moreover, the constants do not deteriorate exponentially with the spatial extent of $p^\star$. We also show that the one-sided Lipschitz control yields a globally Lipschitz transport map from the standard Gaussian to $p^\star$, which implies Poincaré and log-Sobolev inequalities for a broad class of probability measures.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.06065">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.06065.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.06065.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Optimal-Transport-Guided Functional Flow Matching for Turbulent Field Generation in Hilbert Space</span>
        <span class="paper-authors">Li Kunpeng, Wan Chenguang, Qu Zhisong, Lim Kyungtak, Virginie Grandgirard, Xavier Garbet, Yu Hua, Ong Yew Soon</span>
        <span class="paper-meta">Updated 2026-04-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">High-fidelity modeling of turbulent flows requires capturing complex spatiotemporal dynamics and multi-scale intermittency, posing a fundamental challenge for traditional knowledge-based systems. While deep generative models, such as diffusion models and Flow Matching, have shown promising performance, they are fundamentally constrained by their discrete, pixel-based nature. This limitation restricts their applicability in turbulence computing, where data inherently exists in a functional form. To address this gap, we propose Functional Optimal Transport Conditional Flow Matching (FOT-CFM), a generative framework defined directly in infinite-dimensional function space. Unlike conventional approaches defined on fixed grids, FOT-CFM treats physical fields as elements of an infinite-dimensional Hilbert space, and learns resolution-invariant generative dynamics directly at the level of probability measures. By integrating Optimal Transport (OT) theory, we construct deterministic, straight-line probability paths between noise and data measures in Hilbert space. This formulation enables simulation-free training and significantly accelerates the sampling process. We rigorously evaluate the proposed system on a diverse suite of chaotic dynamical systems, including the Navier-Stokes equations, Kolmogorov Flow, and Hasegawa-Wakatani equations, all of which exhibit rich multi-scale turbulent structures. Experimental results demonstrate that FOT-CFM achieves superior fidelity in reproducing high-order turbulent statistics and energy spectra compared to state-of-the-art baselines.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.05700">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.05700.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.05700.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Rectified Schrödinger Bridge Matching for Few-Step Visual Navigation</span>
        <span class="paper-authors">Wuyang Luan, Junhui Li, Weiguang Zhao, Wenjian Zhang, Tieru Wu, Rui Ma</span>
        <span class="paper-meta">Updated 2026-04-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Visual navigation is a core challenge in Embodied AI, requiring autonomous agents to translate high-dimensional sensory observations into continuous, long-horizon action trajectories. While generative policies based on diffusion models and Schrödinger Bridges (SB) effectively capture multimodal action distributions, they require dozens of integration steps due to high-variance stochastic transport, posing a critical barrier for real-time robotic control. We propose Rectified Schrödinger Bridge Matching (RSBM), a framework that exploits a shared velocity-field structure between standard Schrödinger Bridges ($\varepsilon=1$, maximum-entropy transport) and deterministic Optimal Transport ($\varepsilon\to 0$, as in Conditional Flow Matching), controlled by a single entropic regularization parameter $\varepsilon$. We prove two key results: (1) the conditional velocity field&#x27;s functional form is invariant across the entire $\varepsilon$-spectrum (Velocity Structure Invariance), enabling a single network to serve all regularization strengths; and (2) reducing $\varepsilon$ linearly decreases the conditional velocity variance, enabling more stable coarse-step ODE integration. Anchored to a learned conditional prior that shortens transport distance, RSBM operates at an intermediate $\varepsilon$ that balances multimodal coverage and path straightness. Empirically, while standard bridges require $\geq 10$ steps to converge, RSBM achieves over 94% cosine similarity and 92% success rate in merely 3 integration steps -- without distillation or multi-stage training -- substantially narrowing the gap between high-fidelity generative policies and the low-latency demands of Embodied AI.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.05673">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.05673.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.05673.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation</span>
        <span class="paper-authors">Wuyang Luan, Junhui Li, Weiguang Zhao, Wenjian Zhang, Tieru Wu, Rui Ma</span>
        <span class="paper-meta">Updated 2026-04-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Vision-Language-Action (VLA) models based on flow matching -- such as pi0, pi0.5, and SmolVLA -- achieve state-of-the-art generalist robotic manipulation, yet their iterative denoising, typically 10 ODE steps, introduces substantial latency: on a modern GPU, denoising alone accounts for 80% of end-to-end inference time. Naively reducing the step count is unreliable, degrading success on most tasks due to the velocity field being uncalibrated for single-step jumps. We present SnapFlow, a plug-and-play self-distillation method that compresses multi-step denoising into a single forward pass (1-NFE) for flow-matching VLAs. SnapFlow mixes standard flow-matching samples with consistency samples whose targets are two-step Euler shortcut velocities computed from the model&#x27;s own marginal velocity predictions, avoiding the trajectory drift caused by conditional velocities, as we analyze theoretically. A zero-initialized target-time embedding lets the network switch between local velocity estimation and global one-step generation within a single architecture. SnapFlow requires no external teacher, no architecture changes, and trains in ~12h on a single GPU. We validate on two VLA architectures spanning a 6x parameter range, with identical hyperparameters: on pi0.5 (3B) across four LIBERO suites (40 tasks, 400 episodes), SnapFlow achieves 98.75% average success -- matching the 10-step teacher at 97.75% and slightly exceeding it -- with 9.6x denoising speedup and end-to-end latency reduced from 274ms to 83ms; on SmolVLA (500M), it reduces MSE by 8.3% with 3.56x end-to-end acceleration. An action-step sweep on long-horizon tasks reveals that SnapFlow maintains its advantage across execution horizons, achieving 93% at n_act=5 where the baseline reaches only 90%. SnapFlow is orthogonal to layer-distillation and token-pruning approaches, enabling compositional speedups.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.05656">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.05656.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.05656.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Unifying VLM-Guided Flow Matching and Spectral Anomaly Detection for Interpretable Veterinary Diagnosis</span>
        <span class="paper-authors">Pu Wang, Zhixuan Mao, Jialu Li, Zhuoran Zheng, Dianjie Lu, Youshan Zhang</span>
        <span class="paper-meta">Updated 2026-04-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Automatic diagnosis of canine pneumothorax is challenged by data scarcity and the need for trustworthy models. To address this, we first introduce a public, pixel-level annotated dataset to facilitate research. We then propose a novel diagnostic paradigm that reframes the task as a synergistic process of signal localization and spectral detection. For localization, our method employs a Vision-Language Model (VLM) to guide an iterative Flow Matching process, which progressively refines segmentation masks to achieve superior boundary accuracy. For detection, the segmented mask is used to isolate features from the suspected lesion. We then apply Random Matrix Theory (RMT), a departure from traditional classifiers, to analyze these features. This approach models healthy tissue as predictable random noise and identifies pneumothorax by detecting statistically significant outlier eigenvalues that represent a non-random pathological signal. The high-fidelity localization from Flow Matching is crucial for purifying the signal, thus maximizing the sensitivity of our RMT detector. This synergy of generative segmentation and first-principles statistical analysis yields a highly accurate and interpretable diagnostic system (source code is available at: https://github.com/Pu-Wang-alt/Canine-pneumothorax).</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.05482">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.05482.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.05482.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
</section>
