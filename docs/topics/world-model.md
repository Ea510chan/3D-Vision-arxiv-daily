---
layout: default
title: World Model
---

<section class="topic-hero" style="--accent: #28d8ff;">
  <div>
    <p class="eyebrow">Topic</p>
    <h1>World Model</h1>
    <p class="topic-lede">Updated 2026.04.09 · 10 papers</p>
  </div>
  <a class="btn ghost" href="../index.html#topics">← Back to topics</a>
</section>

<section class="paper-grid">
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">How Much LLM Does a Self-Revising Agent Actually Need?</span>
        <span class="paper-authors">Seongwoo Jeong, Seonil Son</span>
        <span class="paper-meta">Updated 2026-04-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Recent LLM-based agents often place world modeling, planning, and reflection inside a single language model loop. This can produce capable behavior, but it makes a basic scientific question difficult to answer: which part of the agent&#x27;s competence actually comes from the LLM, and which part comes from explicit structure around it?   We study this question not by claiming a general answer, but by making it empirically tractable. We introduce a declared reflective runtime protocol that externalizes agent state, confidence signals, guarded actions, and hypothetical transitions into inspectable runtime structure. We instantiate this protocol in a declarative runtime and evaluate it on noisy Collaborative Battleship [4] using four progressively structured agents over 54 games (18 boards $\times$ 3 seeds).   The resulting decomposition isolates four components: posterior belief tracking, explicit world-model planning, symbolic in-episode reflection, and sparse LLM-based revision. Across this decomposition, explicit world-model planning improves substantially over a greedy posterior-following baseline (+24.1pp win rate, +0.017 F1). Symbolic reflection operates as a real runtime mechanism -- with prediction tracking, confidence gating, and guarded revision actions -- even though its current revision presets are not yet net-positive in aggregate. Adding conditional LLM revision at about 4.3\% of turns yields only a small and non-monotonic change: average F1 rises slightly (+0.005) while win rate drops (31$\rightarrow$29 out of 54).   These results suggest a methodological contribution rather than a leaderboard claim: externalizing reflection turns otherwise latent agent behavior into inspectable runtime structure, allowing the marginal role of LLM intervention to be studied directly.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.07236">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.07236.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.07236.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">PhyEdit: Towards Real-World Object Manipulation via Physically-Grounded Image Editing</span>
        <span class="paper-authors">Ruihang Xu, Dewei Zhou, Xiaolong Shen, Fan Ma, Yi Yang</span>
        <span class="paper-meta">Updated 2026-04-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Achieving physically accurate object manipulation in image editing is essential for its potential applications in interactive world models. However, existing visual generative models often fail at precise spatial manipulation, resulting in incorrect scaling and positioning of objects. This limitation primarily stems from the lack of explicit mechanisms to incorporate 3D geometry and perspective projection. To achieve accurate manipulation, we develop PhyEdit, an image editing framework that leverages explicit geometric simulation as contextual 3D-aware visual guidance. By combining this plug-and-play 3D prior with joint 2D--3D supervision, our method effectively improves physical accuracy and manipulation consistency. To support this method and evaluate performance, we present a real-world dataset, RealManip-10K, for 3D-aware object manipulation featuring paired images and depth annotations. We also propose ManipEval, a benchmark with multi-dimensional metrics to evaluate 3D spatial control and geometric consistency. Extensive experiments show that our approach outperforms existing methods, including strong closed-source models, in both 3D geometric accuracy and manipulation consistency.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.07230">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.07230.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.07230.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">INSPATIO-WORLD: A Real-Time 4D World Simulator via Spatiotemporal Autoregressive Modeling</span>
        <span class="paper-authors">InSpatio Team, Donghui Shen, Guofeng Zhang, Haomin Liu, Haoyu Ji, Hujun Bao, Hongjia Zhai, Jialin Liu, Jing Guo, Nan Wang, Siji Pan, Weihong Pan, Weijian Xie, Xianbin Liu, Xiaojun Xiang, Xiaoyu Zhang, Xinyu Chen, Yifu Wang, Yipeng Chen, Zhenzhou Fan, Zhewen Le, Zhichao Ye, Ziqiang Zhao</span>
        <span class="paper-meta">Updated 2026-04-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Building world models with spatial consistency and real-time interactivity remains a fundamental challenge in computer vision. Current video generation paradigms often struggle with a lack of spatial persistence and insufficient visual realism, making it difficult to support seamless navigation in complex environments. To address these challenges, we propose INSPATIO-WORLD, a novel real-time framework capable of recovering and generating high-fidelity, dynamic interactive scenes from a single reference video. At the core of our approach is a Spatiotemporal Autoregressive (STAR) architecture, which enables consistent and controllable scene evolution through two tightly coupled components: Implicit Spatiotemporal Cache aggregates reference and historical observations into a latent world representation, ensuring global consistency during long-horizon navigation; Explicit Spatial Constraint Module enforces geometric structure and translates user interactions into precise and physically plausible camera trajectories. Furthermore, we introduce Joint Distribution Matching Distillation (JDMD). By using real-world data distributions as a regularizing guide, JDMD effectively overcomes the fidelity degradation typically caused by over-reliance on synthetic data. Extensive experiments demonstrate that INSPATIO-WORLD significantly outperforms existing state-of-the-art (SOTA) models in spatial consistency and interaction precision, ranking first among real-time interactive methods on the WorldScore-Dynamic benchmark, and establishing a practical pipeline for navigating 4D environments reconstructed from monocular videos.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.07209">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.07209.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.07209.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Radio-Frequency Inverse Rendering for Wireless Environment Modeling</span>
        <span class="paper-authors">Fuhai Wang, Zihan Jin, Lehang Wang, Xuehui Dong, Tiebin Mi, Robert Caiming Qiu, Zenan ling</span>
        <span class="paper-meta">Updated 2026-04-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Neural rendering paradigms have recently emerged as powerful tools for radio frequency (RF). However, by entangling RF sources with scene geometry and material properties, existing approaches limit downstream manipulation of scene geometry, wireless system configuration, and RF reasoning. To address this, we propose a physically grounded RF inverse rendering (RFIR) framework that explicitly decouples RF emission, geometry, and material electromagnetic properties. Our key insight is an RF-aware bidirectional scattering distribution function, embedded into the Gaussian splatting paradigm as an RF rendering equation. Each Gaussian primitive is endowed with intrinsic physical attributes, including surface normals, material electromagnetic parameters, and roughness, and leveraged by a customized ray-tracing scheme to represent RF signal synthesis. The proposed RFIR generalizes three typical RF tasks: radar cross-section synthesis, received signal strength indicator prediction, and wireless scene editability. Experiments demonstrate significant performance advantages, underscoring the potential for wireless world modeling.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.07086">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.07086.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.07086.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Telecom World Models: Unifying Digital Twins, Foundation Models, and Predictive Planning for 6G</span>
        <span class="paper-authors">Hang Zou, Yuzhi Yang, Lina Bariah, Yu Tian, Yuhuan Lu, Bohao Wang, Anis Bara, Brahim Mefgouda, Hao Liu, Yiwei Tao, Sergy Petrov, Salma Cheour, Nassim Sehad, Sumudu Samarakoon, Chongwen Huang, Samson Lasaulce, Mehdi Bennis, Mérouane Debbah</span>
        <span class="paper-meta">Updated 2026-04-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">The integration of machine learning tools into telecom networks, has led to two prevailing paradigms, namely, language-based systems, such as Large Language Models (LLMs), and physics-based systems, such as Digital Twins (DTs). While LLM-based approaches enable flexible interaction and automation, they lack explicit representations of network dynamics. DTs, in contrast, offer a high-fidelity network simulation, but remain scenario-specific and are not designed for learning or decision-making under uncertainty. This gap becomes critical for 6G systems, where decisions must take into account the evolving network states, uncertainty, and the cascading effects of control actions across multiple layers. In this article, we introduce the {Telecom World Model}~(TWM) concept, an architecture for learned, action-conditioned, uncertainty-aware modeling of telecom system dynamics. We decompose the problem into two interacting worlds, a controllable system world consisting of operator-configurable settings and an external world that captures propagation, mobility, traffic, and failures. We propose a three-layer architecture, comprising a field world model for spatial environment prediction, a control/dynamics world model for action-conditioned Key Performance Indicator (KPI) trajectory prediction, and a telecom foundation model layer for intent translation and orchestration. We showcase a comparative analysis between existing paradigms, which demonstrates that TWM jointly provides telecom state grounding, fast action-conditioned roll-outs, calibrated uncertainty, multi-timescale dynamics, model-based planning, and LLM-integrated guardrails. Furthermore, we present a proof-of-concept on network slicing to validate the proposed architecture, showing that the full three-layer pipeline outperforms single-world baselines and accurately predicts KPI trajectories.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.06882">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.06882.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.06882.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">The Rhetoric of Machine Learning</span>
        <span class="paper-authors">Robert C. Williamson</span>
        <span class="paper-meta">Updated 2026-04-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">I examine the technology of machine learning from the perspective of rhetoric, which is simply the art of persuasion. Rather than being a neutral and &quot;objective&quot; way to build &quot;world models&quot; from data, machine learning is (I argue) inherently rhetorical. I explore some of its rhetorical features, and examine one pervasive business model where machine learning is widely used, &quot;manipulation as a service.&quot;</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.06754">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.06754.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.06754.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Controllable Generative Video Compression</span>
        <span class="paper-authors">Ding Ding, Daowen Li, Ying Chen, Yixin Gao, Ruixiao Dong, Kai Li, Li Li</span>
        <span class="paper-meta">Updated 2026-04-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Perceptual video compression adopts generative video modeling to improve perceptual realism but frequently sacrifices signal fidelity, diverging from the goal of video compression to faithfully reproduce visual signal. To alleviate the dilemma between perception and fidelity, in this paper we propose Controllable Generative Video Compression (CGVC) paradigm to faithfully generate details guided by multiple visual conditions. Under the paradigm, representative keyframes of the scene are coded and used to provide structural priors for non-keyframe generation. Dense per-frame control prior is additionally coded to better preserve finer structure and semantics of each non-keyframe. Guided by these priors, non-keyframes are reconstructed by controllable video generation model with temporal and content consistency. Furthermore, to accurately recover color information of the video, we develop a color-distance-guided keyframe selection algorithm to adaptively choose keyframes. Experimental results show CGVC outperforms previous perceptual video compression method in terms of both signal fidelity and perceptual quality.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.06655">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.06655.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.06655.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Neural Computers</span>
        <span class="paper-authors">Mingchen Zhuge, Changsheng Zhao, Haozhe Liu, Zijian Zhou, Shuming Liu, Wenyi Wang, Ernie Chang, Gael Le Lan, Junjie Fei, Wenxuan Zhang, Yasheng Sun, Zhipeng Cai, Zechun Liu, Yunyang Xiong, Yining Yang, Yuandong Tian, Yangyang Shi, Vikas Chandra, Jürgen Schmidhuber</span>
        <span class="paper-meta">Updated 2026-04-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We propose a new frontier: Neural Computers (NCs) -- an emerging machine form that unifies computation, memory, and I/O in a learned runtime state. Unlike conventional computers, which execute explicit programs, agents, which act over external execution environments, and world models, which learn environment dynamics, NCs aim to make the model itself the running computer. Our long-term goal is the Completely Neural Computer (CNC): the mature, general-purpose realization of this emerging machine form, with stable execution, explicit reprogramming, and durable capability reuse. As an initial step, we study whether early NC primitives can be learned solely from collected I/O traces, without instrumented program state. Concretely, we instantiate NCs as video models that roll out screen frames from instructions, pixels, and user actions (when available) in CLI and GUI settings. These implementations show that learned runtimes can acquire early interface primitives, especially I/O alignment and short-horizon control, while routine reuse, controlled updates, and symbolic stability remain open. We outline a roadmap toward CNCs around these challenges. If overcome, CNCs could establish a new computing paradigm beyond today&#x27;s agents, world models, and conventional computers.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.06425">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.06425.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.06425.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Evolution of Video Generative Foundations</span>
        <span class="paper-authors">Teng Hu, Jiangning Zhang, Hongrui Huang, Ran Yi, Zihan Su, Jieyu Weng, Zhucun Xue, Lizhuang Ma, Ming-Hsuan Yang, Dacheng Tao</span>
        <span class="paper-meta">Updated 2026-04-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">The rapid advancement of Artificial Intelligence Generated Content (AIGC) has revolutionized video generation, enabling systems ranging from proprietary pioneers like OpenAI&#x27;s Sora, Google&#x27;s Veo3, and Bytedance&#x27;s Seedance to powerful open-source contenders like Wan and HunyuanVideo to synthesize temporally coherent and semantically rich videos. These advancements pave the way for building &quot;world models&quot; that simulate real-world dynamics, with applications spanning entertainment, education, and virtual reality. However, existing reviews on video generation often focus on narrow technical fields, e.g., Generative Adversarial Networks (GAN) and diffusion models, or specific tasks (e. g., video editing), lacking a comprehensive perspective on the field&#x27;s evolution, especially regarding Auto-Regressive (AR) models and integration of multimodal information. To address these gaps, this survey firstly provides a systematic review of the development of video generation technology, tracing its evolution from early GANs to dominant diffusion models, and further to emerging AR-based and multimodal techniques. We conduct an in-depth analysis of the foundational principles, key advancements, and comparative strengths/limitations. Then, we explore emerging trends in multimodal video generation, emphasizing the integration of diverse data types to enhance contextual awareness. Finally, by bridging historical developments and contemporary innovations, this survey offers insights to guide future research in video generation and its applications, including virtual/augmented reality, personalized education, autonomous driving simulations, digital entertainment, and advanced world models, in this rapidly evolving field. For more details, please refer to the project at https://github.com/sjtuplayer/Awesome-Video-Foundations.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.06339">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.06339.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.06339.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Action Images: End-to-End Policy Learning via Multiview Video Generation</span>
        <span class="paper-authors">Haoyu Zhen, Zixian Gao, Qiao Sun, Yilin Zhao, Yuncong Yang, Yilun Du, Tsun-Hsuan Wang, Yi-Ling Qiao, Chuang Gan</span>
        <span class="paper-meta">Updated 2026-04-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">World action models (WAMs) have emerged as a promising direction for robot policy learning, as they can leverage powerful video backbones to model the future states. However, existing approaches often rely on separate action modules, or use action representations that are not pixel-grounded, making it difficult to fully exploit the pretrained knowledge of video models and limiting transfer across viewpoints and environments. In this work, we present Action Images, a unified world action model that formulates policy learning as multiview video generation. Instead of encoding control as low-dimensional tokens, we translate 7-DoF robot actions into interpretable action images: multi-view action videos that are grounded in 2D pixels and explicitly track robot-arm motion. This pixel-grounded action representation allows the video backbone itself to act as a zero-shot policy, without a separate policy head or action module. Beyond control, the same unified model supports video-action joint generation, action-conditioned video generation, and action labeling under a shared representation. On RLBench and real-world evaluations, our model achieves the strongest zero-shot success rates and improves video-action joint generation quality over prior video-space world models, suggesting that interpretable action images are a promising route to policy learning.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.06168">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.06168.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.06168.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
</section>
