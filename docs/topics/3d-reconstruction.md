---
layout: default
title: 3D Reconstruction
---

<section class="topic-hero" style="--accent: #7c3aed;">
  <div>
    <p class="eyebrow">Topic</p>
    <h1>3D Reconstruction</h1>
    <p class="topic-lede">Updated 2026.04.09 · 327 papers</p>
  </div>
  <a class="btn ghost" href="../index.html#topics">← Back to topics</a>
</section>

<section class="paper-grid">
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Fast Spatial Memory with Elastic Test-Time Training</span>
        <span class="paper-authors">Ziqiao Ma, Xueyang Yu, Haoyu Zhen, Yuncong Yang, Joyce Chai, Chuang Gan</span>
        <span class="paper-meta">Updated 2026-04-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Large Chunk Test-Time Training (LaCT) has shown strong performance on long-context 3D reconstruction, but its fully plastic inference-time updates remain vulnerable to catastrophic forgetting and overfitting. As a result, LaCT is typically instantiated with a single large chunk spanning the full input sequence, falling short of the broader goal of handling arbitrarily long sequences in a single pass. We propose Elastic Test-Time Training inspired by elastic weight consolidation, that stabilizes LaCT fast-weight updates with a Fisher-weighted elastic prior around a maintained anchor state. The anchor evolves as an exponential moving average of past fast weights to balance stability and plasticity. Based on this updated architecture, we introduce Fast Spatial Memory (FSM), an efficient and scalable model for 4D reconstruction that learns spatiotemporal representations from long observation sequences and renders novel view-time combinations. We pre-trained FSM on large-scale curated 3D/4D data to capture the dynamics and semantics of complex spatial environments. Extensive experiments show that FSM supports fast adaptation over long sequences and delivers high-quality 3D/4D reconstruction with smaller chunks and mitigating the camera-interpolation shortcut. Overall, we hope to advance LaCT beyond the bounded single-chunk setting toward robust multi-chunk adaptation, a necessary step for generalization to genuinely longer sequences, while substantially alleviating the activation-memory bottleneck.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.07350">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.07350.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.07350.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Mem3R: Streaming 3D Reconstruction with Hybrid Memory via Test-Time Training</span>
        <span class="paper-authors">Changkun Liu, Jiezhi Yang, Zeman Li, Yuan Deng, Jiancong Guo, Luca Ballan</span>
        <span class="paper-meta">Updated 2026-04-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Streaming 3D perception is well suited to robotics and augmented reality, where long visual streams must be processed efficiently and consistently. Recent recurrent models offer a promising solution by maintaining fixed-size states and enabling linear-time inference, but they often suffer from drift accumulation and temporal forgetting over long sequences due to the limited capacity of compressed latent memories. We propose Mem3R, a streaming 3D reconstruction model with a hybrid memory design that decouples camera tracking from geometric mapping to improve temporal consistency over long sequences. For camera tracking, Mem3R employs an implicit fast-weight memory implemented as a lightweight Multi-Layer Perceptron updated via Test-Time Training. For geometric mapping, Mem3R maintains an explicit token-based fixed-size state. Compared with CUT3R, this design not only significantly improves long-sequence performance but also reduces the model size from 793M to 644M parameters. Mem3R supports existing improved plug-and-play state update strategies developed for CUT3R. Specifically, integrating it with TTT3R decreases Absolute Trajectory Error by up to 39% over the base implementation on 500 to 1000 frame sequences. The resulting improvements also extend to other downstream tasks, including video depth estimation and 3D reconstruction, while preserving constant GPU memory usage and comparable inference throughput. Project page: https://lck666666.github.io/Mem3R/</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.07279">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.07279.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.07279.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Enhancing MLLM Spatial Understanding via Active 3D Scene Exploration for Multi-Perspective Reasoning</span>
        <span class="paper-authors">Jiahua Chen, Qihong Tang, Weinong Wang, Qi Fan</span>
        <span class="paper-meta">Updated 2026-04-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Although Multimodal Large Language Models have achieved remarkable progress, they still struggle with complex 3D spatial reasoning due to the reliance on 2D visual priors. Existing approaches typically mitigate this limitation either through computationally expensive post-training procedures on limited 3D datasets or through rigid tool-calling mechanisms that lack explicit geometric understanding and viewpoint flexibility. To address these challenges, we propose a \textit{training-free} framework that introduces a Visual Chain-of-Thought mechanism grounded in explicit 3D reconstruction. The proposed pipeline first reconstructs a high-fidelity 3D mesh from a single image using MLLM-guided keyword extraction and mask generation at multiple granularities. Subsequently, the framework leverages an external knowledge base to iteratively compute optimal camera extrinsic parameters and synthesize novel views, thereby emulating human perspective-taking. Extensive experiments demonstrate that the proposed approach significantly enhances spatial comprehension. Specifically, the framework outperforms specialized spatial models and general-purpose MLLMs, including \textit{GPT-5.2} and \textit{Gemini-2.5-Flash}, on major benchmarks such as 3DSRBench and Rel3D.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.06725">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.06725.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.06725.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Human Interaction-Aware 3D Reconstruction from a Single Image</span>
        <span class="paper-authors">Gwanghyun Kim, Junghun James Kim, Suh Yoon Jeon, Jason Park, Se Young Chun</span>
        <span class="paper-meta">Updated 2026-04-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Reconstructing textured 3D human models from a single image is fundamental for AR/VR and digital human applications. However, existing methods mostly focus on single individuals and thus fail in multi-human scenes, where naive composition of individual reconstructions often leads to artifacts such as unrealistic overlaps, missing geometry in occluded regions, and distorted interactions. These limitations highlight the need for approaches that incorporate group-level context and interaction priors. We introduce a holistic method that explicitly models both group- and instance-level information. To mitigate perspective-induced geometric distortions, we first transform the input into a canonical orthographic space. Our primary component, Human Group-Instance Multi-View Diffusion (HUG-MVD), then generates complete multi-view normals and images by jointly modeling individuals and group context to resolve occlusions and proximity. Subsequently, the Human Group-Instance Geometric Reconstruction (HUG-GR) module optimizes the geometry by leveraging explicit, physics-based interaction priors to enforce physical plausibility and accurately model inter-human contact. Finally, the multi-view images are fused into a high-fidelity texture. Together, these components form our complete framework, HUG3D. Extensive experiments show that HUG3D significantly outperforms both single-human and existing multi-human methods, producing physically plausible, high-fidelity 3D reconstructions of interacting people from a single image. Project page: https://jongheean11.github.io/HUG3D_project</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.05436">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.05436.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.05436.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">3DTurboQuant: Training-Free Near-Optimal Quantization for 3D Reconstruction Models</span>
        <span class="paper-authors">Jae Joong Lee</span>
        <span class="paper-meta">Updated 2026-04-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Every existing method for compressing 3D Gaussian Splatting, NeRF, or transformer-based 3D reconstructors requires learning a data-dependent codebook through per-scene fine-tuning. We show this is unnecessary. The parameter vectors that dominate storage in these models, 45-dimensional spherical harmonics in 3DGS and 1024-dimensional key-value vectors in DUSt3R, fall in a dimension range where a single random rotation transforms any input into coordinates with a known Beta distribution. This makes precomputed, data-independent Lloyd-Max quantization near-optimal, within a factor of 2.7 of the information-theoretic lower bound. We develop 3D, deriving (1) a dimension-dependent criterion that predicts which parameters can be quantized and at what bit-width before running any experiment, (2) norm-separation bounds connecting quantization MSE to rendering PSNR per scene, (3) an entry-grouping strategy extending rotation-based quantization to 2-dimensional hash grid features, and (4) a composable pruning-quantization pipeline with a closed-form compression ratio. On NeRF Synthetic, 3DTurboQuant compresses 3DGS by 3.5x with 0.02dB PSNR loss and DUSt3R KV caches by 7.9x with 39.7dB pointmap fidelity. No training, no codebook learning, no calibration data. Compression takes seconds. The code will be released (https://github.com/JaeLee18/3DTurboQuant)</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.05366">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.05366.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.05366.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SmokeGS-R: Physics-Guided Pseudo-Clean 3DGS for Real-World Multi-View Smoke Restoration</span>
        <span class="paper-authors">Xueming Fu, Lixia Han</span>
        <span class="paper-meta">Updated 2026-04-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Real-world smoke simultaneously attenuates scene radiance, adds airlight, and destabilizes multi-view appearance consistency, making robust 3D reconstruction particularly difficult. We present \textbf{SmokeGS-R}, a practical pipeline developed for the NTIRE 2026 3D Restoration and Reconstruction Track 2 challenge. The key idea is to decouple geometry recovery from appearance correction: we generate physics-guided pseudo-clean supervision with a refined dark channel prior and guided filtering, train a sharp clean-only 3D Gaussian Splatting source model, and then harmonize its renderings with a donor ensemble using geometric-mean reference aggregation, LAB-space Reinhard transfer, and light Gaussian smoothing. On the official challenge testing leaderboard, the final submission achieved \mbox{PSNR $=15.217$} and \mbox{SSIM $=0.666$}. After the public release of RealX3D, we re-evaluated the same frozen result on the seven released challenge scenes without retraining and obtained \mbox{PSNR $=15.209$}, \mbox{SSIM $=0.644$}, and \mbox{LPIPS $=0.551$}, outperforming the strongest official baseline average on the same scenes by $+3.68$ dB PSNR. These results suggest that a geometry-first reconstruction strategy combined with stable post-render appearance harmonization is an effective recipe for real-world multi-view smoke restoration. The code is available at https://github.com/windrise/3drr_Track2_SmokeGS-R.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.05301">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.05301.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.05301.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Coverage Optimization for Camera View Selection</span>
        <span class="paper-authors">Timothy Chen, Adam Dai, Maximilian Adang, Grace Gao, Mac Schwager</span>
        <span class="paper-meta">Updated 2026-04-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">What makes a good viewpoint? The quality of the data used to learn 3D reconstructions is crucial for enabling efficient and accurate scene modeling. We study the active view selection problem and develop a principled analysis that yields a simple and interpretable criterion for selecting informative camera poses. Our key insight is that informative views can be obtained by minimizing a tractable approximation of the Fisher Information Gain, which reduces to favoring viewpoints that cover geometry that has been insufficiently observed by past cameras. This leads to a lightweight coverage-based view selection metric that avoids expensive transmittance estimation and is robust to noise and training dynamics. We call this metric COVER (Camera Optimization for View Exploration and Reconstruction). We integrate our method into the Nerfstudio framework and evaluate it on real datasets within fixed and embodied data acquisition scenarios. Across multiple datasets and radiance-field baselines, our method consistently improves reconstruction quality compared to state-of-the-art active view selection methods. Additional visualizations and our Nerfstudio package can be found at https://chengine.github.io/nbv_gym/.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.05259">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.05259.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.05259.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LSRM: High-Fidelity Object-Centric Reconstruction via Scaled Context Windows</span>
        <span class="paper-authors">Zhengqin Li, Cheng Zhang, Jakob Engel, Zhao Dong</span>
        <span class="paper-meta">Updated 2026-04-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We introduce the Large Sparse Reconstruction Model to study how scaling transformer context windows impacts feed-forward 3D reconstruction. Although recent object-centric feed-forward methods deliver robust, high-quality reconstruction, they still lag behind dense-view optimization in recovering fine-grained texture and appearance. We show that expanding the context window -- by substantially increasing the number of active object and image tokens -- remarkably narrows this gap and enables high-fidelity 3D object reconstruction and inverse rendering. To scale effectively, we adapt native sparse attention in our architecture design, unlocking its capacity for 3D reconstruction with three key contributions: (1) an efficient coarse-to-fine pipeline that focuses computation on informative regions by predicting sparse high-resolution residuals; (2) a 3D-aware spatial routing mechanism that establishes accurate 2D-3D correspondences using explicit geometric distances rather than standard attention scores; and (3) a custom block-aware sequence parallelism strategy utilizing an All-gather-KV protocol to balance dynamic, sparse workloads across GPUs. As a result, LSRM handles 20x more object tokens and &gt;2x more image tokens than prior state-of-the-art (SOTA) methods. Extensive evaluations on standard novel-view synthesis benchmarks show substantial gains over the current SOTA, yielding 2.5 dB higher PSNR and 40% lower LPIPS. Furthermore, when extending LSRM to inverse rendering tasks, qualitative and quantitative evaluations on widely-used benchmarks demonstrate consistent improvements in texture and geometry details, achieving an LPIPS that matches or exceeds that of SOTA dense-view optimization methods. Code and model will be released on our project page.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.05182">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.05182.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.05182.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LoMa: Local Feature Matching Revisited</span>
        <span class="paper-authors">David Nordström, Johan Edstedt, Georg Bökman, Jonathan Astermark, Anders Heyden, Viktor Larsson, Mårten Wadenbäck, Michael Felsberg, Fredrik Kahl</span>
        <span class="paper-meta">Updated 2026-04-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Local feature matching has long been a fundamental component of 3D vision systems such as Structure-from-Motion (SfM), yet progress has lagged behind the rapid advances of modern data-driven approaches. The newer approaches, such as feed-forward reconstruction models, have benefited extensively from scaling dataset sizes, whereas local feature matching models are still only trained on a few mid-sized datasets. In this paper, we revisit local feature matching from a data-driven perspective. In our approach, which we call LoMa, we combine large and diverse data mixtures, modern training recipes, scaled model capacity, and scaled compute, resulting in remarkable gains in performance. Since current standard benchmarks mainly rely on collecting sparse views from successful 3D reconstructions, the evaluation of progress in feature matching has been limited to relatively easy image pairs. To address the resulting saturation of benchmarks, we collect 1000 highly challenging image pairs from internet data into a new dataset called HardMatch. Ground truth correspondences for HardMatch are obtained via manual annotation by the authors. In our extensive benchmarking suite, we find that LoMa makes outstanding progress across the board, outperforming the state-of-the-art method ALIKED+LightGlue by +18.6 mAA on HardMatch, +29.5 mAA on WxBS, +21.4 (1m, 10$^\circ$) on InLoc, +24.2 AUC on RUBIK, and +12.4 mAA on IMC 2022. We release our code and models publicly at https://github.com/davnords/LoMa.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.04931">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.04931.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.04931.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">3D Gaussian Splatting for Annular Dark Field Scanning Transmission Electron Microscopy Tomography Reconstruction</span>
        <span class="paper-authors">Beiyuan Zhang, Hesong Li, Ruiwen Shao, Ying Fu</span>
        <span class="paper-meta">Updated 2026-04-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Analytical Dark Field Scanning Transmission Electron Microscopy (ADF-STEM) tomography reconstructs nanoscale materials in 3D by integrating multi-view tilt-series images, enabling precise analysis of their structural and compositional features. Although integrating more tilt views improves 3D reconstruction, it requires extended electron exposure that risks damaging dose-sensitive materials and introduces drift and misalignment, making it difficult to balance reconstruction fidelity with sample preservation. In practice, sparse-view acquisition is frequently required, yet conventional ADF-STEM methods degrade under limited views, exhibiting artifacts and reduced structural fidelity. To resolve these issues, in this paper, we adapt 3D GS to this domain with three key components. We first model the local scattering strength as a learnable scalar field, denza, to address the mismatch between 3DGS and ADF-STEM imaging physics. Then we introduce a coefficient $γ$ to stabilize scattering across tilt angles, ensuring consistent denza via scattering view normalization. Finally, We incorporate a loss function that includes a 2D Fourier amplitude term to suppress missing wedge artifacts in sparse-view reconstruction. Experiments on 45-view and 15-view tilt series show that DenZa-Gaussian produces high-fidelity reconstructions and 2D projections that align more closely with original tilts, demonstrating superior robustness under sparse-view conditions.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.04693">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.04693.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.04693.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">TerraSky3D: Multi-View Reconstructions of European Landmarks in 4K</span>
        <span class="paper-authors">Mattia D&#x27;Urso, Yuxi Hu, Christian Sormann, Mattia Rossi, Friedrich Fraundorfer</span>
        <span class="paper-meta">Updated 2026-03-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Despite the growing need for data of more and more sophisticated 3D reconstruction pipelines, we can still observe a scarcity of suitable public datasets. Existing 3D datasets are either low resolution, limited to a small amount of scenes, based on images of varying quality because retrieved from the internet, or limited to specific capturing scenarios.   Motivated by this lack of suitable 3D datasets, we captured TerraSky3D, a high-resolution large-scale 3D reconstruction dataset comprising 50,000 images divided into 150 ground, aerial, and mixed scenes. The dataset focuses on European landmarks and comes with curated calibration data, camera poses, and depth maps. TerraSky3D tries to answer the need for challenging dataset that can be used to train and evaluate 3D reconstruction-related pipelines.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.28287">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.28287.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.28287.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MV-RoMa: From Pairwise Matching into Multi-View Track Reconstruction</span>
        <span class="paper-authors">Jongmin Lee, Seungyeop Kang, Sungjoo Yoo</span>
        <span class="paper-meta">Updated 2026-03-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Establishing consistent correspondences across images is essential for 3D vision tasks such as structure-from-motion (SfM), yet most existing matchers operate in a pairwise manner, often producing fragmented and geometrically inconsistent tracks when their predictions are chained across views. We propose MV-RoMa, a multi-view dense matching model that jointly estimates dense correspondences from a source image to multiple co-visible targets. Specifically, we design an efficient model architecture which avoids high computational cost of full cross-attention for multi-view feature interaction: (i) multi-view encoder that leverages pair-wise matching results as a geometric prior, and (ii) multi-view matching refiner that refines correspondences using pixel-wise attention. Additionally, we propose a post-processing strategy that integrates our model&#x27;s consistent multi-view correspondences as high-quality tracks for SfM. Across diverse and challenging benchmarks, MV-RoMa produces more reliable correspondences and substantially denser, more accurate 3D reconstructions than existing sparse and dense matching methods. Project page: https://icetea-cv.github.io/mv-roma/.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.27542">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.27542.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.27542.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">From None to All: Self-Supervised 3D Reconstruction via Novel View Synthesis</span>
        <span class="paper-authors">Ranran Huang, Weixun Luo, Ye Mao, Krystian Mikolajczyk</span>
        <span class="paper-meta">Updated 2026-03-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">In this paper, we introduce NAS3R, a self-supervised feed-forward framework that jointly learns explicit 3D geometry and camera parameters with no ground-truth annotations and no pretrained priors. During training, NAS3R reconstructs 3D Gaussians from uncalibrated and unposed context views and renders target views using its self-predicted camera parameters, enabling self-supervised training from 2D photometric supervision. To ensure stable convergence, NAS3R integrates reconstruction and camera prediction within a shared transformer backbone regulated by masked attention, and adopts a depth-based Gaussian formulation that facilitates well-conditioned optimization. The framework is compatible with state-of-the-art supervised 3D reconstruction architectures and can incorporate pretrained priors or intrinsic information when available. Extensive experiments show that NAS3R achieves superior results to other self-supervised methods, establishing a scalable and geometry-aware paradigm for 3D reconstruction from unconstrained data. Code and models are publicly available at https://ranrhuang.github.io/nas3r/.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.27455">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.27455.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.27455.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">HD-VGGT: High-Resolution Visual Geometry Transformer</span>
        <span class="paper-authors">Tianrun Chen, Yuanqi Hu, Yidong Han, Hanjie Xu, Deyi Ji, Qi Zhu, Chunan Yu, Xin Zhang, Cheng Chen, Chaotao Ding, Ying Zang, Xuanfu Li, Jin Ma, Lanyun Zhu</span>
        <span class="paper-meta">Updated 2026-03-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">High-resolution imagery is essential for accurate 3D reconstruction, as many geometric details only emerge at fine spatial scales. Recent feed-forward approaches, such as the Visual Geometry Grounded Transformer (VGGT), have demonstrated the ability to infer scene geometry from large collections of images in a single forward pass. However, scaling these models to high-resolution inputs remains challenging: the number of tokens in transformer architectures grows rapidly with both image resolution and the number of views, leading to prohibitive computational and memory costs. Moreover, we observe that visually ambiguous regions, such as repetitive patterns, weak textures, or specular surfaces, often produce unstable feature tokens that degrade geometric inference, especially at higher resolutions. We introduce HD-VGGT, a dual-branch architecture for efficient and robust high-resolution 3D reconstruction. A low-resolution branch predicts a coarse, globally consistent geometry, while a high-resolution branch refines details via a learned feature upsampling module. To handle unstable tokens, we propose Feature Modulation, which suppresses unreliable features early in the transformer. HD-VGGT leverages high-resolution images and supervision without full-resolution transformer costs, achieving state-of-the-art reconstruction quality.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.27222">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.27222.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.27222.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SceneExpander: Expanding 3D Scenes with Free-Form Inserted Views</span>
        <span class="paper-authors">Zijian He, enjie Liu, Yihao Wang, Weizhi Zhong, Huan Yuan, Kun Gai, Guangrun Wang, Guanbin Li</span>
        <span class="paper-meta">Updated 2026-03-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">World building with 3D scene representations is increasingly important for content creation, simulation, and interactive experiences, yet real workflows are inherently iterative: creators must repeatedly extend an existing scene under user control. Motivated by this research gap, we study 3D scene expansion in a user-centric workflow: starting from a real scene captured by multi-view images, we extend its coverage by inserting an additional view synthesized by a generative model. Unlike simple object editing or style transfer in a fixed scene, the inserted view is often 3D-misaligned with the original reconstruction, introducing geometry shifts, hallucinated content, or view-dependent artifacts that break global multi-view consistency. To address the challenge, we propose SceneExpander, which applies test-time adaptation to a parametric feed-forward 3D reconstruction model with two complementary distillation signals: anchor distillation stabilizes the original scene by distilling geometric cues from the captured views, while inserted-view self-distillation preserves observation-supported predictions yet adapts latent geometry and appearance to accommodate the misaligned inserted view. Experiments on ETH scenes and online data demonstrate improved expansion behavior and reconstruction quality under misalignment.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.27084">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.27084.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.27084.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Drive-Through 3D Vehicle Exterior Reconstruction via Dynamic-Scene SfM and Distortion-Aware Gaussian Splatting</span>
        <span class="paper-authors">Nitin Kulkarni, Akhil Devarashetti, Charlie Cluss, Livio Forte, Philip Schneider, Chunming Qiao, Alina Vereshchaka</span>
        <span class="paper-meta">Updated 2026-03-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">High-fidelity 3D reconstruction of vehicle exteriors improves buyer confidence in online automotive marketplaces, but generating these models in cluttered dealership drive-throughs presents severe technical challenges. Unlike static-scene photogrammetry, this setting features a dynamic vehicle moving against heavily cluttered, static backgrounds. This problem is further compounded by wide-angle lens distortion, specular automotive paint, and non-rigid wheel rotations that violate classical epipolar constraints. We propose an end-to-end pipeline utilizing a two-pillar camera rig. First, we resolve dynamic-scene ambiguities by coupling SAM 3 for instance segmentation with motion-gating to cleanly isolate the moving vehicle, explicitly masking out non-rigid wheels to enforce strict epipolar geometry. Second, we extract robust correspondences directly on raw, distorted 4K imagery using the RoMa v2 learned matcher guided by semantic confidence masks. Third, these matches are integrated into a rig-aware SfM optimization that utilizes CAD-derived relative pose priors to eliminate scale drift. Finally, we use a distortion-aware 3D Gaussian Splatting framework (3DGUT) coupled with a stochastic Markov Chain Monte Carlo (MCMC) densification strategy to render reflective surfaces. Evaluations on 25 real-world vehicles across 10 dealerships demonstrate that our full pipeline achieves a PSNR of 28.66 dB, an SSIM of 0.89, and an LPIPS of 0.21 on held-out views, representing a 3.85 dB improvement over standard 3D-GS, delivering inspection-grade interactive 3D models without controlled studio infrastructure.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.26638">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.26638.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.26638.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Scene Grounding In the Wild</span>
        <span class="paper-authors">Tamir Cohen, Leo Segre, Shay Shomer-Chai, Shai Avidan, Hadar Averbuch-Elor</span>
        <span class="paper-meta">Updated 2026-03-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Reconstructing accurate 3D models of large-scale real-world scenes from unstructured, in-the-wild imagery remains a core challenge in computer vision, especially when the input views have little or no overlap. In such cases, existing reconstruction pipelines often produce multiple disconnected partial reconstructions or erroneously merge non-overlapping regions into overlapping geometry. In this work, we propose a framework that grounds each partial reconstruction to a complete reference model of the scene, enabling globally consistent alignment even in the absence of visual overlap. We obtain reference models from dense, geospatially accurate pseudo-synthetic renderings derived from Google Earth Studio. These renderings provide full scene coverage but differ substantially in appearance from real-world photographs. Our key insight is that, despite this significant domain gap, both domains share the same underlying scene semantics. We represent the reference model using 3D Gaussian Splatting, augmenting each Gaussian with semantic features, and formulate alignment as an inverse feature-based optimization scheme that estimates a global 6DoF pose and scale while keeping the reference model fixed. Furthermore, we introduce the WikiEarth dataset, which registers existing partial 3D reconstructions with pseudo-synthetic reference models. We demonstrate that our approach consistently improves global alignment when initialized with various classical and learning-based pipelines, while mitigating failure modes of state-of-the-art end-to-end models. All code and data will be released.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.26584">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.26584.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.26584.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Conditional Diffusion for 3D CT Volume Reconstruction from 2D X-rays</span>
        <span class="paper-authors">Martin Rath, Morteza Ghahremani, Yitong Li, Ashkan Taghipour, Marcus Makowski, Christian Wachinger</span>
        <span class="paper-meta">Updated 2026-03-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Computed tomography (CT) provides rich 3D anatomical details but is often constrained by high radiation exposure, substantial costs, and limited availability. While standard chest X-rays are cost-effective and widely accessible, they only provide 2D projections with limited pathological information. Reconstructing 3D CT volumes from 2D X-rays offers a transformative solution to increase diagnostic accessibility, yet existing methods predominantly rely on synthetic X-ray projections, limiting clinical generalization. In this work, we propose AXON, a multi-stage diffusion-based framework that reconstructs high-fidelity 3D CT volumes directly from real X-rays. AXON employs a coarse-to-fine strategy, with a Brownian Bridge diffusion model-based initial stage for global structural synthesis, followed by a ControlNet-based refinement stage for local intensity optimization. It also supports bi-planar X-ray input to mitigate depth ambiguities inherent in 2D-to-3D reconstruction. A super-resolution network is integrated to upscale the generated volumes to achieve diagnostic-grade resolution. Evaluations on both public and external datasets demonstrate that AXON significantly outperforms state-of-the-art baselines, achieving a 11.9% improvement in PSNR and a 11.0% increase in SSIM with robust generalizability across disparate clinical distributions. Our code is available at https://github.com/ai-med/AXON.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.26509">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.26509.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.26509.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FAST3DIS: Feed-forward Anchored Scene Transformer for 3D Instance Segmentation</span>
        <span class="paper-authors">Changyang Li, Xueqing Huang, Shin-Fang Chng, Huangying Zhan, Qingan Yan, Yi Xu</span>
        <span class="paper-meta">Updated 2026-03-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">While recent feed-forward 3D reconstruction models provide a strong geometric foundation for scene understanding, extending them to 3D instance segmentation typically relies on a disjointed &quot;lift-and-cluster&quot; paradigm. Grouping dense pixel-wise embeddings via non-differentiable clustering scales poorly with the number of views and disconnects representation learning from the final segmentation objective. In this paper, we present a Feed-forward Anchored Scene Transformer for 3D Instance Segmentation (FAST3DIS), an end-to-end approach that effectively bypasses post-hoc clustering. We introduce a 3D-anchored, query-based Transformer architecture built upon a foundational depth backbone, adapted efficiently to learn instance-specific semantics while retaining its zero-shot geometric priors. We formulate a learned 3D anchor generator coupled with an anchor-sampling cross-attention mechanism for view-consistent 3D instance segmentation. By projecting 3D object queries directly into multi-view feature maps, our method samples context efficiently. Furthermore, we introduce a dual-level regularization strategy, that couples multi-view contrastive learning with a dynamically scheduled spatial overlap penalty to explicitly prevent query collisions and ensure precise instance boundaries. Experiments on complex indoor 3D datasets demonstrate that our approach achieves competitive segmentation accuracy with significantly improved memory scalability and inference speed over state-of-the-art clustering-based methods.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.25993">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.25993.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.25993.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Geo$^\textbf{2}$: Geometry-Guided Cross-view Geo-Localization and Image Synthesis</span>
        <span class="paper-authors">Yancheng Zhang, Xiaohan Zhang, Guangyu Sun, Zonglin Lyu, Safwan Wshah, Chen Chen</span>
        <span class="paper-meta">Updated 2026-03-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Cross-view geo-spatial learning consists of two important tasks: Cross-View Geo-Localization (CVGL) and Cross-View Image Synthesis (CVIS), both of which rely on establishing geometric correspondences between ground and aerial views. Recent Geometric Foundation Models (GFMs) have demonstrated strong capabilities in extracting generalizable 3D geometric features from images, but their potential in cross-view geo-spatial tasks remains underexplored. In this work, we present Geo^2, a unified framework that leverages Geometric priors from GFMs (e.g., VGGT) to jointly perform geo-spatial tasks, CVGL and bidirectional CVIS. Despite the 3D reconstruction ability of GFMs, directly applying them to CVGL and CVIS remains challenging due to the large viewpoint gap between ground and aerial imagery. We propose GeoMap, which embeds ground and aerial features into a shared 3D-aware latent space, effectively reducing cross-view discrepancies for localization. This shared latent space naturally bridges cross-view image synthesis in both directions. To exploit this, we propose GeoFlow, a flow-matching model conditioned on geometry-aware latent embeddings. We further introduce a consistency loss to enforce latent alignment between the two synthesis directions, ensuring bidirectional coherence. Extensive experiments on standard benchmarks, including CVUSA, CVACT, and VIGOR, demonstrate that Geo^2 achieves state-of-the-art performance in both localization and synthesis, highlighting the effectiveness of 3D geometric priors for cross-view geo-spatial learning.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.25819">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.25819.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.25819.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SLAT-Phys: Fast Material Property Field Prediction from Structured 3D Latents</span>
        <span class="paper-authors">Rocktim Jyoti Das, Dinesh Manocha</span>
        <span class="paper-meta">Updated 2026-03-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Estimating the material property field of 3D assets is critical for physics-based simulation, robotics, and digital twin generation. Existing vision-based approaches are either too expensive and slow or rely on 3D information. We present SLAT-Phys, an end-to-end method that predicts spatially varying material property fields of 3D assets directly from a single RGB image without explicit 3D reconstruction. Our approach leverages spatially organised latent features from a pretrained 3D asset generation model that encodes rich geometry and semantic prior, and trains a lightweight neural decoder to estimate Young&#x27;s modulus, density, and Poisson&#x27;s ratio. The coarse volumetric layout and semantic cues of the latent representation about object geometry and appearance enable accurate material estimation. Our experiments demonstrate that our method provides competitive accuracy in predicting continuous material parameters when compared against prior approaches, while significantly reducing computation time. In particular, SLAT-Phys requires only 9.9 seconds per object on an NVIDIA RTXA5000 GPU and avoids reconstruction and voxelization preprocessing. This results in 120x speedup compared to prior methods and enables faster material property estimation from a single image.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.23973">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.23973.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.23973.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">AdvSplat: Adversarial Attacks on Feed-Forward Gaussian Splatting Models</span>
        <span class="paper-authors">Yiran Qiao, Yiren Lu, Yunlai Zhou, Rui Yang, Linlin Hou, Yu Yin, Jing Ma</span>
        <span class="paper-meta">Updated 2026-03-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">3D Gaussian Splatting (3DGS) is increasingly recognized as a powerful paradigm for real-time, high-fidelity 3D reconstruction. However, its per-scene optimization pipeline limits scalability and generalization, and prevents efficient inference. Recently emerged feed-forward 3DGS models address these limitations by enabling fast reconstruction from a few input views after large-scale pretraining, without scene-specific optimization. Despite their advantages and strong potential for commercial deployment, the use of neural networks as the backbone also amplifies the risk of adversarial manipulation. In this paper, we introduce AdvSplat, the first systematic study of adversarial attacks on feed-forward 3DGS. We first employ white-box attacks to reveal fundamental vulnerabilities of this model family. We then develop two improved, practically relevant, query-efficient black-box algorithms that optimize pixel-space perturbations via a frequency-domain parameterization: one based on gradient estimation and the other gradient-free, without requiring any access to model internals. Extensive experiments across multiple datasets demonstrate that AdvSplat can significantly disrupt reconstruction results by injecting imperceptible perturbations into the input images. Our findings surface an overlooked yet urgent problem in this domain, and we hope to draw the community&#x27;s attention to this emerging security and robustness challenge.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.23686">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.23686.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.23686.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">I3DM: Implicit 3D-aware Memory Retrieval and Injection for Consistent Video Scene Generation</span>
        <span class="paper-authors">Jia Li, Han Yan, Yihang Chen, Siqi Li, Xibin Song, Yifu Wang, Jianfei Cai, Tien-Tsin Wong, Pan Ji</span>
        <span class="paper-meta">Updated 2026-03-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Despite remarkable progress in video generation, maintaining long-term scene consistency upon revisiting previously explored areas remains challenging. Existing solutions rely either on explicitly constructing 3D geometry, which suffers from error accumulation and scale ambiguity, or on naive camera Field-of-View (FoV) retrieval, which typically fails under complex occlusions. To overcome these limitations, we propose I3DM, a novel implicit 3D-aware memory mechanism for consistent video scene generation that bypasses explicit 3D reconstruction. At the core of our approach is a 3D-aware memory retrieval strategy, which leverages the intermediate features of a pre-trained Feed-Forward Novel View Synthesis (FF-NVS) model to score view relevance, enabling robust retrieval even in highly occluded scenarios. Furthermore, to fully utilize the retrieved historical frames, we introduce a 3D-aligned memory injection module. This module implicitly warps historical content to the target view and adaptively conditions the generation on reliable warping regions, leading to improved revisit consistency and accurate camera control. Extensive experiments demonstrate that our method outperforms state-of-the-art approaches, achieving superior revisit consistency, generation fidelity, and camera control precision.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.23413">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.23413.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.23413.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GO-Renderer: Generative Object Rendering with 3D-aware Controllable Video Diffusion Models</span>
        <span class="paper-authors">Zekai Gu, Shuoxuan Feng, Yansong Wang, Hanzhuo Huang, Zhongshuo Du, Chengfeng Zhao, Chengwei Ren, Peng Wang, Yuan Liu</span>
        <span class="paper-meta">Updated 2026-03-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Reconstructing a renderable 3D model from images is a useful but challenging task. Recent feedforward 3D reconstruction methods have demonstrated remarkable success in efficiently recovering geometry, but still cannot accurately model the complex appearances of these 3D reconstructed models. Recent diffusion-based generative models can synthesize realistic images or videos of an object using reference images without explicitly modeling its appearance, which provides a promising direction for object rendering, but lacks accurate control over the viewpoints. In this paper, we propose GO-Renderer, a unified framework integrating the reconstructed 3D proxies to guide the video generative models to achieve high-quality object rendering on arbitrary viewpoints under arbitrary lighting conditions. Our method not only enjoys the accurate viewpoint control using the reconstructed 3D proxy but also enables high-quality rendering in different lighting environments using diffusion generative models without explicitly modeling complex materials and lighting. Extensive experiments demonstrate that GO-Renderer achieves state-of-the-art performance across the object rendering tasks, including synthesizing images on new viewpoints, rendering the objects in a novel lighting environment, and inserting an object into an existing video.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.23246">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.23246.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.23246.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GTLR-GS: Geometry-Texture Aware LiDAR-Regularized 3D Gaussian Splatting for Realistic Scene Reconstruction</span>
        <span class="paper-authors">Yan Fang, Jianfei Ge, Jiangjian Xiao</span>
        <span class="paper-meta">Updated 2026-03-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Recent advances in 3D Gaussian Splatting (3DGS) have enabled real-time, photorealistic scene reconstruction. However, conventional 3DGS frameworks typically rely on sparse point clouds derived from Structure-from-Motion (SfM), which inherently suffer from scale ambiguity, limited geometric consistency, and strong view dependency due to the lack of geometric priors. In this work, a LiDAR-centric 3D Gaussian Splatting framework is proposed that explicitly incorporates metric geometric priors into the entire Gaussian optimization process. Instead of treating LiDAR data as a passive initialization source, 3DGS optimization is reformulated as a geometry-conditioned allocation and refinement problem under a fixed representational budget. Specifically, this work introduces (i) a geometry-texture-aware allocation strategy that selectively assigns Gaussian primitives to regions with high structural or appearance complexity, (ii) a curvature-adaptive refinement mechanism that dynamically guides Gaussian splitting toward geometrically complex areas during training, and (iii) a confidence-aware metric depth regularization that anchors the reconstructed geometry to absolute scale using LiDAR measurements while maintaining optimization stability. Extensive experiments on the ScanNet++ dataset and a custom real-world dataset validate the proposed approach. The results demonstrate state-of-the-art performance in metric-scale reconstruction with high geometric fidelity.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.23192">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.23192.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.23192.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">UniQueR: Unified Query-based Feedforward 3D Reconstruction</span>
        <span class="paper-authors">Chensheng Peng, Quentin Herau, Jiezhi Yang, Yichen Xie, Yihan Hu, Wenzhao Zheng, Matthew Strong, Masayoshi Tomizuka, Wei Zhan</span>
        <span class="paper-meta">Updated 2026-03-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We present UniQueR, a unified query-based feedforward framework for efficient and accurate 3D reconstruction from unposed images. Existing feedforward models such as DUSt3R, VGGT, and AnySplat typically predict per-pixel point maps or pixel-aligned Gaussians, which remain fundamentally 2.5D and limited to visible surfaces. In contrast, UniQueR formulates reconstruction as a sparse 3D query inference problem. Our model learns a compact set of 3D anchor points that act as explicit geometric queries, enabling the network to infer scene structure, including geometry in occluded regions--in a single forward pass. Each query encodes spatial and appearance priors directly in global 3D space (instead of per-frame camera space) and spawns a set of 3D Gaussians for differentiable rendering. By leveraging unified query interactions across multi-view features and a decoupled cross-attention design, UniQueR achieves strong geometric expressiveness while substantially reducing memory and computational cost. Experiments on Mip-NeRF 360 and VR-NeRF demonstrate that UniQueR surpasses state-of-the-art feedforward methods in both rendering quality and geometric accuracy, using an order of magnitude fewer primitives than dense alternatives.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.22851">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.22851.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.22851.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">CAM3R: Camera-Agnostic Model for 3D Reconstruction</span>
        <span class="paper-authors">Namitha Guruprasad, Abhay Yadav, Cheng Peng, Rama Chellappa</span>
        <span class="paper-meta">Updated 2026-03-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Recovering dense 3D geometry from unposed images remains a foundational challenge in computer vision. Current state-of-the-art models are predominantly trained on perspective datasets, which implicitly constrains them to a standard pinhole camera geometry. As a result, these models suffer from significant geometric degradation when applied to wide-angle imagery captured via non-rectilinear optics, such as fisheye or panoramic sensors. To address this, we present CAM3R, a Camera-Agnostic, feed-forward Model for 3D Reconstruction capable of processing images from wide-angle camera models without prior calibration. Our framework consists of a two-view network which is bifurcated into a Ray Module (RM) to estimate per-pixel ray directions and a Cross-view Module (CVM) to infer radial distance with confidence maps, pointmaps, and relative poses. To unify these pairwise predictions into a consistent 3D scene, we introduce a Ray-Aware Global Alignment framework for pose refinement and scale optimization while strictly preserving the predicted local geometry. Extensive experiments on various camera model datasets, including panorama, fisheye and pinhole imagery, demonstrate that CAM3R establishes a new state-of-the-art in pose estimation and reconstruction.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.22631">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.22631.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.22631.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FullCircle: Effortless 3D Reconstruction from Casual 360$^\circ$ Captures</span>
        <span class="paper-authors">Yalda Foroutan, Ipek Oztas, Daniel Rebain, Aysegul Dundar, Kwang Moo Yi, Lily Goli, Andrea Tagliasacchi</span>
        <span class="paper-meta">Updated 2026-03-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Radiance fields have emerged as powerful tools for 3D scene reconstruction. However, casual capture remains challenging due to the narrow field of view of perspective cameras, which limits viewpoint coverage and feature correspondences necessary for reliable camera calibration and reconstruction. While commercially available 360$^\circ$ cameras offer significantly broader coverage than perspective cameras for the same capture effort, existing 360$^\circ$ reconstruction methods require special capture protocols and pre-processing steps that undermine the promise of radiance fields: effortless workflows to capture and reconstruct 3D scenes. We propose a practical pipeline for reconstructing 3D scenes directly from raw 360$^\circ$ camera captures. We require no special capture protocols or pre-processing, and exhibit robustness to a prevalent source of reconstruction errors: the human operator that is visible in all 360$^\circ$ imagery. To facilitate evaluation, we introduce a multi-tiered dataset of scenes captured as raw dual-fisheye images, establishing a benchmark for robust casual 360$^\circ$ reconstruction. Our method significantly outperforms not only vanilla 3DGS for 360$^\circ$ cameras but also robust perspective baselines when perspective cameras are simulated from the same capture, demonstrating the advantages of 360$^\circ$ capture for casual reconstruction. Additional results are available at: https://theialab.github.io/fullcircle</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.22572">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.22572.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.22572.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">UrbanVGGT: Scalable Sidewalk Width Estimation from Street View Images</span>
        <span class="paper-authors">Kaizhen Tan, Fan Zhang</span>
        <span class="paper-meta">Updated 2026-03-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Sidewalk width is an important indicator of pedestrian accessibility, comfort, and network quality, yet large-scale width data remain scarce in most cities. Existing approaches typically rely on costly field surveys, high-resolution overhead imagery, or simplified geometric assumptions that limit scalability or introduce systematic error. To address this gap, we present UrbanVGGT, a measurement pipeline for estimating metric sidewalk width from a single street-view image. The method combines semantic segmentation, feed-forward 3D reconstruction, adaptive ground-plane fitting, camera-height-based scale calibration, and directional width measurement on the recovered plane. On a ground-truth benchmark from Washington, D.C., UrbanVGGT achieves a mean absolute error of 0.252 m, with 95.5% of estimates within 0.50 m of the reference width. Ablation experiments show that metric scale calibration is the most critical component, and controlled comparisons with alternative geometry backbones support the effectiveness of the overall design. As a feasibility demonstration, we further apply the pipeline to three cities and generate SV-SideWidth, a prototype sidewalk-width dataset covering 527 OpenStreetMap street segments. The results indicate that street-view imagery can support scalable generation of candidate sidewalk-width attributes, while broader cross-city validation and local ground-truth auditing remain necessary before deployment as authoritative planning data.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.22531">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.22531.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.22531.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Static Scene Reconstruction from Dynamic Egocentric Videos</span>
        <span class="paper-authors">Qifei Cui, Patrick Chen</span>
        <span class="paper-meta">Updated 2026-03-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Egocentric videos present unique challenges for 3D reconstruction due to rapid camera motion and frequent dynamic interactions. State-of-the-art static reconstruction systems, such as MapAnything, often degrade in these settings, suffering from catastrophic trajectory drift and &quot;ghost&quot; geometry caused by moving hands. We bridge this gap by proposing a robust pipeline that adapts static reconstruction backbones to long-form egocentric video. Our approach introduces a mask-aware reconstruction mechanism that explicitly suppresses dynamic foreground in the attention layers, preventing hand artifacts from contaminating the static map. Furthermore, we employ a chunked reconstruction strategy with pose-graph stitching to ensure global consistency and eliminate long-term drift. Experiments on HD-EPIC and indoor drone datasets demonstrate that our pipeline significantly improves absolute trajectory error and yields visually clean static geometry compared to naive baselines, effectively extending the capability of foundation models to dynamic first-person scenes.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.22450">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.22450.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.22450.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MonoArt: Progressive Structural Reasoning for Monocular Articulated 3D Reconstruction</span>
        <span class="paper-authors">Haitian Li, Haozhe Xie, Junxiang Xu, Beichen Wen, Fangzhou Hong, Ziwei Liu</span>
        <span class="paper-meta">Updated 2026-03-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Reconstructing articulated 3D objects from a single image requires jointly inferring object geometry, part structure, and motion parameters from limited visual evidence. A key difficulty lies in the entanglement between motion cues and object structure, which makes direct articulation regression unstable. Existing methods address this challenge through multi-view supervision, retrieval-based assembly, or auxiliary video generation, often sacrificing scalability or efficiency. We present MonoArt, a unified framework grounded in progressive structural reasoning. Rather than predicting articulation directly from image features, MonoArt progressively transforms visual observations into canonical geometry, structured part representations, and motion-aware embeddings within a single architecture. This structured reasoning process enables stable and interpretable articulation inference without external motion templates or multi-stage pipelines. Extensive experiments on PartNet-Mobility demonstrate that OM achieves state-of-the-art performance in both reconstruction accuracy and inference speed. The framework further generalizes to robotic manipulation and articulated scene reconstruction.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.19231">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.19231.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.19231.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Reconstruction Matters: Learning Geometry-Aligned BEV Representation through 3D Gaussian Splatting</span>
        <span class="paper-authors">Yiren Lu, Xin Ye, Burhaneddin Yaman, Jingru Luo, Zhexiao Xiong, Liu Ren, Yu Yin</span>
        <span class="paper-meta">Updated 2026-03-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Bird&#x27;s-Eye-View (BEV) perception serves as a cornerstone for autonomous driving, offering a unified spatial representation that fuses surrounding-view images to enable reasoning for various downstream tasks, such as semantic segmentation, 3D object detection, and motion prediction. However, most existing BEV perception frameworks adopt an end-to-end training paradigm, where image features are directly transformed into the BEV space and optimized solely through downstream task supervision. This formulation treats the entire perception process as a black box, often lacking explicit 3D geometric understanding and interpretability, leading to suboptimal performance. In this paper, we claim that an explicit 3D representation matters for accurate BEV perception, and we propose Splat2BEV, a Gaussian Splatting-assisted framework for BEV tasks. Splat2BEV aims to learn BEV feature representations that are both semantically rich and geometrically precise. We first pre-train a Gaussian generator that explicitly reconstructs 3D scenes from multi-view inputs, enabling the generation of geometry-aligned feature representations. These representations are then projected into the BEV space to serve as inputs for downstream tasks. Extensive experiments on nuScenes and argoverse dataset demonstrate that Splat2BEV achieves state-of-the-art performance and validate the effectiveness of incorporating explicit 3D reconstruction into BEV perception.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.19193">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.19193.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.19193.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">VGGT-360: Geometry-Consistent Zero-Shot Panoramic Depth Estimation</span>
        <span class="paper-authors">Jiayi Yuan, Haobo Jiang, De Wen Soh, Na Zhao</span>
        <span class="paper-meta">Updated 2026-03-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">This paper presents VGGT-360, a novel training-free framework for zero-shot, geometry-consistent panoramic depth estimation. Unlike prior view-independent training-free approaches, VGGT-360 reformulates the task as panoramic reprojection over multi-view reconstructed 3D models by leveraging the intrinsic 3D consistency of VGGT-like foundation models, thereby unifying fragmented per-view reasoning into a coherent panoramic understanding. To achieve robust and accurate estimation, VGGT-360 integrates three plug-and-play modules that form a unified panorama-to-3D-to-depth framework: (i) Uncertainty-guided adaptive projection slices panoramas into perspective views to bridge the domain gap between panoramic inputs and VGGT&#x27;s perspective prior. It estimates gradient-based uncertainty to allocate denser views to geometry-poor regions, yielding geometry-informative inputs for VGGT. (ii) Structure-saliency enhanced attention strengthens VGGT&#x27;s robustness during 3D reconstruction by injecting structure-aware confidence into its attention layers, guiding focus toward geometrically reliable regions and enhancing cross-view coherence. (iii) Correlation-weighted 3D model correction refines the reconstructed 3D model by reweighting overlapping points using attention-inferred correlation scores, providing a consistent geometric basis for accurate panoramic reprojection. Extensive experiments show that VGGT-360 outperforms both trained and training-free state-of-the-art methods across multiple resolutions and diverse indoor and outdoor datasets.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.18943">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.18943.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.18943.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GHOST: Fast Category-agnostic Hand-Object Interaction Reconstruction from RGB Videos using Gaussian Splatting</span>
        <span class="paper-authors">Ahmed Tawfik Aboukhadra, Marcel Rogge, Nadia Robertini, Abdalla Arafa, Jameel Malik, Ahmed Elhayek, Didier Stricker</span>
        <span class="paper-meta">Updated 2026-03-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Understanding realistic hand-object interactions from monocular RGB videos is essential for AR/VR, robotics, and embodied AI. Existing methods rely on category-specific templates or heavy computation, yet still produce physically inconsistent hand-object alignment in 3D. We introduce GHOST (Gaussian Hand-Object Splatting), a fast, category-agnostic framework for reconstructing dynamic hand-object interactions using 2D Gaussian Splatting. GHOST represents both hands and objects as dense, view-consistent Gaussian discs and introduces three key innovations: (1) a geometric-prior retrieval and consistency loss that completes occluded object regions, (2) a grasp-aware alignment that refines hand translations and object scale to ensure realistic contact, and (3) a hand-aware background loss that prevents penalizing hand-occluded object regions. GHOST achieves complete, physically consistent, and animatable reconstructions from a single RGB video while running an order of magnitude faster than prior category-agnostic methods. Extensive experiments on ARCTIC, HO3D, and in-the-wild datasets demonstrate state-of-the-art accuracy in 3D reconstruction and 2D rendering quality, establishing GHOST as an efficient and robust solution for realistic hand-object interaction modeling. Code is available at https://github.com/ATAboukhadra/GHOST.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.18912">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.18912.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.18912.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SEAR: Simple and Efficient Adaptation of Visual Geometric Transformers for RGB+Thermal 3D Reconstruction</span>
        <span class="paper-authors">Vsevolod Skorokhodov, Chenghao Xu, Shuo Sun, Olga Fink, Malcolm Mielle</span>
        <span class="paper-meta">Updated 2026-03-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Foundational feed-forward visual geometry models enable accurate and efficient camera pose estimation and scene reconstruction by learning strong scene priors from massive RGB datasets. However, their effectiveness drops when applied to mixed sensing modalities, such as RGB-thermal (RGB-T) images. We observe that while a visual geometry grounded transformer pretrained on RGB data generalizes well to thermal-only reconstruction, it struggles to align RGB and thermal modalities when processed jointly. To address this, we propose SEAR, a simple yet efficient fine-tuning strategy that adapts a pretrained geometry transformer to multimodal RGB-T inputs. Despite being trained on a relatively small RGB-T dataset, our approach significantly outperforms state-of-the-art methods for 3D reconstruction and camera pose estimation, achieving significant improvements over all metrics (e.g., over 29\% in AUC@30) and delivering higher detail and consistency between modalities with negligible overhead in inference time compared to the original pretrained model. Notably, SEAR enables reliable multimodal pose estimation and reconstruction even under challenging conditions, such as low lighting and dense smoke. We validate our architecture through extensive ablation studies, demonstrating how the model aligns both modalities. Additionally, we introduce a new dataset featuring RGB and thermal sequences captured at different times, viewpoints, and illumination conditions, providing a robust benchmark for future work in multimodal 3D scene reconstruction. Code and models are publicly available at https://www.github.com/Schindler-EPFL-Lab/SEAR.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.18774">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.18774.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.18774.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SwiftGS: Episodic Priors for Immediate Satellite Surface Recovery</span>
        <span class="paper-authors">Rong Fu, Jiekai Wu, Haiyun Wei, Xiaowen Ma, Shiyin Lin, Kangan Qian, Chuang Liu, Jianyuan Ni, Simon James Fong</span>
        <span class="paper-meta">Updated 2026-03-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Rapid, large-scale 3D reconstruction from multi-date satellite imagery is vital for environmental monitoring, urban planning, and disaster response, yet remains difficult due to illumination changes, sensor heterogeneity, and the cost of per-scene optimization. We introduce SwiftGS, a meta-learned system that reconstructs 3D surfaces in a single forward pass by predicting geometry-radiation-decoupled Gaussian primitives together with a lightweight SDF, replacing expensive per-scene fitting with episodic training that captures transferable priors. The model couples a differentiable physics graph for projection, illumination, and sensor response with spatial gating that blends sparse Gaussian detail and global SDF structure, and incorporates semantic-geometric fusion, conditional lightweight task heads, and multi-view supervision from a frozen geometric teacher under an uncertainty-aware multi-task loss. At inference, SwiftGS operates zero-shot with optional compact calibration and achieves accurate DSM reconstruction and view-consistent rendering at significantly reduced computational cost, with ablations highlighting the benefits of the hybrid representation, physics-aware rendering, and episodic meta-training.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.18634">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.18634.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.18634.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FILT3R: Latent State Adaptive Kalman Filter for Streaming 3D Reconstruction</span>
        <span class="paper-authors">Seonghyun Jin, Jong Chul Ye</span>
        <span class="paper-meta">Updated 2026-03-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Streaming 3D reconstruction maintains a persistent latent state that is updated online from incoming frames, enabling constant-memory inference. A key failure mode is the state update rule: aggressive overwrites forget useful history, while conservative updates fail to track new evidence, and both behaviors become unstable beyond the training horizon. To address this challenge, we propose FILT3R, a training-free latent filtering layer that casts recurrent state updates as stochastic state estimation in token space. FILT3R maintains a per-token variance and computes a Kalman-style gain that adaptively balances memory retention against new observations. Process noise -- governing how much the latent state is expected to change between frames -- is estimated online from EMA-normalized temporal drift of candidate tokens. Using extensive experiments, we demonstrate that FILT3R yields an interpretable, plug-in update rule that generalizes common overwrite and gating policies as special cases. Specifically, we show that gains shrink in stable regimes as uncertainty contracts with accumulated evidence, and rise when genuine scene change increases process uncertainty, improving long-horizon stability for depth, pose, and 3D reconstruction, compared to the existing methods. Code will be released at https://github.com/jinotter3/FILT3R.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.18493">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.18493.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.18493.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Fast and Generalizable NeRF Architecture Selection for Satellite Scene Reconstruction</span>
        <span class="paper-authors">Devjyoti Chakraborty, Zaki Sukma, Rakandhiya D. Rachmanto, Kriti Ghosh, In Kee Kim, Suchendra M. Bhandarkar, Lakshmish Ramaswamy, Nancy K. O&#x27;Hare, Deepak Mishra</span>
        <span class="paper-meta">Updated 2026-03-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Neural Radiance Fields (NeRF) have emerged as a powerful approach for photorealistic 3D reconstruction from multi-view images. However, deploying NeRF for satellite imagery remains challenging. Each scene requires individual training, and optimizing architectures via Neural Architecture Search (NAS) demands hours to days of GPU time. While existing approaches focus on architectural improvements, our SHAP analysis reveals that multi-view consistency, rather than model architecture, determines reconstruction quality. Based on this insight, we develop PreSCAN, a predictive framework that estimates NeRF quality prior to training using lightweight geometric and photometric descriptors. PreSCAN selects suitable architectures in &lt; 30 seconds with &lt; 1 dB prediction error, achieving 1000$\times$ speedup over NAS. We further demonstrate PreSCAN&#x27;s deployment utility on edge platforms (Jetson Orin), where combining its predictions with offline cost profiling reduces inference power by 26% and latency by 43% with minimal quality loss. Experiments on DFC2019 datasets confirm that PreSCAN generalizes across diverse satellite scenes without retraining.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.18306">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.18306.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.18306.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">TAPESTRY: From Geometry to Appearance via Consistent Turntable Videos</span>
        <span class="paper-authors">Yan Zeng, Haoran Jiang, Kaixin Yao, Qixuan Zhang, Longwen Zhang, Lan Xu, Jingyi Yu</span>
        <span class="paper-meta">Updated 2026-03-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Automatically generating photorealistic and self-consistent appearances for untextured 3D models is a critical challenge in digital content creation. The advancement of large-scale video generation models offers a natural approach: directly synthesizing 360-degree turntable videos (TTVs), which can serve not only as high-quality dynamic previews but also as an intermediate representation to drive texture synthesis and neural rendering. However, existing general-purpose video diffusion models struggle to maintain strict geometric consistency and appearance stability across the full range of views, making their outputs ill-suited for high-quality 3D reconstruction. To this end, we introduce TAPESTRY, a framework for generating high-fidelity TTVs conditioned on explicit 3D geometry. We reframe the 3D appearance generation task as a geometry-conditioned video diffusion problem: given a 3D mesh, we first render and encode multi-modal geometric features to constrain the video generation process with pixel-level precision, thereby enabling the creation of high-quality and consistent TTVs. Building upon this, we also design a method for downstream reconstruction tasks from the TTV input, featuring a multi-stage pipeline with 3D-Aware Inpainting. By rotating the model and performing a context-aware secondary generation, this pipeline effectively completes self-occluded regions to achieve full surface coverage. The videos generated by TAPESTRY are not only high-quality dynamic previews but also serve as a reliable, 3D-aware intermediate representation that can be seamlessly back-projected into UV textures or used to supervise neural rendering methods like 3DGS. This enables the automated creation of production-ready, complete 3D assets from untextured meshes. Experimental results demonstrate that our method outperforms existing approaches in both video consistency and final reconstruction quality.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.17735">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.17735.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.17735.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">PanoVGGT: Feed-Forward 3D Reconstruction from Panoramic Imagery</span>
        <span class="paper-authors">Yijing Guo, Mengjun Chao, Luo Wang, Tianyang Zhao, Haizhao Dai, Yingliang Zhang, Jingyi Yu, Yujiao Shi</span>
        <span class="paper-meta">Updated 2026-03-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Panoramic imagery offers a full 360° field of view and is increasingly common in consumer devices. However, it introduces non-pinhole distortions that challenge joint pose estimation and 3D reconstruction. Existing feed-forward models, built for perspective cameras, generalize poorly to this setting. We propose PanoVGGT, a permutation-equivariant Transformer framework that jointly predicts camera poses, depth maps, and 3D point clouds from one or multiple panoramas in a single forward pass. The model incorporates spherical-aware positional embeddings and a panorama-specific three-axis SO(3) rotation augmentation, enabling effective geometric reasoning in the spherical domain. To resolve inherent global-frame ambiguity, we further introduce a stochastic anchoring strategy during training. In addition, we contribute PanoCity, a large-scale outdoor panoramic dataset with dense depth and 6-DoF pose annotations. Extensive experiments on PanoCity and standard benchmarks demonstrate that PanoVGGT achieves competitive accuracy, strong robustness, and improved cross-domain generalization. Code and dataset will be released.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.17571">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.17571.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.17571.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Towards Spatio-Temporal World Scene Graph Generation from Monocular Videos</span>
        <span class="paper-authors">Rohith Peddi, Saurabh, Shravan Shanmugam, Likhitha Pallapothula, Yu Xiang, Parag Singla, Vibhav Gogate</span>
        <span class="paper-meta">Updated 2026-03-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Spatio-temporal scene graphs provide a principled representation for modeling evolving object interactions, yet existing methods remain fundamentally frame-centric: they reason only about currently visible objects, discard entities upon occlusion, and operate in 2D. To address this, we first introduce ActionGenome4D, a dataset that upgrades Action Genome videos into 4D scenes via feed-forward 3D reconstruction, world-frame oriented bounding boxes for every object involved in actions, and dense relationship annotations including for objects that are temporarily unobserved due to occlusion or camera motion. Building on this data, we formalize World Scene Graph Generation (WSGG), the task of constructing a world scene graph at each timestamp that encompasses all interacting objects in the scene, both observed and unobserved. We then propose three complementary methods, each exploring a different inductive bias for reasoning about unobserved objects: PWG (Persistent World Graph), which implements object permanence via a zero-order feature buffer; MWAE (Masked World Auto-Encoder), which reframes unobserved-object reasoning as masked completion with cross-view associative retrieval; and 4DST (4D Scene Transformer), which replaces the static buffer with differentiable per-object temporal attention enriched by 3D motion and camera-pose features. We further design and evaluate the performance of strong open-source Vision-Language Models on the WSGG task via a suite of Graph RAG-based approaches, establishing baselines for unlocalized relationship prediction. WSGG thus advances video scene understanding toward world-centric, temporally persistent, and interpretable scene reasoning.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.13185">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.13185.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.13185.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">3DTCR: A Physics-Based Generative Framework for Vortex-Following 3D Reconstruction to Improve Tropical Cyclone Intensity Forecasting</span>
        <span class="paper-authors">Jun Liu, Xiaohui Zhong, Kai Zheng, Jiarui Li, Yifei Li, Tao Zhou, Wenxu Qian, Shun Dai, Ruian Tie, Yangyang Zhao, Hao Li</span>
        <span class="paper-meta">Updated 2026-03-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Tropical cyclone (TC) intensity forecasting remains challenging as current numerical and AI-based weather models fail to satisfactorily represent extreme TC structure and intensity. Although intensity time-series forecasting has achieved significant advances, it outputs intensity sequences rather than the three-dimensional inner-core fine-scale structure and physical mechanisms governing TC evolution. High-resolution numerical simulations can capture these features but remain computationally expensive and inefficient for large-scale operational applications. Here we present 3DTCR, a physics-based generative framework combining physical constraints with generative AI efficiency for 3D TC structure reconstruction. Trained on a six-year, 3-km-resolution moving-domain WRF dataset, 3DTCR enables region-adaptive vortex-following reconstruction using conditional Flow Matching(CFM), optimized via latent domain adaptation and two-stage transfer learning. The framework mitigates limitations imposed by low-resolution targets and over-smoothed forecasts, improving the representation of TC inner-core structure and intensity while maintaining track stability. Results demonstrate that 3DTCR outperforms the ECMWF high-resolution forecasting system (ECMWF-HRES) in TC intensity prediction at nearly all lead times up to 5 days and reduces the RMSE of maximum WS10M by 36.5\% relative to its FuXi inputs. These findings highlight 3DTCR as a physics-based generative framework that efficiently resolves fine-scale structures at lower computational cost, which may offer a promising avenue for improving TC intensity forecasting.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.13049">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.13049.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.13049.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">CMHANet: A Cross-Modal Hybrid Attention Network for Point Cloud Registration</span>
        <span class="paper-authors">Dongxu Zhang, Yingsen Wang, Yiding Sun, Haoran Xu, Peilin Fan, Jihua Zhu</span>
        <span class="paper-meta">Updated 2026-03-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Robust point cloud registration is a fundamental task in 3D computer vision and geometric deep learning, essential for applications such as large-scale 3D reconstruction, augmented reality, and scene understanding. However, the performance of established learning-based methods often degrades in complex, real world scenarios characterized by incomplete data, sensor noise, and low overlap regions. To address these limitations, we propose CMHANet, a novel Cross-Modal Hybrid Attention Network. Our method integrates the fusion of rich contextual information from 2D images with the geometric detail of 3D point clouds, yielding a comprehensive and resilient feature representation. Furthermore, we introduce an innovative optimization function based on contrastive learning, which enforces geometric consistency and significantly improves the model&#x27;s robustness to noise and partial observations. We evaluated CMHANet on the 3DMatch and the challenging 3DLoMatch datasets. \rev{Additionally, zero-shot evaluations on the TUM RGB-D SLAM dataset verify the model&#x27;s generalization capability to unseen domains.} The experimental results demonstrate that our method achieves substantial improvements in both registration accuracy and overall robustness, outperforming current techniques. We also release our code in \href{https://github.com/DongXu-Zhang/CMHANet}{https://github.com/DongXu-Zhang/CMHANet}.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.12721">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.12721.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.12721.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Marker-Based 3D Reconstruction of Aggregates with a Comparative Analysis of 2D and 3D Morphologies</span>
        <span class="paper-authors">Haohang Huang, Jiayi Luo, Issam Qamhia, Erol Tutumluer, John M. Hart, Andrew J. Stolba</span>
        <span class="paper-meta">Updated 2026-03-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Aggregates, serving as the main skeleton in assemblies of construction materials, are important functional components in various building and transportation infrastructures. They can be used in unbound layer applications, e.g. pavement base and railroad ballast, bound applications of cement concrete and asphalt concrete, and as riprap and large-sized primary crushed rocks. Information on the size and shape or morphology of aggregates can greatly facilitate the Quality Assurance/Quality Control (QA/QC) process by providing insights of aggregate behavior during composition and packing. A full 3D characterization of aggregate particle morphology is difficult both during production in a quarry and at a construction site. Many aggregate imaging approaches have been developed to quantify the particle morphology by computer vision, including 2D image-based approaches that analyze particle silhouettes and 3D scanning-based methods that require expensive devices such as 3D laser scanners or X-Ray Computed Tomography (CT) equipment. This paper presents a flexible and cost-effective photogrammetry-based approach for the 3D reconstruction of aggregate particles. The proposed approach follows a marker-based design that enables background suppression, point cloud stitching, and scale referencing to obtain high-quality aggregate models. The accuracy of the reconstruction results was validated against ground-truth for selected aggregate samples. Comparative analyses were conducted on 2D and 3D morphological properties of the selected samples. Significant differences were found between the 2D and 3D statistics. Based on the presented approach, 3D shape information of aggregates can be obtained easily and at a low cost, thus allowing convenient aggregate inspection, data collection, and 3D morphological analysis.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.12667">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.12667.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.12667.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Single-View Rolling-Shutter SfM</span>
        <span class="paper-authors">Sofía Errázuriz Muñoz, Kim Kiehn, Petr Hruby, Kathlén Kohn</span>
        <span class="paper-meta">Updated 2026-03-12</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Rolling-shutter (RS) cameras are ubiquitous, but RS SfM (structure-from-motion) has not been fully solved yet. This work suggests an approach to remedy this: We characterize RS single-view geometry of observed world points or lines. Exploiting this geometry, we describe which motion and scene parameters can be recovered from a single RS image and systematically derive minimal reconstruction problems. We evaluate several representative cases with proof-of-concept solvers, highlighting both feasibility and practical limitations.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.11888">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.11888.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.11888.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">CEI-3D: Collaborative Explicit-Implicit 3D Reconstruction for Realistic and Fine-Grained Object Editing</span>
        <span class="paper-authors">Yue Shi, Rui Shi, Yuxuan Xiong, Bingbing Ni, Wenjun Zhang</span>
        <span class="paper-meta">Updated 2026-03-12</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Existing 3D editing methods often produce unrealistic and unrefined results due to the deeply integrated nature of their reconstruction networks. To address the challenge, this paper introduces CEI-3D, an editing-oriented reconstruction pipeline designed to facilitate realistic and fine-grained editing. Specifically, we propose a collaborative explicit-implicit reconstruction approach, which represents the target object using an implicit SDF network and a differentially sampled, locally controllable set of handler points. The implicit network provides a smooth and continuous geometry prior, while the explicit handler points offer localized control, enabling mutual guidance between the global 3D structure and user-specified local editing regions. To independently control each attribute of the handler points, we design a physical properties disentangling module to decouple the color of the handler points into separate physical properties. We also propose a dual-diffuse-albedo network in this module to process the edited and non-edited regions through separate branches, thereby preventing undesired interference from editing operations. Building on the reconstructed collaborative explicit-implicit representation with disentangled properties, we introduce a spatial-aware editing module that enables part-wise adjustment of relevant handler points. This module employs a cross-view propagation-based 3D segmentation strategy, which helps users to edit the specified physical attributes of a target part efficiently. Extensive experiments on both real and synthetic datasets demonstrate that our approach achieves more realistic and fine-grained editing results than the state-of-the-art (SOTA) methods while requiring less editing time. Our code is available on https://github.com/shiyue001/CEI-3D.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.11810">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.11810.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.11810.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">High-Precision 6DOF Pose Estimation via Global Phase Retrieval in Fringe Projection Profilometry for 3D Mapping</span>
        <span class="paper-authors">Sehoon Tak, Keunhee Cho, Sangpil Kim, Jae-Sang Hyun</span>
        <span class="paper-meta">Updated 2026-03-12</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Digital fringe projection (DFP) enables micrometer-level 3D reconstruction, yet extending it to large-scale mapping remains challenging because six-degree-of-freedom pose estimation often cannot match the reconstruction&#x27;s precision. Conventional iterative closest point (ICP) registration becomes inefficient on multi-million-point clouds and typically relies on downsampling or feature-based selection, which can reduce local detail and degrade pose precision. Drift-correction methods improve long-term consistency but do not resolve sampling sensitivity in dense DFP point clouds.We propose a high-precision pose estimation method that augments a moving DFP system with a fixed, intrinsically calibrated global projector. Using the global projector&#x27;s phase-derived pixel constraints and a PnP-style reprojection objective, the method estimates the DFP system pose in a fixed reference frame without relying on deterministic feature extraction, and we experimentally demonstrate sampling invariance under coordinate-preserving subsampling. Experiments demonstrate sub-millimeter pose accuracy against a reference with quantified uncertainty bounds, high repeatability under aggressive subsampling, robust operation on homogeneous surfaces and low-overlap views, and reduced error accumulation when used to correct ICP-based trajectories. The method extends DFP toward accurate 3D mapping in quasi-static scenarios such as inspection and metrology, with the trade-off of time-multiplexed acquisition for the additional projector measurements.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.11389">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.11389.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.11389.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">InstantHDR: Single-forward Gaussian Splatting for High Dynamic Range 3D Reconstruction</span>
        <span class="paper-authors">Dingqiang Ye, Jiacong Xu, Jianglu Ping, Yuxiang Guo, Chao Fan, Vishal M. Patel</span>
        <span class="paper-meta">Updated 2026-03-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">High dynamic range (HDR) novel view synthesis (NVS) aims to reconstruct HDR scenes from multi-exposure low dynamic range (LDR) images. Existing HDR pipelines heavily rely on known camera poses, well-initialized dense point clouds, and time-consuming per-scene optimization. Current feed-forward alternatives overlook the HDR problem by assuming exposure-invariant appearance. To bridge this gap, we propose InstantHDR, a feed-forward network that reconstructs 3D HDR scenes from uncalibrated multi-exposure LDR collections in a single forward pass. Specifically, we design a geometry-guided appearance modeling for multi-exposure fusion, and a meta-network for generalizable scene-specific tone mapping. Due to the lack of HDR scene data, we build a pre-training dataset, called HDR-Pretrain, for generalizable feed-forward HDR models, featuring 168 Blender-rendered scenes, diverse lighting types, and multiple camera response functions. Comprehensive experiments show that our InstantHDR delivers comparable synthesis performance to the state-of-the-art optimization-based HDR methods while enjoying $\sim700\times$ and $\sim20\times$ reconstruction speed improvement with our single-forward and post-optimization settings. All code, models, and datasets will be released after the review process.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.11298">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.11298.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.11298.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GGPT: Geometry Grounded Point Transformer</span>
        <span class="paper-authors">Yutong Chen, Yiming Wang, Xucong Zhang, Sergey Prokudin, Siyu Tang</span>
        <span class="paper-meta">Updated 2026-03-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Recent feed-forward networks have achieved remarkable progress in sparse-view 3D reconstruction by predicting dense point maps directly from RGB images. However, they often suffer from geometric inconsistencies and limited fine-grained accuracy due to the absence of explicit multi-view constraints. We introduce the Geometry-Grounded Point Transformer (GGPT), a framework that augments feed-forward reconstruction with reliable sparse geometric guidance. We first propose an improved Structure-from-Motion pipeline based on dense feature matching and lightweight geometric optimisation to efficiently estimate accurate camera poses and partial 3D point clouds from sparse input views. Building on this foundation, we propose a geometry-guided 3D point transformer that refines dense point maps under explicit partial-geometry supervision using an optimised guidance encoding. Extensive experiments demonstrate that our method provides a principled mechanism for integrating geometric priors with dense feed-forward predictions, producing reconstructions that are both geometrically consistent and spatially complete, recovering fine structures and filling gaps in textureless areas. Trained solely on ScanNet++ with VGGT predictions, GGPT generalises across architectures and datasets, substantially outperforming state-of-the-art feed-forward 3D reconstruction models in both in-domain and out-of-domain settings.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.11174">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.11174.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.11174.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Neural Field Thermal Tomography: A Differentiable Physics Framework for Non-Destructive Evaluation</span>
        <span class="paper-authors">Tao Zhong, Yixun Hu, Dongzhe Zheng, Aditya Sood, Christine Allen-Blanchette</span>
        <span class="paper-meta">Updated 2026-03-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We propose Neural Field Thermal Tomography (NeFTY), a differentiable physics framework for the quantitative 3D reconstruction of material properties from transient surface temperature measurements. While traditional thermography relies on pixel-wise 1D approximations that neglect lateral diffusion, and soft-constrained Physics-Informed Neural Networks (PINNs) often fail in transient diffusion scenarios due to gradient stiffness, NeFTY parameterizes the 3D diffusivity field as a continuous neural field optimized through a rigorous numerical solver. By leveraging a differentiable physics solver, our approach enforces thermodynamic laws as hard constraints while maintaining the memory efficiency required for high-resolution 3D tomography. Our discretize-then-optimize paradigm effectively mitigates the spectral bias and ill-posedness inherent in inverse heat conduction, enabling the recovery of subsurface defects at arbitrary scales. Experimental validation on synthetic data demonstrates that NeFTY significantly improves the accuracy of subsurface defect localization over baselines. Additional details at https://cab-lab-princeton.github.io/nefty/</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.11045">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.11045.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.11045.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">NLiPsCalib: An Efficient Calibration Framework for High-Fidelity 3D Reconstruction of Curved Visuotactile Sensors</span>
        <span class="paper-authors">Xuhao Qin, Feiyu Zhao, Yatao Leng, Runze Hu, Chenxi Xiao</span>
        <span class="paper-meta">Updated 2026-03-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Recent advances in visuotactile sensors increasingly employ biomimetic curved surfaces to enhance sensorimotor capabilities. Although such curved visuotactile sensors enable more conformal object contact, their perceptual quality is often degraded by non-uniform illumination, which reduces reconstruction accuracy and typically necessitates calibration. Existing calibration methods commonly rely on customized indenters and specialized devices to collect large-scale photometric data, but these processes are expensive and labor-intensive. To overcome these calibration challenges, we present NLiPsCalib, a physics-consistent and efficient calibration framework for curved visuotactile sensors. NLiPsCalib integrates controllable near-field light sources and leverages Near-Light Photometric Stereo (NLiPs) to estimate contact geometry, simplifying calibration to just a few simple contacts with everyday objects. We further introduce NLiPsTac, a controllable-light-source tactile sensor developed to validate our framework. Experimental results demonstrate that our approach enables high-fidelity 3D reconstruction across diverse curved form factors with a simple calibration procedure. We emphasize that our approach lowers the barrier to developing customized visuotactile sensors of diverse geometries, thereby making visuotactile sensing more accessible to the broader community.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.09319">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.09319.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.09319.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Implicit Geometry Representations for Vision-and-Language Navigation from Web Videos</span>
        <span class="paper-authors">Mingfei Han, Haihong Hao, Liang Ma, Kamila Zhumakhanova, Ekaterina Radionova, Jingyi Zhang, Xiaojun Chang, Xiaodan Liang, Ivan Laptev</span>
        <span class="paper-meta">Updated 2026-03-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Vision-and-Language Navigation (VLN) has long been constrained by the limited diversity and scalability of simulator-curated datasets, which fail to capture the complexity of real-world environments. To overcome this limitation, we introduce a large-scale video-instruction framework derived from web-based room tour videos, enabling agents to learn from natural human walking demonstrations in diverse, realistic indoor settings. Unlike existing datasets, our framework integrates both open-ended description-enriched trajectories and action-enriched trajectories reconstructed in 3D, providing richer spatial and semantic supervision. A key extension in this work is the incorporation of implicit geometry representations, which extract spatial cues directly from RGB frames without requiring fragile 3D reconstruction. This approach substantially improves data utilization, alleviates reconstruction failures, and unlocks large portions of previously unusable video data. Comprehensive experiments across multiple VLN benchmarks (CVDN, SOON, R2R, and REVERIE) demonstrate that our method not only sets new state-of-the-art performance but also enables the development of robust zero-shot navigation agents. By bridging large-scale web videos with implicit spatial reasoning, this work advances embodied navigation towards more scalable, generalizable, and real-world applicable solutions.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.09259">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.09259.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.09259.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">OSCAR: Occupancy-based Shape Completion via Acoustic Neural Implicit Representations</span>
        <span class="paper-authors">Magdalena Wysocki, Kadir Burak Buldu, Miruna-Alexandra Gafencu, Mohammad Farid Azampour, Nassir Navab</span>
        <span class="paper-meta">Updated 2026-03-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Accurate 3D reconstruction of vertebral anatomy from ultrasound is important for guiding minimally invasive spine interventions, but it remains challenging due to acoustic shadowing and view-dependent signal variations. We propose an occupancy-based shape completion method that reconstructs complete 3D anatomical geometry from partial ultrasound observations. Crucially for intra-operative applications, our approach extracts the anatomical surface directly from the image, avoiding the need for anatomical labels during inference. This label-free completion relies on a coupled latent space representing both the image appearance and the underlying anatomical shape. By leveraging a Neural Implicit Representation (NIR) that jointly models both spatial occupancy and acoustic interactions, the method uses acoustic parameters to become implicitly aware of the unseen regions without explicit shadowing labels through tracking acoustic signal transmission. We show that this method outperforms state-of-the-art shape completion for B-mode ultrasound by 80% in HD95 score. We validate our approach both in-silico and on phantom US images with registered mesh models from CT labels, demonstrating accurate reconstruction of occluded anatomy and robust generalization across diverse imaging conditions. Code and data will be released on publication.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.08279">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.08279.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.08279.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Speed3R: Sparse Feed-forward 3D Reconstruction Models</span>
        <span class="paper-authors">Weining Ren, Xiao Tan, Kai Han</span>
        <span class="paper-meta">Updated 2026-03-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">While recent feed-forward 3D reconstruction models accelerate 3D reconstruction by jointly inferring dense geometry and camera poses in a single pass, their reliance on dense attention imposes a quadratic complexity, creating a prohibitive computational bottleneck that severely limits inference speed. To resolve this, we introduce Speed3R, an end-to-end trainable model inspired by the core principle of Structure-from-Motion: that a sparse set of keypoints is sufficient for robust pose estimation. Speed3R features a dual-branch attention mechanism where a compression branch creates a coarse contextual prior to guide a selection branch, which performs fine-grained attention only on the most informative image tokens. This strategy mimics the efficiency of traditional keypoint matching, achieving a remarkable 12.4x inference speedup on 1000-view sequences, while introducing a minimal, controlled trade-off in geometric accuracy. Validated on standard benchmarks with both VGGT and $π^3$ backbones, our method delivers high-quality reconstructions at a fraction of computational cost, paving the way for efficient large-scale scene modeling.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.08055">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.08055.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.08055.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">$L^3$:Scene-agnostic Visual Localization in the Wild</span>
        <span class="paper-authors">Yu Zhang, Muhua Zhu, Yifei Xue, Tie Ji, Yizhen Lao</span>
        <span class="paper-meta">Updated 2026-03-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Standard visual localization methods typically require offline pre-processing of scenes to obtain 3D structural information for better performance. This inevitably introduces additional computational and time costs, as well as the overhead of storing scene representations. Can we visually localize in a wild scene without any off-line preprocessing step? In this paper, we leverage the online inference capabilities of feed-forward 3D reconstruction networks to propose a novel map-free visual localization framework $L^3$. Specifically, by performing direct online 3D reconstruction on RGB images, followed by two-stage metric scale recovery and pose refinement based on 2D-3D correspondences, $L^3$ achieves high accuracy without the need to pre-build or store any offline scene representations. Extensive experiments demonstrate $L^3$ not only that the performance is comparable to state-of-the-art solutions on various benchmarks, but also that it exhibits significantly superior robustness in sparse scenes (fewer reference images per scene).</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.07937">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.07937.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.07937.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FrameVGGT: Frame Evidence Rolling Memory for streaming VGGT</span>
        <span class="paper-authors">Zhisong Xu, Takeshi Oishi</span>
        <span class="paper-meta">Updated 2026-03-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Streaming Visual Geometry Transformers such as StreamVGGT enable strong online 3D perception but suffer from unbounded KV-cache growth, which limits deployment over long streams. We revisit bounded-memory streaming from the perspective of geometric support. In geometry-driven reasoning, memory quality depends not only on how many tokens are retained, but also on whether the retained memory still preserves sufficiently coherent local support. This suggests that token-level retention may become less suitable under fixed budgets, as it can thin the evidence available within each contributing frame and make subsequent fusion more sensitive to weakly aligned history. Motivated by this observation, we propose FrameVGGT, a frame-driven rolling explicit-memory framework that treats each frame&#x27;s incremental KV contribution as a coherent evidence block. FrameVGGT summarizes each block into a compact prototype and maintains a fixed-capacity mid-term bank of complementary frame blocks under strict budgets, with an optional lightweight anchor tier for rare prolonged degradation. Across long-sequence 3D reconstruction, video depth estimation, and camera pose benchmarks, FrameVGGT achieves favorable accuracy--memory trade-offs under bounded memory, while maintaining more stable geometry over long streams.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.07690">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.07690.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.07690.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ACCURATE: Arbitrary-shaped Continuum Reconstruction Under Robust Adaptive Two-view Estimation</span>
        <span class="paper-authors">Yaozhi Zhang, Shun Yu, Yugang Zhang, Yang Liu</span>
        <span class="paper-meta">Updated 2026-03-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Accurate reconstruction of arbitrary-shaped long slender continuum bodies, such as guidewires, catheters and other soft continuum manipulators, is essential for accurate mechanical simulation. However, existing image-based reconstruction approaches often suffer from limited accuracy because they often underutilize camera geometry, or lack generality as they rely on rigid geometric assumptions that may fail for continuum robots with complex and highly deformable shapes. To address these limitations, we propose ACCURATE, a 3D reconstruction framework integrating an image segmentation neural network with a geometry-constrained topology traversal and dynamic programming algorithm that enforces global biplanar geometric consistency, minimizes the cumulative point-to-epipolar-line distance, and remains robust to occlusions and epipolar ambiguities cases caused by noise and discretization. Our method achieves high reconstruction accuracy on both simulated and real phantom datasets acquired using a clinical X-ray C-arm system, with mean absolute errors below 1.0 mm.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.07533">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.07533.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.07533.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DogWeave: High-Fidelity 3D Canine Reconstruction from a Single Image via Normal Fusion and Conditional Inpainting</span>
        <span class="paper-authors">Shufan Sun, Chenchen Wang, Zongfu Yu</span>
        <span class="paper-meta">Updated 2026-03-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Monocular 3D animal reconstruction is challenging due to complex articulation, self-occlusion, and fine-scale details such as fur. Existing methods often produce distorted geometry and inconsistent textures due to the lack of articulated 3D supervision and limited availability of back-view images in 2D datasets, which makes reconstructing unobserved regions particularly difficult. To address these limitations, we propose DogWeave, a model-based framework for reconstructing high-fidelity 3D canine models from a single RGB image. DogWeave improves geometry by refining a coarsely-initiated parametric mesh into a detailed SDF representation through multi-view normal field optimization using diffusion-enhanced normals. It then generates view-consistent textures through conditional partial inpainting guided by structure and style cues, enabling realistic reconstruction of unobserved regions. Using only about 7,000 dog images processed via our 2D pipeline for training, DogWeave produces complete, realistic 3D models and outperforms state-of-the-art single image to 3d reconstruction methods in both shape accuracy and texture realism for canines.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.07441">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.07441.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.07441.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SurgCUT3R: Surgical Scene-Aware Continuous Understanding of Temporal 3D Representation</span>
        <span class="paper-authors">Kaiyuan Xu, Fangzhou Hong, Daniel Elson, Baoru Huang</span>
        <span class="paper-meta">Updated 2026-03-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Reconstructing surgical scenes from monocular endoscopic video is critical for advancing robotic-assisted surgery. However, the application of state-of-the-art general-purpose reconstruction models is constrained by two key challenges: the lack of supervised training data and performance degradation over long video sequences. To overcome these limitations, we propose SurgCUT3R, a systematic framework that adapts unified 3D reconstruction models to the surgical domain. Our contributions are threefold. First, we develop a data generation pipeline that exploits public stereo surgical datasets to produce large-scale, metric-scale pseudo-ground-truth depth maps, effectively bridging the data gap. Second, we propose a hybrid supervision strategy that couples our pseudo-ground-truth with geometric self-correction to enhance robustness against inherent data imperfections. Third, we introduce a hierarchical inference framework that employs two specialized models to effectively mitigate accumulated pose drift over long surgical videos: one for global stability and one for local accuracy. Experiments on the SCARED and StereoMIS datasets demonstrate that our method achieves a competitive balance between accuracy and efficiency, delivering near state-of-the-art but substantially faster pose estimation and offering a practical and effective solution for robust reconstruction in surgical environments. Project page: https://chumo-xu.github.io/SurgCUT3R-ICRA26/.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.06971">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.06971.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.06971.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Virtual Intraoperative CT (viCT): Sequential Anatomic Updates for Modeling Tissue Resection Throughout Endoscopic Sinus Surgery</span>
        <span class="paper-authors">Nicole M. Gunderson, Graham J. Harris, Jeremy S. Ruthberg, Pengcheng Chen, Di Mao, Randall A. Bly, Waleed M. Abuzeid, Eric J. Seibel</span>
        <span class="paper-meta">Updated 2026-03-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Purpose: Incomplete dissection is a common cause of persistent disease and revision endoscopic sinus surgery (ESS) in chronic rhinosinusitis. Current image-guided surgery systems typically reference static preoperative CT (pCT), and do not model evolving resection boundaries. We present Virtual Intraoperative CT (viCT), a method for sequentially updating pCT throughout ESS using intraoperative 3D reconstructions from monocular endoscopic video to enable visualization of evolving anatomy in CT format.   Methods: Monocular endoscopic video is processed using a depth-supervised NeRF framework with virtual stereo synthesis to generate metrically scaled 3D reconstructions at multiple surgical intervals. Reconstructions undergo rigid, landmark-based registration in 3D Slicer guided by anatomical correspondences, and are then voxelized into the pCT grid. viCT volumes were generated using a ray-based occupancy comparison between pCT and reconstruction to delete outdated voxels and remap preserved anatomy and updated boundaries. Performance is evaluated in a cadaveric feasibility study of four specimens across four ESS stages using volumetric overlap (DSC, Jaccard) and surface metrics (HD95, Chamfer, MSD, RMSD), and qualitative comparisons to ground-truth CT.   Results: viCT updates show agreement with ground-truth anatomy across surgical stages, with submillimeter mean surface errors. Dice Similarity Coefficient (DSC) = 0.88 +/- 0.05 and Jaccard Index = 0.79 +/- 0.07, and Hausdorff Distance 95% (HD95) = 0.69 +/- 0.28 mm, Chamfer Distance = 0.09 +/- 0.05 mm, Mean Surface Distance (MSD) = 0.11 +/- 0.05 mm, and Root Mean Square Distance (RMSD) = 0.32 +/- 0.10 mm.   Conclusion: viCT enables CT-format anatomic updating in an ESS setting without ancillary hardware. Future work will focus on fully automating registration, validation in live cases, and optimizing runtime for real-time deployment.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.06956">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.06956.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.06956.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">VGG-T$^3$: Offline Feed-Forward 3D Reconstruction at Scale</span>
        <span class="paper-authors">Sven Elflein, Ruilong Li, Sérgio Agostinho, Zan Gojcic, Laura Leal-Taixé, Qunjie Zhou, Aljosa Osep</span>
        <span class="paper-meta">Updated 2026-02-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We present a scalable 3D reconstruction model that addresses a critical limitation in offline feed-forward methods: their computational and memory requirements grow quadratically w.r.t. the number of input images. Our approach is built on the key insight that this bottleneck stems from the varying-length Key-Value (KV) space representation of scene geometry, which we distill into a fixed-size Multi-Layer Perceptron (MLP) via test-time training. VGG-T$^3$ (Visual Geometry Grounded Test Time Training) scales linearly w.r.t. the number of input views, similar to online models, and reconstructs a $1k$ image collection in just $54$ seconds, achieving a $11.6\times$ speed-up over baselines that rely on softmax attention. Since our method retains global scene aggregation capability, our point map reconstruction error outperforming other linear-time methods by large margins. Finally, we demonstrate visual localization capabilities of our model by querying the scene representation with unseen images.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.23361">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.23361.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.23361.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">UniScale: Unified Scale-Aware 3D Reconstruction for Multi-View Understanding via Prior Injection for Robotic Perception</span>
        <span class="paper-authors">Mohammad Mahdavian, Gordon Tan, Binbin Xu, Yuan Ren, Dongfeng Bai, Bingbing Liu</span>
        <span class="paper-meta">Updated 2026-02-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We present UniScale, a unified, scale-aware multi-view 3D reconstruction framework for robotic applications that flexibly integrates geometric priors through a modular, semantically informed design. In vision-based robotic navigation, the accurate extraction of environmental structure from raw image sequences is critical for downstream tasks. UniScale addresses this challenge with a single feed-forward network that jointly estimates camera intrinsics and extrinsics, scale-invariant depth and point maps, and the metric scale of a scene from multi-view images, while optionally incorporating auxiliary geometric priors when available. By combining global contextual reasoning with camera-aware feature representations, UniScale is able to recover the metric-scale of the scene. In robotic settings where camera intrinsics are known, they can be easily incorporated to improve performance, with additional gains obtained when camera poses are also available. This co-design enables robust, metric-aware 3D reconstruction within a single unified model. Importantly, UniScale does not require training from scratch, and leverages world priors exhibited in pre-existing models without geometric encoding strategies, making it particularly suitable for resource-constrained robotic teams. We evaluate UniScale on multiple benchmarks, demonstrating strong generalization and consistent performance across diverse environments. We will release our implementation upon acceptance.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.23224">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.23224.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.23224.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FLIGHT: Fibonacci Lattice-based Inference for Geometric Heading in real-Time</span>
        <span class="paper-authors">David Dirnfeld, Fabien Delattre, Pedro Miraldo, Erik Learned-Miller</span>
        <span class="paper-meta">Updated 2026-02-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Estimating camera motion from monocular video is a fundamental problem in computer vision, central to tasks such as SLAM, visual odometry, and structure-from-motion. Existing methods that recover the camera&#x27;s heading under known rotation, whether from an IMU or an optimization algorithm, tend to perform well in low-noise, low-outlier conditions, but often decrease in accuracy or become computationally expensive as noise and outlier levels increase. To address these limitations, we propose a novel generalization of the Hough transform on the unit sphere (S(2)) to estimate the camera&#x27;s heading. First, the method extracts correspondences between two frames and generates a great circle of directions compatible with each pair of correspondences. Then, by discretizing the unit sphere using a Fibonacci lattice as bin centers, each great circle casts votes for a range of directions, ensuring that features unaffected by noise or dynamic objects vote consistently for the correct motion direction. Experimental results on three datasets demonstrate that the proposed method is on the Pareto frontier of accuracy versus efficiency. Additionally, experiments on SLAM show that the proposed method reduces RMSE by correcting the heading during camera pose initialization.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.23115">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.23115.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.23115.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">UCM: Unifying Camera Control and Memory with Time-aware Positional Encoding Warping for World Models</span>
        <span class="paper-authors">Tianxing Xu, Zixuan Wang, Guangyuan Wang, Li Hu, Zhongyi Zhang, Peng Zhang, Bang Zhang, Song-Hai Zhang</span>
        <span class="paper-meta">Updated 2026-02-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">World models based on video generation demonstrate remarkable potential for simulating interactive environments but face persistent difficulties in two key areas: maintaining long-term content consistency when scenes are revisited and enabling precise camera control from user-provided inputs. Existing methods based on explicit 3D reconstruction often compromise flexibility in unbounded scenarios and fine-grained structures. Alternative methods rely directly on previously generated frames without establishing explicit spatial correspondence, thereby constraining controllability and consistency. To address these limitations, we present UCM, a novel framework that unifies long-term memory and precise camera control via a time-aware positional encoding warping mechanism. To reduce computational overhead, we design an efficient dual-stream diffusion transformer for high-fidelity generation. Moreover, we introduce a scalable data curation strategy utilizing point-cloud-based rendering to simulate scene revisiting, facilitating training on over 500K monocular videos. Extensive experiments on real-world and synthetic benchmarks demonstrate that UCM significantly outperforms state-of-the-art methods in long-term scene consistency, while also achieving precise camera controllability in high-fidelity video generation.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.22960">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.22960.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.22960.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Sapling-NeRF: Geo-Localised Sapling Reconstruction in Forests for Ecological Monitoring</span>
        <span class="paper-authors">Miguel Ángel Muñoz-Bañón, Nived Chebrolu, Sruthi M. Krishna Moorthy, Yifu Tao, Fernando Torres, Roberto Salguero-Gómez, Maurice Fallon</span>
        <span class="paper-meta">Updated 2026-02-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Saplings are key indicators of forest regeneration and overall forest health. However, their fine-scale architectural traits are difficult to capture with existing 3D sensing methods, which make quantitative evaluation difficult. Terrestrial Laser Scanners (TLS), Mobile Laser Scanners (MLS), or traditional photogrammetry approaches poorly reconstruct thin branches, dense foliage, and lack the scale consistency needed for long-term monitoring. Implicit 3D reconstruction methods such as Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) are promising alternatives, but cannot recover the true scale of a scene and lack any means to be accurately geo-localised. In this paper, we present a pipeline which fuses NeRF, LiDAR SLAM, and GNSS to enable repeatable, geo-localised ecological monitoring of saplings. Our system proposes a three-level representation: (i) coarse Earth-frame localisation using GNSS, (ii) LiDAR-based SLAM for centimetre-accurate localisation and reconstruction, and (iii) NeRF-derived object-centric dense reconstruction of individual saplings. This approach enables repeatable quantitative evaluation and long-term monitoring of sapling traits. Our experiments in forest plots in Wytham Woods (Oxford, UK) and Evo (Finland) show that stem height, branching patterns, and leaf-to-wood ratios can be captured with increased accuracy as compared to TLS. We demonstrate that accurate stem skeletons and leaf distributions can be measured for saplings with heights between 0.5m and 2m in situ, giving ecologists access to richer structural and quantitative data for analysing forest dynamics.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.22731">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.22731.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.22731.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">QuadSync: Quadrifocal Tensor Synchronization via Tucker Decomposition</span>
        <span class="paper-authors">Daniel Miao, Gilad Lerman, Joe Kileel</span>
        <span class="paper-meta">Updated 2026-02-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">In structure from motion, quadrifocal tensors capture more information than their pairwise counterparts (essential matrices), yet they have often been thought of as impractical and only of theoretical interest. In this work, we challenge such beliefs by providing a new framework to recover $n$ cameras from the corresponding collection of quadrifocal tensors. We form the block quadrifocal tensor and show that it admits a Tucker decomposition whose factor matrices are the stacked camera matrices, and which thus has a multilinear rank of (4,~4,~4,~4) independent of $n$. We develop the first synchronization algorithm for quadrifocal tensors, using Tucker decomposition, alternating direction method of multipliers, and iteratively reweighted least squares. We further establish relationships between the block quadrifocal, trifocal, and bifocal tensors, and introduce an algorithm that jointly synchronizes these three entities. Numerical experiments demonstrate the effectiveness of our methods on modern datasets, indicating the potential and importance of using higher-order information in synchronization.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.22639">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.22639.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.22639.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GIFSplat: Generative Prior-Guided Iterative Feed-Forward 3D Gaussian Splatting from Sparse Views</span>
        <span class="paper-authors">Tianyu Chen, Wei Xiang, Kang Han, Yu Lu, Di Wu, Gaowen Liu, Ramana Rao Kompella</span>
        <span class="paper-meta">Updated 2026-02-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Feed-forward 3D reconstruction offers substantial runtime advantages over per-scene optimization, which remains slow at inference and often fragile under sparse views. However, existing feed-forward methods still have potential for further performance gains, especially for out-of-domain data, and struggle to retain second-level inference time once a generative prior is introduced. These limitations stem from the one-shot prediction paradigm in existing feed-forward pipeline: models are strictly bounded by capacity, lack inference-time refinement, and are ill-suited for continuously injecting generative priors. We introduce GIFSplat, a purely feed-forward iterative refinement framework for 3D Gaussian Splatting from sparse unposed views. A small number of forward-only residual updates progressively refine current 3D scene using rendering evidence, achieve favorable balance between efficiency and quality. Furthermore, we distill a frozen diffusion prior into Gaussian-level cues from enhanced novel renderings without gradient backpropagation or ever-increasing view-set expansion, thereby enabling per-scene adaptation with generative prior while preserving feed-forward efficiency. Across DL3DV, RealEstate10K, and DTU, GIFSplat consistently outperforms state-of-the-art feed-forward baselines, improving PSNR by up to +2.1 dB, and it maintains second-scale inference time without requiring camera poses or any test-time gradient optimization.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.22571">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.22571.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.22571.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SwiftNDC: Fast Neural Depth Correction for High-Fidelity 3D Reconstruction</span>
        <span class="paper-authors">Kang Han, Wei Xiang, Lu Yu, Mathew Wyatt, Gaowen Liu, Ramana Rao Kompella</span>
        <span class="paper-meta">Updated 2026-02-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Depth-guided 3D reconstruction has gained popularity as a fast alternative to optimization-heavy approaches, yet existing methods still suffer from scale drift, multi-view inconsistencies, and the need for substantial refinement to achieve high-fidelity geometry. Here, we propose SwiftNDC, a fast and general framework built around a Neural Depth Correction field that produces cross-view consistent depth maps. From these refined depths, we generate a dense point cloud through back-projection and robust reprojection-error filtering, obtaining a clean and uniformly distributed geometric initialization for downstream reconstruction. This reliable dense geometry substantially accelerates 3D Gaussian Splatting (3DGS) for mesh reconstruction, enabling high-quality surfaces with significantly fewer optimization iterations. For novel-view synthesis, SwiftNDC can also improve 3DGS rendering quality, highlighting the benefits of strong geometric initialization. We conduct a comprehensive study across five datasets, including two for mesh reconstruction, as well as three for novel-view synthesis. SwiftNDC consistently reduces running time for accurate mesh reconstruction and boosts rendering fidelity for view synthesis, demonstrating the effectiveness of combining neural depth refinement with robust geometric initialization for high-fidelity and efficient 3D reconstruction.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.22565">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.22565.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.22565.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Global-Aware Edge Prioritization for Pose Graph Initialization</span>
        <span class="paper-authors">Tong Wei, Giorgos Tolias, Jiri Matas, Daniel Barath</span>
        <span class="paper-meta">Updated 2026-02-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">The pose graph is a core component of Structure-from-Motion (SfM), where images act as nodes and edges encode relative poses. Since geometric verification is expensive, SfM pipelines restrict the pose graph to a sparse set of candidate edges, making initialization critical. Existing methods rely on image retrieval to connect each image to its $k$ nearest neighbors, treating pairs independently and ignoring global consistency. We address this limitation through the concept of edge prioritization, ranking candidate edges by their utility for SfM. Our approach has three components: (1) a GNN trained with SfM-derived supervision to predict globally consistent edge reliability; (2) multi-minimal-spanning-tree-based pose graph construction guided by these ranks; and (3) connectivity-aware score modulation that reinforces weak regions and reduces graph diameter. This globally informed initialization yields more reliable and compact pose graphs, improving reconstruction accuracy in sparse and high-speed settings and outperforming SOTA retrieval methods on ambiguous scenes. The ode and trained models are available at https://github.com/weitong8591/global_edge_prior.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.21963">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.21963.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.21963.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Geometry-as-context: Modulating Explicit 3D in Scene-consistent Video Generation to Geometry Context</span>
        <span class="paper-authors">JiaKui Hu, Jialun Liu, Liying Yang, Xinliang Zhang, Kaiwen Li, Shuang Zeng, Yuanwei Li, Haibin Huang, Chi Zhang, Yanye Lu</span>
        <span class="paper-meta">Updated 2026-02-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Scene-consistent video generation aims to create videos that explore 3D scenes based on a camera trajectory. Previous methods rely on video generation models with external memory for consistency, or iterative 3D reconstruction and inpainting, which accumulate errors during inference due to incorrect intermediary outputs, non-differentiable processes, and separate models. To overcome these limitations, we introduce ``geometry-as-context&quot;. It iteratively completes the following steps using an autoregressive camera-controlled video generation model: (1) estimates the geometry of the current view necessary for 3D reconstruction, and (2) simulates and restores novel view images rendered by the 3D scene. Under this multi-task framework, we develop the camera gated attention module to enhance the model&#x27;s capability to effectively leverage camera poses. During the training phase, text contexts are utilized to ascertain whether geometric or RGB images should be generated. To ensure that the model can generate RGB-only outputs during inference, the geometry context is randomly dropped from the interleaved text-image-geometry training sequence. The method has been tested on scene video generation with one-direction and forth-and-back trajectories. The results show its superiority over previous approaches in maintaining scene consistency and camera control.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.21929">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.21929.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.21929.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Event-Aided Sharp Radiance Field Reconstruction for Fast-Flying Drones</span>
        <span class="paper-authors">Rong Zou, Marco Cannici, Davide Scaramuzza</span>
        <span class="paper-meta">Updated 2026-02-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Fast-flying aerial robots promise rapid inspection under limited battery constraints, with direct applications in infrastructure inspection, terrain exploration, and search and rescue. However, high speeds lead to severe motion blur in images and induce significant drift and noise in pose estimates, making dense 3D reconstruction with Neural Radiance Fields (NeRFs) particularly challenging due to their high sensitivity to such degradations. In this work, we present a unified framework that leverages asynchronous event streams alongside motion-blurred frames to reconstruct high-fidelity radiance fields from agile drone flights. By embedding event-image fusion into NeRF optimization and jointly refining event-based visual-inertial odometry priors using both event and frame modalities, our method recovers sharp radiance fields and accurate camera trajectories without ground-truth supervision. We validate our approach on both synthetic data and real-world sequences captured by a fast-flying drone. Despite highly dynamic drone flights, where RGB frames are severely degraded by motion blur and pose priors become unreliable, our method reconstructs high-fidelity radiance fields and preserves fine scene details, delivering a performance gain of over 50% on real-world data compared to state-of-the-art methods.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.21101">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.21101.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.21101.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">UFO: Unifying Feed-Forward and Optimization-based Methods for Large Driving Scene Modeling</span>
        <span class="paper-authors">Kaiyuan Tan, Yingying Shen, Mingfei Tu, Haohui Zhu, Bing Wang, Guang Chen, Hangjun Ye, Haiyang Sun</span>
        <span class="paper-meta">Updated 2026-02-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Dynamic driving scene reconstruction is critical for autonomous driving simulation and closed-loop learning. While recent feed-forward methods have shown promise for 3D reconstruction, they struggle with long-range driving sequences due to quadratic complexity in sequence length and challenges in modeling dynamic objects over extended durations. We propose UFO, a novel recurrent paradigm that combines the benefits of optimization-based and feed-forward methods for efficient long-range 4D reconstruction. Our approach maintains a 4D scene representation that is iteratively refined as new observations arrive, using a visibility-based filtering mechanism to select informative scene tokens and enable efficient processing of long sequences. For dynamic objects, we introduce an object pose-guided modeling approach that supports accurate long-range motion capture. Experiments on the Waymo Open Dataset demonstrate that our method significantly outperforms both per-scene optimization and existing feed-forward methods across various sequence lengths. Notably, our approach can reconstruct 16-second driving logs within 0.5 second while maintaining superior visual quality and geometric accuracy.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.20943">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.20943.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.20943.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">RU4D-SLAM: Reweighting Uncertainty in Gaussian Splatting SLAM for 4D Scene Reconstruction</span>
        <span class="paper-authors">Yangfan Zhao, Hanwei Zhang, Ke Huang, Qiufeng Wang, Zhenzhou Shao, Dengyu Wu</span>
        <span class="paper-meta">Updated 2026-02-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Combining 3D Gaussian splatting with Simultaneous Localization and Mapping (SLAM) has gained popularity as it enables continuous 3D environment reconstruction during motion. However, existing methods struggle in dynamic environments, particularly moving objects complicate 3D reconstruction and, in turn, hinder reliable tracking. The emergence of 4D reconstruction, especially 4D Gaussian splatting, offers a promising direction for addressing these challenges, yet its potential for 4D-aware SLAM remains largely underexplored. Along this direction, we propose a robust and efficient framework, namely Reweighting Uncertainty in Gaussian Splatting SLAM (RU4D-SLAM) for 4D scene reconstruction, that introduces temporal factors into spatial 3D representation while incorporating uncertainty-aware perception of scene changes, blurred image synthesis, and dynamic scene reconstruction. We enhance dynamic scene representation by integrating motion blur rendering, and improve uncertainty-aware tracking by extending per-pixel uncertainty modeling, which is originally designed for static scenarios, to handle blurred images. Furthermore, we propose a semantic-guided reweighting mechanism for per-pixel uncertainty estimation in dynamic scenes, and introduce a learnable opacity weight to support adaptive 4D mapping. Extensive experiments on standard benchmarks demonstrate that our method substantially outperforms state-of-the-art approaches in both trajectory accuracy and 4D scene reconstruction, particularly in dynamic environments with moving objects and low-quality inputs. Code available: https://ru4d-slam.github.io</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.20807">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.20807.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.20807.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Monocular Endoscopic Tissue 3D Reconstruction with Multi-Level Geometry Regularization</span>
        <span class="paper-authors">Yangsen Chen, Hao Wang</span>
        <span class="paper-meta">Updated 2026-02-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Reconstructing deformable endoscopic tissues is crucial for achieving robot-assisted surgery. However, 3D Gaussian Splatting-based approaches encounter challenges in achieving consistent tissue surface reconstruction, while existing NeRF-based methods lack real-time rendering capabilities. In pursuit of both smooth deformable surfaces and real-time rendering, we introduce a novel approach based on 3D Gaussian Splatting. Specifically, we introduce surface-aware reconstruction, initially employing a Sign Distance Field-based method to construct a mesh, subsequently utilizing this mesh to constrain the Gaussian Splatting reconstruction process. Furthermore, to ensure the generation of physically plausible deformations, we incorporate local rigidity and global non-rigidity restrictions to guide Gaussian deformation, tailored for the highly deformable nature of soft endoscopic tissue. Based on 3D Gaussian Splatting, our proposed method delivers a fast rendering process and smooth surface appearances. Quantitative and qualitative analysis against alternative methodologies shows that our approach achieves solid reconstruction quality in both textures and geometries.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.20718">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.20718.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.20718.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">From Pairs to Sequences: Track-Aware Policy Gradients for Keypoint Detection</span>
        <span class="paper-authors">Yepeng Liu, Hao Li, Liwen Yang, Fangzhen Li, Xudi Ge, Yuliang Gu, kuang Gao, Bing Wang, Guang Chen, Hangjun Ye, Yongchao Xu</span>
        <span class="paper-meta">Updated 2026-02-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Keypoint-based matching is a fundamental component of modern 3D vision systems, such as Structure-from-Motion (SfM) and SLAM. Most existing learning-based methods are trained on image pairs, a paradigm that fails to explicitly optimize for the long-term trackability of keypoints across sequences under challenging viewpoint and illumination changes. In this paper, we reframe keypoint detection as a sequential decision-making problem. We introduce TraqPoint, a novel, end-to-end Reinforcement Learning (RL) framework designed to optimize the \textbf{Tra}ck-\textbf{q}uality (Traq) of keypoints directly on image sequences. Our core innovation is a track-aware reward mechanism that jointly encourages the consistency and distinctiveness of keypoints across multiple views, guided by a policy gradient method. Extensive evaluations on sparse matching benchmarks, including relative pose estimation and 3D reconstruction, demonstrate that TraqPoint significantly outperforms some state-of-the-art (SOTA) keypoint detection and description methods.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.20630">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.20630.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.20630.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Long-Term Multi-Session 3D Reconstruction Under Substantial Appearance Change</span>
        <span class="paper-authors">Beverley Gorry, Tobias Fischer, Michael Milford, Alejandro Fontan</span>
        <span class="paper-meta">Updated 2026-02-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Long-term environmental monitoring requires the ability to reconstruct and align 3D models across repeated site visits separated by months or years. However, existing Structure-from-Motion (SfM) pipelines implicitly assume near-simultaneous image capture and limited appearance change, and therefore fail when applied to long-term monitoring scenarios such as coral reef surveys, where substantial visual and structural change is common. In this paper, we show that the primary limitation of current approaches lies in their reliance on post-hoc alignment of independently reconstructed sessions, which is insufficient under large temporal appearance change. We address this limitation by enforcing cross-session correspondences directly within a joint SfM reconstruction. Our approach combines complementary handcrafted and learned visual features to robustly establish correspondences across large temporal gaps, enabling the reconstruction of a single coherent 3D model from imagery captured years apart, where standard independent and joint SfM pipelines break down. We evaluate our method on long-term coral reef datasets exhibiting significant real-world change, and demonstrate consistent joint reconstruction across sessions in cases where existing methods fail to produce coherent reconstructions. To ensure scalability to large datasets, we further restrict expensive learned feature matching to a small set of likely cross-session image pairs identified via visual place recognition, which reduces computational cost and improves alignment robustness.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.20584">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.20584.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.20584.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Progressive Per-Branch Depth Optimization for DEFOM-Stereo and SAM3 Joint Analysis in UAV Forestry Applications</span>
        <span class="paper-authors">Yida Lin, Bing Xue, Mengjie Zhang, Sam Schofield, Richard Green</span>
        <span class="paper-meta">Updated 2026-02-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Accurate per-branch 3D reconstruction is a prerequisite for autonomous UAV-based tree pruning; however, dense disparity maps from modern stereo matchers often remain too noisy for individual branch analysis in complex forest canopies. This paper introduces a progressive pipeline integrating DEFOM-Stereo foundation-model disparity estimation, SAM3 instance segmentation, and multi-stage depth optimization to deliver robust per-branch point clouds. Starting from a naive baseline, we systematically identify and resolve three error families through successive refinements. Mask boundary contamination is first addressed through morphological erosion and subsequently refined via a skeleton-preserving variant to safeguard thin-branch topology. Segmentation inaccuracy is then mitigated using LAB-space Mahalanobis color validation coupled with cross-branch overlap arbitration. Finally, depth noise - the most persistent error source - is initially reduced by outlier removal and median filtering, before being superseded by a robust five-stage scheme comprising MAD global detection, spatial density consensus, local MAD filtering, RGB-guided filtering, and adaptive bilateral filtering. Evaluated on 1920x1080 stereo imagery of Radiata pine (Pinus radiata) acquired with a ZED Mini camera (63 mm baseline) from a UAV in Canterbury, New Zealand, the proposed pipeline reduces the average per-branch depth standard deviation by 82% while retaining edge fidelity. The result is geometrically coherent 3D point clouds suitable for autonomous pruning tool positioning. All code and processed data are publicly released to facilitate further UAV forestry research.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.20539">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.20539.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.20539.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Large-scale Photorealistic Outdoor 3D Scene Reconstruction from UAV Imagery Using Gaussian Splatting Techniques</span>
        <span class="paper-authors">Christos Maikos, Georgios Angelidis, Georgios Th. Papadopoulos</span>
        <span class="paper-meta">Updated 2026-02-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">In this study, we present an end-to-end pipeline capable of converting drone-captured video streams into high-fidelity 3D reconstructions with minimal latency. Unmanned aerial vehicles (UAVs) are extensively used in aerial real-time perception applications. Moreover, recent advances in 3D Gaussian Splatting (3DGS) have demonstrated significant potential for real-time neural rendering. However, their integration into end-to-end UAV-based reconstruction and visualization systems remains underexplored. Our goal is to propose an efficient architecture that combines live video acquisition via RTMP streaming, synchronized sensor fusion, camera pose estimation, and 3DGS optimization, achieving continuous model updates and low-latency deployment within interactive visualization environments that supports immersive augmented and virtual reality (AR/VR) applications. Experimental results demonstrate that the proposed method achieves competitive visual fidelity, while delivering significantly higher rendering performance and substantially reduced end-to-end latency, compared to NeRF-based approaches. Reconstruction quality remains within 4-7\% of high-fidelity offline references, confirming the suitability of the proposed system for real-time, scalable augmented perception from aerial platforms.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.20342">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.20342.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.20342.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">tttLRM: Test-Time Training for Long Context and Autoregressive 3D Reconstruction</span>
        <span class="paper-authors">Chen Wang, Hao Tan, Wang Yifan, Zhiqin Chen, Yuheng Liu, Kalyan Sunkavalli, Sai Bi, Lingjie Liu, Yiwei Hu</span>
        <span class="paper-meta">Updated 2026-02-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We propose tttLRM, a novel large 3D reconstruction model that leverages a Test-Time Training (TTT) layer to enable long-context, autoregressive 3D reconstruction with linear computational complexity, further scaling the model&#x27;s capability. Our framework efficiently compresses multiple image observations into the fast weights of the TTT layer, forming an implicit 3D representation in the latent space that can be decoded into various explicit formats, such as Gaussian Splats (GS) for downstream applications. The online learning variant of our model supports progressive 3D reconstruction and refinement from streaming observations. We demonstrate that pretraining on novel view synthesis tasks effectively transfers to explicit 3D modeling, resulting in improved reconstruction quality and faster convergence. Extensive experiments show that our method achieves superior performance in feedforward 3D Gaussian reconstruction compared to state-of-the-art approaches on both objects and scenes.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.20160">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.20160.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.20160.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Monocular Mesh Recovery and Body Measurement of Female Saanen Goats</span>
        <span class="paper-authors">Bo Jin, Shichao Zhao, Jin Lyu, Bin Zhang, Tao Yu, Liang An, Yebin Liu, Meili Wang</span>
        <span class="paper-meta">Updated 2026-02-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">The lactation performance of Saanen dairy goats, renowned for their high milk yield, is intrinsically linked to their body size, making accurate 3D body measurement essential for assessing milk production potential, yet existing reconstruction methods lack goat-specific authentic 3D data. To address this limitation, we establish the FemaleSaanenGoat dataset containing synchronized eight-view RGBD videos of 55 female Saanen goats (6-18 months). Using multi-view DynamicFusion, we fuse noisy, non-rigid point cloud sequences into high-fidelity 3D scans, overcoming challenges from irregular surfaces and rapid movement. Based on these scans, we develop SaanenGoat, a parametric 3D shape model specifically designed for female Saanen goats. This model features a refined template with 41 skeletal joints and enhanced udder representation, registered with our scan data. A comprehensive shape space constructed from 48 goats enables precise representation of diverse individual variations. With the help of SaanenGoat model, we get high-precision 3D reconstruction from single-view RGBD input, and achieve automated measurement of six critical body dimensions: body length, height, chest width, chest girth, hip width, and hip height. Experimental results demonstrate the superior accuracy of our method in both 3D reconstruction and body measurement, presenting a novel paradigm for large-scale 3D vision applications in precision livestock farming.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.19896">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.19896.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.19896.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Ctrl&amp;Shift: High-Quality Geometry-Aware Object Manipulation in Visual Generation</span>
        <span class="paper-authors">Penghui Ruan, Bojia Zi, Xianbiao Qi, Youze Huang, Rong Xiao, Pichao Wang, Jiannong Cao, Yuhui Shi</span>
        <span class="paper-meta">Updated 2026-02-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Object-level manipulation, relocating or reorienting objects in images or videos while preserving scene realism, is central to film post-production, AR, and creative editing. Yet existing methods struggle to jointly achieve three core goals: background preservation, geometric consistency under viewpoint shifts, and user-controllable transformations. Geometry-based approaches offer precise control but require explicit 3D reconstruction and generalize poorly; diffusion-based methods generalize better but lack fine-grained geometric control. We present Ctrl&amp;Shift, an end-to-end diffusion framework to achieve geometry-consistent object manipulation without explicit 3D representations. Our key insight is to decompose manipulation into two stages, object removal and reference-guided inpainting under explicit camera pose control, and encode both within a unified diffusion process. To enable precise, disentangled control, we design a multi-task, multi-stage training strategy that separates background, identity, and pose signals across tasks. To improve generalization, we introduce a scalable real-world dataset construction pipeline that generates paired image and video samples with estimated relative camera poses. Extensive experiments demonstrate that Ctrl&amp;Shift achieves state-of-the-art results in fidelity, viewpoint consistency, and controllability. To our knowledge, this is the first framework to unify fine-grained geometric control and real-world generalization for object manipulation, without relying on any explicit 3D modeling.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.11440">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.11440.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.11440.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Using a 4-megapixel hybrid photon counting detector for fast, lab-based nanoscale x-ray tomography</span>
        <span class="paper-authors">Jordan Fonseca, Zachary H. Levine, Joseph W. Fowler, Felix H. Kim, Galen O&#x27;Neil, Nathan J. Ortiz, John Henry Scott, Daniel S. Swetz, Paul Szypryt, Andras E. Vladar, Nathan Nakamura</span>
        <span class="paper-meta">Updated 2026-02-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Hybrid photon counting detectors (HPCDs) have unlocked new capabilities for x-ray-based measurements at synchrotrons around the world in the last 30 years. By leveraging independently optimized sensor and readout layers, they offer high quantum efficiency ($&gt; 80 \%$), ultra-low dark counts, sub-pixel point-spread function, and high count rates ($&gt; 10^{6}$ counts per pixel per second). Furthermore, their small pixel size and large active area endow them with excellent coverage and resolution for both real-space and reciprocal space imaging. Here, we demonstrate that HPCDs are also well-suited for laboratory-based nanoscale x-ray tomography (nano-xCT). We perform nano-xCT on an integrated circuit fabricated at the 130-nm node and produce a 3D reconstruction with 40 times more photons collected 20 times faster than in this group&#x27;s previous work, for an overall speedup of 800$\times$. We review the technical considerations of using an HPCD for tabletop tomography. We quantify our reconstruction image quality using well-established metrics, including the modulation transfer function (MTF), Fourier shell correlation (FSC), and contrast-to-noise (CNR), to validate our choice of experimental parameters that provide sufficient resolution and imaging speed. Using these metrics, we determine that even under current experimental conditions, 160 nm wiring features are reconstructed at 75-80 nm spatial resolution.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.11375">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.11375.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.11375.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ERGO: Excess-Risk-Guided Optimization for High-Fidelity Monocular 3D Gaussian Splatting</span>
        <span class="paper-authors">Zehua Ma, Hanhui Li, Zhenyu Xie, Xiaonan Luo, Michael Kampffmeyer, Feng Gao, Xiaodan Liang</span>
        <span class="paper-meta">Updated 2026-02-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Generating 3D content from a single image remains a fundamentally challenging and ill-posed problem due to the inherent absence of geometric and textural information in occluded regions. While state-of-the-art generative models can synthesize auxiliary views to provide additional supervision, these views inevitably contain geometric inconsistencies and textural misalignments that propagate and amplify artifacts during 3D reconstruction. To effectively harness these imperfect supervisory signals, we propose an adaptive optimization framework guided by excess risk decomposition, termed ERGO. Specifically, ERGO decomposes the optimization losses in 3D Gaussian splatting into two components, i.e., excess risk that quantifies the suboptimality gap between current and optimal parameters, and Bayes error that models the irreducible noise inherent in synthesized views. This decomposition enables ERGO to dynamically estimate the view-specific excess risk and adaptively adjust loss weights during optimization. Furthermore, we introduce geometry-aware and texture-aware objectives that complement the excess-risk-derived weighting mechanism, establishing a synergistic global-local optimization paradigm. Consequently, ERGO demonstrates robustness against supervision noise while consistently enhancing both geometric fidelity and textural quality of the reconstructed 3D content. Extensive experiments on the Google Scanned Objects dataset and the OmniObject3D dataset demonstrate the superiority of ERGO over existing state-of-the-art methods.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.10278">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.10278.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.10278.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">XSPLAIN: XAI-enabling Splat-based Prototype Learning for Attribute-aware INterpretability</span>
        <span class="paper-authors">Dominik Galus, Julia Farganus, Tymoteusz Zapala, Mikołaj Czachorowski, Piotr Borycki, Przemysław Spurek, Piotr Syga</span>
        <span class="paper-meta">Updated 2026-02-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">3D Gaussian Splatting (3DGS) has rapidly become a standard for high-fidelity 3D reconstruction, yet its adoption in multiple critical domains is hindered by the lack of interpretability of the generation models as well as classification of the Splats. While explainability methods exist for other 3D representations, like point clouds, they typically rely on ambiguous saliency maps that fail to capture the volumetric coherence of Gaussian primitives. We introduce XSPLAIN, the first ante-hoc, prototype-based interpretability framework designed specifically for 3DGS classification. Our approach leverages a voxel-aggregated PointNet backbone and a novel, invertible orthogonal transformation that disentangles feature channels for interpretability while strictly preserving the original decision boundaries. Explanations are grounded in representative training examples, enabling intuitive ``this looks like that&#x27;&#x27; reasoning without any degradation in classification performance. A rigorous user study (N=51) demonstrates a decisive preference for our approach: participants selected XSPLAIN explanations 48.4\% of the time as the best, significantly outperforming baselines $(p&lt;0.001)$, showing that XSPLAIN provides transparency and user trust. The source code for this work is available at: https://github.com/Solvro/ml-splat-xai</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.10239">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.10239.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.10239.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Robo3R: Enhancing Robotic Manipulation with Accurate Feed-Forward 3D Reconstruction</span>
        <span class="paper-authors">Sizhe Yang, Linning Xu, Hao Li, Juncheng Mu, Jia Zeng, Dahua Lin, Jiangmiao Pang</span>
        <span class="paper-meta">Updated 2026-02-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">3D spatial perception is fundamental to generalizable robotic manipulation, yet obtaining reliable, high-quality 3D geometry remains challenging. Depth sensors suffer from noise and material sensitivity, while existing reconstruction models lack the precision and metric consistency required for physical interaction. We introduce Robo3R, a feed-forward, manipulation-ready 3D reconstruction model that predicts accurate, metric-scale scene geometry directly from RGB images and robot states in real time. Robo3R jointly infers scale-invariant local geometry and relative camera poses, which are unified into the scene representation in the canonical robot frame via a learned global similarity transformation. To meet the precision demands of manipulation, Robo3R employs a masked point head for sharp, fine-grained point clouds, and a keypoint-based Perspective-n-Point (PnP) formulation to refine camera extrinsics and global alignment. Trained on Robo3R-4M, a curated large-scale synthetic dataset with four million high-fidelity annotated frames, Robo3R consistently outperforms state-of-the-art reconstruction methods and depth sensors. Across downstream tasks including imitation learning, sim-to-real transfer, grasp synthesis, and collision-free motion planning, we observe consistent gains in performance, suggesting the promise of this alternative 3D sensing module for robotic manipulation.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.10101">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.10101.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.10101.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SARS: A Novel Face and Body Shape and Appearance Aware 3D Reconstruction System extends Morphable Models</span>
        <span class="paper-authors">Gulraiz Khan, Kenneth Y. Wertheim, Kevin Pimbblet, Waqas Ahmed</span>
        <span class="paper-meta">Updated 2026-02-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Morphable Models (3DMMs) are a type of morphable model that takes 2D images as inputs and recreates the structure and physical appearance of 3D objects, especially human faces and bodies. 3DMM combines identity and expression blendshapes with a basic face mesh to create a detailed 3D model. The variability in the 3D Morphable models can be controlled by tuning diverse parameters. They are high-level image descriptors, such as shape, texture, illumination, and camera parameters. Previous research in 3D human reconstruction concentrated solely on global face structure or geometry, ignoring face semantic features such as age, gender, and facial landmarks characterizing facial boundaries, curves, dips, and wrinkles. In order to accommodate changes in these high-level facial characteristics, this work introduces a shape and appearance-aware 3D reconstruction system (named SARS by us), a c modular pipeline that extracts body and face information from a single image to properly rebuild the 3D model of the human full body.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.09918">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.09918.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.09918.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Single-Slice-to-3D Reconstruction in Medical Imaging and Natural Objects: A Comparative Benchmark with SAM 3D</span>
        <span class="paper-authors">Yan Luo, Advaith Ravishankar, Serena Liu, Yutong Yang, Mengyu Wang</span>
        <span class="paper-meta">Updated 2026-02-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">A 3D understanding of anatomy is central to diagnosis and treatment planning, yet volumetric imaging remains costly with long wait times. Image-to-3D foundations models can solve this issue by reconstructing 3D data from 2D modalites. Current foundation models are trained on natural image distributions to reconstruct naturalistic objects from a single image by leveraging geometric priors across pixels. However, it is unclear whether these learned geometric priors transfer to medical data. In this study, we present a controlled zero-shot benchmark of single slice medical image-to-3D reconstruction across five state-of-the-art image-to-3D models: SAM3D, Hunyuan3D-2.1, Direct3D, Hi3DGen, and TripoSG. These are evaluated across six medical datasets spanning anatomical and pathological structures and two natrual datasets, using voxel based metrics and point cloud distance metrics. Across medical datasets, voxel based overlap remains moderate for all models, consistent with a depth reconstruction failure mode when inferring volume from a single slice. In contrast, global distance metrics show more separation between methods: SAM3D achieves the strongest overall topological similarity to ground truth medical 3D data, while alternative models are more prone to over-simplication of reconstruction. Our results quantify the limits of single-slice medical reconstruction and highlight depth ambiguity caused by the planar nature of 2D medical data, motivating multi-view image-to-3D reconstruction to enable reliable medical 3D inference.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.09407">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.09407.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.09407.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">RealSynCol: a high-fidelity synthetic colon dataset for 3D reconstruction applications</span>
        <span class="paper-authors">Chiara Lena, Davide Milesi, Alessandro Casella, Luca Carlini, Joseph C. Norton, James Martin, Bruno Scaglioni, Keith L. Obstein, Roberto De Sire, Marco Spadaccini, Cesare Hassan, Pietro Valdastri, Elena De Momi</span>
        <span class="paper-meta">Updated 2026-02-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Deep learning has the potential to improve colonoscopy by enabling 3D reconstruction of the colon, providing a comprehensive view of mucosal surfaces and lesions, and facilitating the identification of unexplored areas. However, the development of robust methods is limited by the scarcity of large-scale ground truth data. We propose RealSynCol, a highly realistic synthetic dataset designed to replicate the endoscopic environment. Colon geometries extracted from 10 CT scans were imported into a virtual environment that closely mimics intraoperative conditions and rendered with realistic vascular textures. The resulting dataset comprises 28\,130 frames, paired with ground truth depth maps, optical flow, 3D meshes, and camera trajectories. A benchmark study was conducted to evaluate the available synthetic colon datasets for the tasks of depth and pose estimation. Results demonstrate that the high realism and variability of RealSynCol significantly enhance generalization performance on clinical images, proving it to be a powerful tool for developing deep learning algorithms to support endoscopic diagnosis.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.08397">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.08397.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.08397.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Dynamic Black-hole Emission Tomography with Physics-informed Neural Fields</span>
        <span class="paper-authors">Berthy T. Feng, Andrew A. Chael, David Bromley, Aviad Levis, William T. Freeman, Katherine L. Bouman</span>
        <span class="paper-meta">Updated 2026-02-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">With the success of static black-hole imaging, the next frontier is the dynamic and 3D imaging of black holes. Recovering the dynamic 3D gas near a black hole would reveal previously-unseen parts of the universe and inform new physics models. However, only sparse radio measurements from a single viewpoint are possible, making the dynamic 3D reconstruction problem significantly ill-posed. Previously, BH-NeRF addressed the ill-posed problem by assuming Keplerian dynamics of the gas, but this assumption breaks down near the black hole, where the strong gravitational pull of the black hole and increased electromagnetic activity complicate fluid dynamics. To overcome the restrictive assumptions of BH-NeRF, we propose PI-DEF, a physics-informed approach that uses differentiable neural rendering to fit a 4D (time + 3D) emissivity field given EHT measurements. Our approach jointly reconstructs the 3D velocity field with the 4D emissivity field and enforces the velocity as a soft constraint on the dynamics of the emissivity. In experiments on simulated data, we find significantly improved reconstruction accuracy over both BH-NeRF and a physics-agnostic approach. We demonstrate how our method may be used to estimate other physics parameters of the black hole, such as its spin.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.08029">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.08029.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.08029.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Scalable Adaptation of 3D Geometric Foundation Models via Weak Supervision from Internet Video</span>
        <span class="paper-authors">Zihui Gao, Ke Liu, Donny Y. Chen, Duochao Shi, Guosheng Lin, Hao Chen, Chunhua Shen</span>
        <span class="paper-meta">Updated 2026-02-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Geometric foundation models show promise in 3D reconstruction, yet their progress is severely constrained by the scarcity of diverse, large-scale 3D annotations. While Internet videos offer virtually unlimited raw data, utilizing them as a scaling source for geometric learning is challenging due to the absence of ground-truth geometry and the presence of observational noise. To address this, we propose SAGE, a framework for Scalable Adaptation of GEometric foundation models from raw video streams. SAGE leverages a hierarchical mining pipeline to transform videos into training trajectories and hybrid supervision: (1) Informative training trajectory selection; (2) Sparse Geometric Anchoring via SfM point clouds for global structural guidance; and (3) Dense Differentiable Consistency via 3D Gaussian rendering for multi-view constraints. To prevent catastrophic forgetting, we introduce a regularization strategy using anchor data. Extensive experiments show that SAGE significantly enhances zero-shot generalization, reducing Chamfer Distance by 20-42% on unseen benchmarks (7Scenes, TUM-RGBD, Matterport3D) compared to state-of-the-art baselines. To our knowledge, SAGE pioneers the adaptation of geometric foundation models via Internet video, establishing a scalable paradigm for general-purpose 3D learning.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.07891">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.07891.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.07891.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Recovering 3D Shapes from Ultra-Fast Motion-Blurred Images</span>
        <span class="paper-authors">Fei Yu, Shudan Guo, Shiqing Xin, Beibei Wang, Haisen Zhao, Wenzheng Chen</span>
        <span class="paper-meta">Updated 2026-02-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We consider the problem of 3D shape recovery from ultra-fast motion-blurred images. While 3D reconstruction from static images has been extensively studied, recovering geometry from extreme motion-blurred images remains challenging. Such scenarios frequently occur in both natural and industrial settings, such as fast-moving objects in sports (e.g., balls) or rotating machinery, where rapid motion distorts object appearance and makes traditional 3D reconstruction techniques like Multi-View Stereo (MVS) ineffective.   In this paper, we propose a novel inverse rendering approach for shape recovery from ultra-fast motion-blurred images. While conventional rendering techniques typically synthesize blur by averaging across multiple frames, we identify a major computational bottleneck in the repeated computation of barycentric weights. To address this, we propose a fast barycentric coordinate solver, which significantly reduces computational overhead and achieves a speedup of up to 4.57x, enabling efficient and photorealistic simulation of high-speed motion. Crucially, our method is fully differentiable, allowing gradients to propagate from rendered images to the underlying 3D shape, thereby facilitating shape recovery through inverse rendering.   We validate our approach on two representative motion types: rapid translation and rotation. Experimental results demonstrate that our method enables efficient and realistic modeling of ultra-fast moving objects in the forward simulation. Moreover, it successfully recovers 3D shapes from 2D imagery of objects undergoing extreme translational and rotational motion, advancing the boundaries of vision-based 3D reconstruction. Project page: https://maxmilite.github.io/rec-from-ultrafast-blur/</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.07860">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.07860.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.07860.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Compressed Sensing Methods for Memory Reduction in Monte Carlo Simulations</span>
        <span class="paper-authors">Ethan Lame, Camille Palmer, Todd Palmer, Ilham Variansyah</span>
        <span class="paper-meta">Updated 2026-02-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Monte Carlo simulations of neutronic systems are computationally intensive and demand significant memory resources for high-fidelity modeling. Compressed sensing enables accurate reconstruction of signals from significantly fewer samples than traditional methods. The specific implementation of compressed sensing investigated here involves the use of overlapping cells to collect tallies. Increasing the number of samples improves the reconstruction accuracy, although the marginal gains diminish with more samples. Reconstruction quality is strongly influenced by the sparsity parameter used in basis pursuit denoising. Across the three test cases considered, memory reductions of up to 81.25% (96.25%) are demonstrated for 2D (3D) reconstructions, with select scenarios achieving reconstruction errors within 1 standard deviation of the corresponding high-fidelity reference results.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.07771">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.07771.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.07771.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Perspective-aware fusion of incomplete depth maps and surface normals for accurate 3D reconstruction</span>
        <span class="paper-authors">Ondrej Hlinka, Georg Kaniak, Christian Kapeller</span>
        <span class="paper-meta">Updated 2026-02-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We address the problem of reconstructing 3D surfaces from depth and surface normal maps acquired by a sensor system based on a single perspective camera. Depth and normal maps can be obtained through techniques such as structured-light scanning and photometric stereo, respectively. We propose a perspective-aware log-depth fusion approach that extends existing orthographic gradient-based depth-normals fusion methods by explicitly accounting for perspective projection, leading to metrically accurate 3D reconstructions. Additionally, the method handles missing depth measurements by leveraging available surface normal information to inpaint gaps. Experiments on the DiLiGenT-MV data set demonstrate the effectiveness of our approach and highlight the importance of perspective-aware depth-normals fusion.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.07444">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.07444.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.07444.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MetaSSP: Enhancing Semi-supervised Implicit 3D Reconstruction through Meta-adaptive EMA and SDF-aware Pseudo-label Evaluation</span>
        <span class="paper-authors">Luoxi Zhang, Chun Xie, Itaru Kitahara</span>
        <span class="paper-meta">Updated 2026-02-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Implicit SDF-based methods for single-view 3D reconstruction achieve high-quality surfaces but require large labeled datasets, limiting their scalability. We propose MetaSSP, a novel semi-supervised framework that exploits abundant unlabeled images. Our approach introduces gradient-based parameter importance estimation to regularize adaptive EMA updates and an SDF-aware pseudo-label weighting mechanism combining augmentation consistency with SDF variance. Beginning with a 10% supervised warm-up, the unified pipeline jointly refines labeled and unlabeled data. On the Pix3D benchmark, our method reduces Chamfer Distance by approximately 20.61% and increases IoU by around 24.09% compared to existing semi-supervised baselines, setting a new state of the art.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.06163">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.06163.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.06163.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MGP-KAD: Multimodal Geometric Priors and Kolmogorov-Arnold Decoder for Single-View 3D Reconstruction in Complex Scenes</span>
        <span class="paper-authors">Luoxi Zhang, Chun Xie, Itaru Kitahara</span>
        <span class="paper-meta">Updated 2026-02-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Single-view 3D reconstruction in complex real-world scenes is challenging due to noise, object diversity, and limited dataset availability. To address these challenges, we propose MGP-KAD, a novel multimodal feature fusion framework that integrates RGB and geometric prior to enhance reconstruction accuracy. The geometric prior is generated by sampling and clustering ground-truth object data, producing class-level features that dynamically adjust during training to improve geometric understanding. Additionally, we introduce a hybrid decoder based on Kolmogorov-Arnold Networks (KAN) to overcome the limitations of traditional linear decoders in processing complex multimodal inputs. Extensive experiments on the Pix3D dataset demonstrate that MGP-KAD achieves state-of-the-art (SOTA) performance, significantly improving geometric integrity, smoothness, and detail preservation. Our work provides a robust and effective solution for advancing single-view 3D reconstruction in complex scenes.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.06158">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.06158.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.06158.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">From Blurry to Believable: Enhancing Low-quality Talking Heads with 3D Generative Priors</span>
        <span class="paper-authors">Ding-Jiun Huang, Yuanhao Wang, Shao-Ji Yuan, Albert Mosella-Montoro, Francisco Vicente Carrasco, Cheng Zhang, Fernando De la Torre</span>
        <span class="paper-meta">Updated 2026-02-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Creating high-fidelity, animatable 3D talking heads is crucial for immersive applications, yet often hindered by the prevalence of low-quality image or video sources, which yield poor 3D reconstructions. In this paper, we introduce SuperHead, a novel framework for enhancing low-resolution, animatable 3D head avatars. The core challenge lies in synthesizing high-quality geometry and textures, while ensuring both 3D and temporal consistency during animation and preserving subject identity. Despite recent progress in image, video and 3D-based super-resolution (SR), existing SR techniques are ill-equipped to handle dynamic 3D inputs. To address this, SuperHead leverages the rich priors from pre-trained 3D generative models via a novel dynamics-aware 3D inversion scheme. This process optimizes the latent representation of the generative model to produce a super-resolved 3D Gaussian Splatting (3DGS) head model, which is subsequently rigged to an underlying parametric head model (e.g., FLAME) for animation. The inversion is jointly supervised using a sparse collection of upscaled 2D face renderings and corresponding depth maps, captured from diverse facial expressions and camera viewpoints, to ensure realism under dynamic facial motions. Experiments demonstrate that SuperHead generates avatars with fine-grained facial details under dynamic motions, significantly outperforming baseline methods in visual quality.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.06122">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.06122.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.06122.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Splat and Distill: Augmenting Teachers with Feed-Forward 3D Reconstruction For 3D-Aware Distillation</span>
        <span class="paper-authors">David Shavin, Sagie Benaim</span>
        <span class="paper-meta">Updated 2026-02-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Vision Foundation Models (VFMs) have achieved remarkable success when applied to various downstream 2D tasks. Despite their effectiveness, they often exhibit a critical lack of 3D awareness. To this end, we introduce Splat and Distill, a framework that instills robust 3D awareness into 2D VFMs by augmenting the teacher model with a fast, feed-forward 3D reconstruction pipeline. Given 2D features produced by a teacher model, our method first lifts these features into an explicit 3D Gaussian representation, in a feedforward manner. These 3D features are then ``splatted&quot; onto novel viewpoints, producing a set of novel 2D feature maps used to supervise the student model, ``distilling&quot; geometrically grounded knowledge. By replacing slow per-scene optimization of prior work with our feed-forward lifting approach, our framework avoids feature-averaging artifacts, creating a dynamic learning process where the teacher&#x27;s consistency improves alongside that of the student. We conduct a comprehensive evaluation on a suite of downstream tasks, including monocular depth estimation, surface normal estimation, multi-view correspondence, and semantic segmentation. Our method significantly outperforms prior works, not only achieving substantial gains in 3D awareness but also enhancing the underlying semantic richness of 2D features. Project page is available at https://davidshavin4.github.io/Splat-and-Distill/</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.06032">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.06032.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.06032.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">AGILE: Hand-Object Interaction Reconstruction from Video via Agentic Generation</span>
        <span class="paper-authors">Jin-Chuan Shi, Binhong Ye, Tao Liu, Junzhe He, Yangjinhui Xu, Xiaoyang Liu, Zeju Li, Hao Chen, Chunhua Shen</span>
        <span class="paper-meta">Updated 2026-02-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Reconstructing dynamic hand-object interactions from monocular videos is critical for dexterous manipulation data collection and creating realistic digital twins for robotics and VR. However, current methods face two prohibitive barriers: (1) reliance on neural rendering often yields fragmented, non-simulation-ready geometries under heavy occlusion, and (2) dependence on brittle Structure-from-Motion (SfM) initialization leads to frequent failures on in-the-wild footage. To overcome these limitations, we introduce AGILE, a robust framework that shifts the paradigm from reconstruction to agentic generation for interaction learning. First, we employ an agentic pipeline where a Vision-Language Model (VLM) guides a generative model to synthesize a complete, watertight object mesh with high-fidelity texture, independent of video occlusions. Second, bypassing fragile SfM entirely, we propose a robust anchor-and-track strategy. We initialize the object pose at a single interaction onset frame using a foundation model and propagate it temporally by leveraging the strong visual similarity between our generated asset and video observations. Finally, a contact-aware optimization integrates semantic, geometric, and interaction stability constraints to enforce physical plausibility. Extensive experiments on HO3D, DexYCB, and in-the-wild videos reveal that AGILE outperforms baselines in global geometric accuracy while demonstrating exceptional robustness on challenging sequences where prior art frequently collapses. By prioritizing physical validity, our method produces simulation-ready assets validated via real-to-sim retargeting for robotic applications.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.04672">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.04672.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.04672.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">S-MUSt3R: Sliding Multi-view 3D Reconstruction</span>
        <span class="paper-authors">Leonid Antsfeld, Boris Chidlovskii, Yohann Cabon, Vincent Leroy, Jerome Revaud</span>
        <span class="paper-meta">Updated 2026-02-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">The recent paradigm shift in 3D vision led to the rise of foundation models with remarkable capabilities in 3D perception from uncalibrated images. However, extending these models to large-scale RGB stream 3D reconstruction remains challenging due to memory limitations. This work proposes S-MUSt3R, a simple and efficient pipeline that extends the limits of foundation models for monocular 3D reconstruction. Our approach addresses the scalability bottleneck of foundation models through a simple strategy of sequence segmentation followed by segment alignment and lightweight loop closure optimization. Without model retraining, we benefit from remarkable 3D reconstruction capacities of MUSt3R model and achieve trajectory and reconstruction performance comparable to traditional methods with more complex architecture. We evaluate S-MUSt3R on TUM, 7-Scenes and proprietary robot navigation datasets and show that S-MUSt3R runs successfully on long RGB sequences and produces accurate and consistent 3D reconstruction. Our results highlight the potential of leveraging the MUSt3R model for scalable monocular 3D scene in real-world settings, with an important advantage of making predictions directly in the metric space.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.04517">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.04517.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.04517.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">TrajVG: 3D Trajectory-Coupled Visual Geometry Learning</span>
        <span class="paper-authors">Xingyu Miao, Weiguang Zhao, Tao Lu, Linning Yu, Mulin Yu, Yang Long, Jiangmiao Pang, Junting Dong</span>
        <span class="paper-meta">Updated 2026-02-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Feed-forward multi-frame 3D reconstruction models often degrade on videos with object motion. Global-reference becomes ambiguous under multiple motions, while the local pointmap relies heavily on estimated relative poses and can drift, causing cross-frame misalignment and duplicated structures. We propose TrajVG, a reconstruction framework that makes cross-frame 3D correspondence an explicit prediction by estimating camera-coordinate 3D trajectories. We couple sparse trajectories, per-frame local point maps, and relative camera poses with geometric consistency objectives: (i) bidirectional trajectory-pointmap consistency with controlled gradient flow, and (ii) a pose consistency objective driven by static track anchors that suppresses gradients from dynamic regions. To scale training to in-the-wild videos where 3D trajectory labels are scarce, we reformulate the same coupling constraints into self-supervised objectives using only pseudo 2D tracks, enabling unified training with mixed supervision. Extensive experiments across 3D tracking, pose estimation, pointmap reconstruction, and video depth show that TrajVG surpasses the current feedforward performance baseline.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.04439">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.04439.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.04439.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Improving 2D Diffusion Models for 3D Medical Imaging with Inter-Slice Consistent Stochasticity</span>
        <span class="paper-authors">Chenhe Du, Qing Wu, Xuanyu Tian, Jingyi Yu, Hongjiang Wei, Yuyao Zhang</span>
        <span class="paper-meta">Updated 2026-02-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">3D medical imaging is in high demand and essential for clinical diagnosis and scientific research. Currently, diffusion models (DMs) have become an effective tool for medical imaging reconstruction thanks to their ability to learn rich, high-quality data priors. However, learning the 3D data distribution with DMs in medical imaging is challenging, not only due to the difficulties in data collection but also because of the significant computational burden during model training. A common compromise is to train the DMs on 2D data priors and reconstruct stacked 2D slices to address 3D medical inverse problems. However, the intrinsic randomness of diffusion sampling causes severe inter-slice discontinuities of reconstructed 3D volumes. Existing methods often enforce continuity regularizations along the z-axis, which introduces sensitive hyper-parameters and may lead to over-smoothing results. In this work, we revisit the origin of stochasticity in diffusion sampling and introduce Inter-Slice Consistent Stochasticity (ISCS), a simple yet effective strategy that encourages interslice consistency during diffusion sampling. Our key idea is to control the consistency of stochastic noise components during diffusion sampling, thereby aligning their sampling trajectories without adding any new loss terms or optimization steps. Importantly, the proposed ISCS is plug-and-play and can be dropped into any 2D trained diffusion based 3D reconstruction pipeline without additional computational cost. Experiments on several medical imaging problems show that our method can effectively improve the performance of medical 3D imaging problems based on 2D diffusion models. Our findings suggest that controlling inter-slice stochasticity is a principled and practically attractive route toward high-fidelity 3D medical imaging with 2D diffusion priors. The code is available at: https://github.com/duchenhe/ISCS</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.04162">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.04162.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.04162.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SuperPoint-E: local features for 3D reconstruction via tracking adaptation in endoscopy</span>
        <span class="paper-authors">O. Leon Barbed, José M. M. Montiel, Pascal Fua, Ana C. Murillo</span>
        <span class="paper-meta">Updated 2026-02-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">In this work, we focus on boosting the feature extraction to improve the performance of Structure-from-Motion (SfM) in endoscopy videos. We present SuperPoint-E, a new local feature extraction method that, using our proposed Tracking Adaptation supervision strategy, significantly improves the quality of feature detection and description in endoscopy. Extensive experimentation on real endoscopy recordings studies our approach&#x27;s most suitable configuration and evaluates SuperPoint-E feature quality. The comparison with other baselines also shows that our 3D reconstructions are denser and cover more and longer video segments because our detector fires more densely and our features are more likely to survive (i.e. higher detection precision). In addition, our descriptor is more discriminative, making the guided matching step almost redundant. The presented approach brings significant improvements in the 3D reconstructions obtained, via SfM on endoscopy videos, compared to the original SuperPoint and the gold standard SfM COLMAP pipeline.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.04108">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.04108.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.04108.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">AnyStyle: Single-Pass Multimodal Stylization for 3D Gaussian Splatting</span>
        <span class="paper-authors">Joanna Kaleta, Bartosz Świrta, Kacper Kania, Przemysław Spurek, Marek Kowalski</span>
        <span class="paper-meta">Updated 2026-02-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">The growing demand for rapid and scalable 3D asset creation has driven interest in feed-forward 3D reconstruction methods, with 3D Gaussian Splatting (3DGS) emerging as an effective scene representation. While recent approaches have demonstrated pose-free reconstruction from unposed image collections, integrating stylization or appearance control into such pipelines remains underexplored. Existing attempts largely rely on image-based conditioning, which limits both controllability and flexibility. In this work, we introduce AnyStyle, a feed-forward 3D reconstruction and stylization framework that enables pose-free, zero-shot stylization through multimodal conditioning. Our method supports both textual and visual style inputs, allowing users to control the scene appearance using natural language descriptions or reference images. We propose a modular stylization architecture that requires only minimal architectural modifications and can be integrated into existing feed-forward 3D reconstruction backbones. Experiments demonstrate that AnyStyle improves style controllability over prior feed-forward stylization methods while preserving high-quality geometric reconstruction. A user study further confirms that AnyStyle achieves superior stylization quality compared to an existing state-of-the-art approach. Repository: https://github.com/joaxkal/AnyStyle.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.04043">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.04043.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.04043.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">EventNeuS: 3D Mesh Reconstruction from a Single Event Camera</span>
        <span class="paper-authors">Shreyas Sachan, Viktor Rudnev, Mohamed Elgharib, Christian Theobalt, Vladislav Golyanik</span>
        <span class="paper-meta">Updated 2026-02-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Event cameras offer a considerable alternative to RGB cameras in many scenarios. While there are recent works on event-based novel-view synthesis, dense 3D mesh reconstruction remains scarcely explored and existing event-based techniques are severely limited in their 3D reconstruction accuracy. To address this limitation, we present EventNeuS, a self-supervised neural model for learning 3D representations from monocular colour event streams. Our approach, for the first time, combines 3D signed distance function and density field learning with event-based supervision. Furthermore, we introduce spherical harmonics encodings into our model for enhanced handling of view-dependent effects. EventNeuS outperforms existing approaches by a significant margin, achieving 34% lower Chamfer distance and 31% lower mean absolute error on average compared to the best previous method.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.03847">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.03847.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.03847.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Pi-GS: Sparse-View Gaussian Splatting with Dense π^3 Initialization</span>
        <span class="paper-authors">Manuel Hofer, Markus Steinberger, Thomas Köhler</span>
        <span class="paper-meta">Updated 2026-02-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Novel view synthesis has evolved rapidly, advancing from Neural Radiance Fields to 3D Gaussian Splatting (3DGS), which offers real-time rendering and rapid training without compromising visual fidelity. However, 3DGS relies heavily on accurate camera poses and high-quality point cloud initialization, which are difficult to obtain in sparse-view scenarios. While traditional Structure from Motion (SfM) pipelines often fail in these settings, existing learning-based point estimation alternatives typically require reliable reference views and remain sensitive to pose or depth errors. In this work, we propose a robust method utilizing π^3, a reference-free point cloud estimation network. We integrate dense initialization from π^3 with a regularization scheme designed to mitigate geometric inaccuracies. Specifically, we employ uncertainty-guided depth supervision, normal consistency loss, and depth warping. Experimental results demonstrate that our approach achieves state-of-the-art performance on the Tanks and Temples, LLFF, DTU, and MipNeRF360 datasets.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.03327">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.03327.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.03327.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Depth Completion in Unseen Field Robotics Environments Using Extremely Sparse Depth Measurements</span>
        <span class="paper-authors">Marco Job, Thomas Stastny, Eleni Kelasidi, Roland Siegwart, Michael Pantic</span>
        <span class="paper-meta">Updated 2026-02-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Autonomous field robots operating in unstructured environments require robust perception to ensure safe and reliable operations. Recent advances in monocular depth estimation have demonstrated the potential of low-cost cameras as depth sensors; however, their adoption in field robotics remains limited due to the absence of reliable scale cues, ambiguous or low-texture conditions, and the scarcity of large-scale datasets. To address these challenges, we propose a depth completion model that trains on synthetic data and uses extremely sparse measurements from depth sensors to predict dense metric depth in unseen field robotics environments. A synthetic dataset generation pipeline tailored to field robotics enables the creation of multiple realistic datasets for training purposes. This dataset generation approach utilizes textured 3D meshes from Structure from Motion and photorealistic rendering with novel viewpoint synthesis to simulate diverse field robotics scenarios. Our approach achieves an end-to-end latency of 53 ms per frame on a Nvidia Jetson AGX Orin, enabling real-time deployment on embedded platforms. Extensive evaluation demonstrates competitive performance across diverse real-world field robotics scenarios.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.03209">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.03209.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.03209.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">3D Foundation Model-Based Loop Closing for Decentralized Collaborative SLAM</span>
        <span class="paper-authors">Pierre-Yves Lajoie, Benjamin Ramtoula, Daniele De Martini, Giovanni Beltrame</span>
        <span class="paper-meta">Updated 2026-02-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Decentralized Collaborative Simultaneous Localization And Mapping (C-SLAM) techniques often struggle to identify map overlaps due to significant viewpoint variations among robots. Motivated by recent advancements in 3D foundation models, which can register images despite large viewpoint differences, we propose a robust loop closing approach that leverages these models to establish inter-robot measurements. In contrast to resource-intensive methods requiring full 3D reconstruction within a centralized map, our approach integrates foundation models into existing SLAM pipelines, yielding scalable and robust multi-robot mapping. Our contributions include: (1) integrating 3D foundation models to reliably estimate relative poses from monocular image pairs within decentralized C-SLAM; (2) introducing robust outlier mitigation techniques critical to the use of these relative poses; and (3) developing specialized pose graph optimization formulations that efficiently resolve scale ambiguities. We evaluate our method against state-of-the-art approaches, demonstrating improvements in localization and mapping accuracy, alongside significant gains in computational and memory efficiency. These results highlight the potential of our approach for deployment in large-scale multi-robot scenarios.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.02430">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.02430.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.02430.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MetricAnything: Scaling Metric Depth Pretraining with Noisy Heterogeneous Sources</span>
        <span class="paper-authors">Baorui Ma, Jiahui Yang, Donglin Di, Xuancheng Zhang, Jianxun Cui, Hao Li, Yan Xie, Wei Chen</span>
        <span class="paper-meta">Updated 2026-01-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Scaling has powered recent advances in vision foundation models, yet extending this paradigm to metric depth estimation remains challenging due to heterogeneous sensor noise, camera-dependent biases, and metric ambiguity in noisy cross-source 3D data. We introduce Metric Anything, a simple and scalable pretraining framework that learns metric depth from noisy, diverse 3D sources without manually engineered prompts, camera-specific modeling, or task-specific architectures. Central to our approach is the Sparse Metric Prompt, created by randomly masking depth maps, which serves as a universal interface that decouples spatial reasoning from sensor and camera biases. Using about 20M image-depth pairs spanning reconstructed, captured, and rendered 3D data across 10000 camera models, we demonstrate-for the first time-a clear scaling trend in the metric depth track. The pretrained model excels at prompt-driven tasks such as depth completion, super-resolution and Radar-camera fusion, while its distilled prompt-free student achieves state-of-the-art results on monocular depth estimation, camera intrinsics recovery, single/multi-view metric 3D reconstruction, and VLA planning. We also show that using pretrained ViT of Metric Anything as a visual encoder significantly boosts Multimodal Large Language Model capabilities in spatial intelligence. These results show that metric depth estimation can benefit from the same scaling laws that drive modern foundation models, establishing a new path toward scalable and efficient real-world metric perception. We open-source MetricAnything at http://metric-anything.github.io/metric-anything-io/ to support community research.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.22054">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.22054.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.22054.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">PLANING: A Loosely Coupled Triangle-Gaussian Framework for Streaming 3D Reconstruction</span>
        <span class="paper-authors">Changjian Jiang, Kerui Ren, Xudong Li, Kaiwen Song, Linning Xu, Tao Lu, Junting Dong, Yu Zhang, Bo Dai, Mulin Yu</span>
        <span class="paper-meta">Updated 2026-01-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Streaming reconstruction from monocular image sequences remains challenging, as existing methods typically favor either high-quality rendering or accurate geometry, but rarely both. We present PLANING, an efficient on-the-fly reconstruction framework built on a hybrid representation that loosely couples explicit geometric primitives with neural Gaussians, enabling geometry and appearance to be modeled in a decoupled manner. This decoupling supports an online initialization and optimization strategy that separates geometry and appearance updates, yielding stable streaming reconstruction with substantially reduced structural redundancy. PLANING improves dense mesh Chamfer-L2 by 18.52% over PGSR, surpasses ARTDECO by 1.31 dB PSNR, and reconstructs ScanNetV2 scenes in under 100 seconds, over 5x faster than 2D Gaussian Splatting, while matching the quality of offline per-scene optimization. Beyond reconstruction quality, the structural clarity and computational efficiency of \modelname~make it well suited for a broad range of downstream applications, such as enabling large-scale scene modeling and simulation-ready environments for embodied AI. Project page: https://city-super.github.io/PLANING/ .</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.22046">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.22046.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.22046.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Urban Neural Surface Reconstruction from Constrained Sparse Aerial Imagery with 3D SAR Fusion</span>
        <span class="paper-authors">Da Li, Chen Yao, Tong Mao, Jiacheng Bao, Houjun Sun</span>
        <span class="paper-meta">Updated 2026-01-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Neural surface reconstruction (NSR) has recently shown strong potential for urban 3D reconstruction from multi-view aerial imagery. However, existing NSR methods often suffer from geometric ambiguity and instability, particularly under sparse-view conditions. This issue is critical in large-scale urban remote sensing, where aerial image acquisition is limited by flight paths, terrain, and cost. To address this challenge, we present the first urban NSR framework that fuses 3D synthetic aperture radar (SAR) point clouds with aerial imagery for high-fidelity reconstruction under constrained, sparse-view settings. 3D SAR can efficiently capture large-scale geometry even from a single side-looking flight path, providing robust priors that complement photometric cues from images. Our framework integrates radar-derived spatial constraints into an SDF-based NSR backbone, guiding structure-aware ray selection and adaptive sampling for stable and efficient optimization. We also construct the first benchmark dataset with co-registered 3D SAR point clouds and aerial imagery, facilitating systematic evaluation of cross-modal 3D reconstruction. Extensive experiments show that incorporating 3D SAR markedly enhances reconstruction accuracy, completeness, and robustness compared with single-modality baselines under highly sparse and oblique-view conditions, highlighting a viable route toward scalable high-fidelity urban reconstruction with advanced airborne and spaceborne optical-SAR sensing.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.22045">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.22045.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.22045.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Synthetic-to-Real Domain Bridging for Single-View 3D Reconstruction of Ships for Maritime Monitoring</span>
        <span class="paper-authors">Borja Carrillo-Perez, Felix Sattler, Angel Bueno Rodriguez, Maurice Stephan, Sarah Barnes</span>
        <span class="paper-meta">Updated 2026-01-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Three-dimensional (3D) reconstruction of ships is an important part of maritime monitoring, allowing improved visualization, inspection, and decision-making in real-world monitoring environments. However, most state-ofthe-art 3D reconstruction methods require multi-view supervision, annotated 3D ground truth, or are computationally intensive, making them impractical for real-time maritime deployment. In this work, we present an efficient pipeline for single-view 3D reconstruction of real ships by training entirely on synthetic data and requiring only a single view at inference. Our approach uses the Splatter Image network, which represents objects as sparse sets of 3D Gaussians for rapid and accurate reconstruction from single images. The model is first fine-tuned on synthetic ShapeNet vessels and further refined with a diverse custom dataset of 3D ships, bridging the domain gap between synthetic and real-world imagery. We integrate a state-of-the-art segmentation module based on YOLOv8 and custom preprocessing to ensure compatibility with the reconstruction network. Postprocessing steps include real-world scaling, centering, and orientation alignment, followed by georeferenced placement on an interactive web map using AIS metadata and homography-based mapping. Quantitative evaluation on synthetic validation data demonstrates strong reconstruction fidelity, while qualitative results on real maritime images from the ShipSG dataset confirm the potential for transfer to operational maritime settings. The final system provides interactive 3D inspection of real ships without requiring real-world 3D annotations. This pipeline provides an efficient, scalable solution for maritime monitoring and highlights a path toward real-time 3D ship visualization in practical applications. Interactive demo: https://dlr-mi.github.io/ship3d-demo/.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.21786">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.21786.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.21786.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">From Implicit Ambiguity to Explicit Solidity: Diagnosing Interior Geometric Degradation in Neural Radiance Fields for Dense 3D Scene Understanding</span>
        <span class="paper-authors">Jiangsan Zhao, Jakob Geipel, Kryzysztof Kusnierek</span>
        <span class="paper-meta">Updated 2026-01-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Neural Radiance Fields (NeRFs) have emerged as a powerful paradigm for multi-view reconstruction, complementing classical photogrammetric pipelines based on Structure-from-Motion (SfM) and Multi-View Stereo (MVS). However, their reliability for quantitative 3D analysis in dense, self-occluding scenes remains poorly understood. In this study, we identify a fundamental failure mode of implicit density fields under heavy occlusion, which we term Interior Geometric Degradation (IGD). We show that transmittance-based volumetric optimization satisfies photometric supervision by reconstructing hollow or fragmented structures rather than solid interiors, leading to systematic instance undercounting. Through controlled experiments on synthetic datasets with increasing occlusion, we demonstrate that state-of-the-art mask-supervised NeRFs saturate at approximately 89% instance recovery in dense scenes, despite improved surface coherence and mask quality. To overcome this limitation, we introduce an explicit geometric pipeline based on Sparse Voxel Rasterization (SVRaster), initialized from SfM feature geometry. By projecting 2D instance masks onto an explicit voxel grid and enforcing geometric separation via recursive splitting, our approach preserves physical solidity and achieves a 95.8% recovery rate in dense clusters. A sensitivity analysis using degraded segmentation masks further shows that explicit SfM-based geometry is substantially more robust to supervision failure, recovering 43% more instances than implicit baselines. These results demonstrate that explicit geometric priors are a prerequisite for reliable quantitative analysis in highly self-occluding 3D scenes.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.21421">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.21421.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.21421.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">VersaQ-3D: A Reconfigurable Accelerator Enabling Feed-Forward and Generalizable 3D Reconstruction via Versatile Quantization</span>
        <span class="paper-authors">Yipu Zhang, Jintao Cheng, Xingyu Liu, Zeyu Li, Carol Jingyi Li, Jin Wu, Lin Jiang, Yuan Xie, Jiang Xu, Wei Zhang</span>
        <span class="paper-meta">Updated 2026-01-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">The Visual Geometry Grounded Transformer (VGGT) enables strong feed-forward 3D reconstruction without per-scene optimization. However, its billion-parameter scale creates high memory and compute demands, hindering on-device deployment. Existing LLM quantization methods fail on VGGT due to saturated activation channels and diverse 3D semantics, which cause unreliable calibration. Furthermore, VGGT presents hardware challenges regarding precision-sensitive nonlinear operators and memory-intensive global attention. To address this, we propose VersaQ-3D, an algorithm-architecture co-design framework. Algorithmically, we introduce the first calibration-free, scene-agnostic quantization for VGGT down to 4-bit, leveraging orthogonal transforms to decorrelate features and suppress outliers. Architecturally, we design a reconfigurable accelerator supporting BF16, INT8, and INT4. A unified systolic datapath handles both linear and nonlinear operators, reducing latency by 60%, while two-stage recomputation-based tiling alleviates memory pressure for long-sequence attention. Evaluations show VersaQ-3D preserves 98-99% accuracy at W4A8. At W4A4, it outperforms prior methods by 1.61x-2.39x across diverse scenes. The accelerator delivers 5.2x-10.8x speedup over edge GPUs with low power, enabling efficient instant 3D reconstruction.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.20317">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.20317.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.20317.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GeoDiff3D: Self-Supervised 3D Scene Generation with Geometry-Constrained 2D Diffusion Guidance</span>
        <span class="paper-authors">Haozhi Zhu, Miaomiao Zhao, Dingyao Liu, Runze Tian, Yan Zhang, Jie Guo, Fenggen Yu</span>
        <span class="paper-meta">Updated 2026-01-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">3D scene generation is a core technology for gaming, film/VFX, and VR/AR. Growing demand for rapid iteration, high-fidelity detail, and accessible content creation has further increased interest in this area. Existing methods broadly follow two paradigms - indirect 2D-to-3D reconstruction and direct 3D generation - but both are limited by weak structural modeling and heavy reliance on large-scale ground-truth supervision, often producing structural artifacts, geometric inconsistencies, and degraded high-frequency details in complex scenes. We propose GeoDiff3D, an efficient self-supervised framework that uses coarse geometry as a structural anchor and a geometry-constrained 2D diffusion model to provide texture-rich reference images. Importantly, GeoDiff3D does not require strict multi-view consistency of the diffusion-generated references and remains robust to the resulting noisy, inconsistent guidance. We further introduce voxel-aligned 3D feature aggregation and dual self-supervision to maintain scene coherence and fine details while substantially reducing dependence on labeled data. GeoDiff3D also trains with low computational cost and enables fast, high-quality 3D scene generation. Extensive experiments on challenging scenes show improved generalization and generation quality over existing baselines, offering a practical solution for accessible and efficient 3D scene construction.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.19785">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.19785.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.19785.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Size Matters: Reconstructing Real-Scale 3D Models from Monocular Images for Food Portion Estimation</span>
        <span class="paper-authors">Gautham Vinod, Bruce Coburn, Siddeshwar Raghavan, Jiangpeng He, Fengqing Zhu</span>
        <span class="paper-meta">Updated 2026-01-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">The rise of chronic diseases related to diet, such as obesity and diabetes, emphasizes the need for accurate monitoring of food intake. While AI-driven dietary assessment has made strides in recent years, the ill-posed nature of recovering size (portion) information from monocular images for accurate estimation of ``how much did you eat?&#x27;&#x27; is a pressing challenge. Some 3D reconstruction methods have achieved impressive geometric reconstruction but fail to recover the crucial real-world scale of the reconstructed object, limiting its usage in precision nutrition. In this paper, we bridge the gap between 3D computer vision and digital health by proposing a method that recovers a true-to-scale 3D reconstructed object from a monocular image. Our approach leverages rich visual features extracted from models trained on large-scale datasets to estimate the scale of the reconstructed object. This learned scale enables us to convert single-view 3D reconstructions into true-to-life, physically meaningful models. Extensive experiments and ablation studies on two publicly available datasets show that our method consistently outperforms existing techniques, achieving nearly a 30% reduction in mean absolute volume-estimation error, showcasing its potential to enhance the domain of precision nutrition. Code: https://gitlab.com/viper-purdue/size-matters</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.20051">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.20051.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.20051.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">WaterClear-GS: Optical-Aware Gaussian Splatting for Underwater Reconstruction and Restoration</span>
        <span class="paper-authors">Xinrui Zhang, Yufeng Wang, Shuangkang Fang, Zesheng Wang, Dacheng Qi, Wenrui Ding</span>
        <span class="paper-meta">Updated 2026-01-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Underwater 3D reconstruction and appearance restoration are hindered by the complex optical properties of water, such as wavelength-dependent attenuation and scattering. Existing Neural Radiance Fields (NeRF)-based methods struggle with slow rendering speeds and suboptimal color restoration, while 3D Gaussian Splatting (3DGS) inherently lacks the capability to model complex volumetric scattering effects. To address these issues, we introduce WaterClear-GS, the first pure 3DGS-based framework that explicitly integrates underwater optical properties of local attenuation and scattering into Gaussian primitives, eliminating the need for an auxiliary medium network. Our method employs a dual-branch optimization strategy to ensure underwater photometric consistency while naturally recovering water-free appearances. This strategy is enhanced by depth-guided geometry regularization and perception-driven image loss, together with exposure constraints, spatially-adaptive regularization, and physically guided spectral regularization, which collectively enforce local 3D coherence and maintain natural visual perception. Experiments on standard benchmarks and our newly collected dataset demonstrate that WaterClear-GS achieves outstanding performance on both novel view synthesis (NVS) and underwater image restoration (UIR) tasks, while maintaining real-time rendering. The code will be available at https://buaaxrzhang.github.io/WaterClear-GS/.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.19753">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.19753.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.19753.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">NuiWorld: Exploring a Scalable Framework for End-to-End Controllable World Generation</span>
        <span class="paper-authors">Han-Hung Lee, Cheng-Yu Yang, Yu-Lun Liu, Angel X. Chang</span>
        <span class="paper-meta">Updated 2026-01-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">World generation is a fundamental capability for applications like video games, simulation, and robotics. However, existing approaches face three main obstacles: controllability, scalability, and efficiency. End-to-end scene generation models have been limited by data scarcity. While object-centric generation approaches rely on fixed resolution representations, degrading fidelity for larger scenes. Training-free approaches, while flexible, are often slow and computationally expensive at inference time. We present NuiWorld, a framework that attempts to address these challenges. To overcome data scarcity, we propose a generative bootstrapping strategy that starts from a few input images. Leveraging recent 3D reconstruction and expandable scene generation techniques, we synthesize scenes of varying sizes and layouts, producing enough data to train an end-to-end model. Furthermore, our framework enables controllability through pseudo sketch labels, and demonstrates a degree of generalization to previously unseen sketches. Our approach represents scenes as a collection of variable scene chunks, which are compressed into a flattened vector-set representation. This significantly reduces the token length for large scenes, enabling consistent geometric fidelity across scenes sizes while improving training and inference efficiency.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.19048">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.19048.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.19048.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Three-dimensional visualization of X-ray micro-CT with large-scale datasets: Efficiency and accuracy for real-time interaction</span>
        <span class="paper-authors">Yipeng Yin, Rao Yao, Qingying Li, Dazhong Wang, Hong Zhou, Zhijun Fang, Jianing Chen, Longjie Qian, Mingyue Wu</span>
        <span class="paper-meta">Updated 2026-01-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">As Micro-CT technology continues to refine its characterization of material microstructures, industrial CT ultra-precision inspection is generating increasingly large datasets, necessitating solutions to the trade-off between accuracy and efficiency in the 3D characterization of defects during ultra-precise detection. This article provides a unique perspective on recent advances in accurate and efficient 3D visualization using Micro-CT, tracing its evolution from medical imaging to industrial non-destructive testing (NDT). Among the numerous CT reconstruction and volume rendering methods, this article selectively reviews and analyzes approaches that balance accuracy and efficiency, offering a comprehensive analysis to help researchers quickly grasp highly efficient and accurate 3D reconstruction methods for microscopic features. By comparing the principles of computed tomography with advancements in microstructural technology, this article examines the evolution of CT reconstruction algorithms from analytical methods to deep learning techniques, as well as improvements in volume rendering algorithms, acceleration, and data reduction. Additionally, it explores advanced lighting models for high-accuracy, photorealistic, and efficient volume rendering. Furthermore, this article envisions potential directions in CT reconstruction and volume rendering. It aims to guide future research in quickly selecting efficient and precise methods and developing new ideas and approaches for real-time online monitoring of internal material defects through virtual-physical interaction, for applying digital twin model to structural health monitoring (SHM).</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.15098">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.15098.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.15098.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Rig-Aware 3D Reconstruction of Vehicle Undercarriages using Gaussian Splatting</span>
        <span class="paper-authors">Nitin Kulkarni, Akhil Devarashetti, Charlie Cluss, Livio Forte, Dan Buckmaster, Philip Schneider, Chunming Qiao, Alina Vereshchaka</span>
        <span class="paper-meta">Updated 2026-01-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Inspecting the undercarriage of used vehicles is a labor-intensive task that requires inspectors to crouch or crawl underneath each vehicle to thoroughly examine it. Additionally, online buyers rarely see undercarriage photos. We present an end-to-end pipeline that utilizes a three-camera rig to capture videos of the undercarriage as the vehicle drives over it, and produces an interactive 3D model of the undercarriage. The 3D model enables inspectors and customers to rotate, zoom, and slice through the undercarriage, allowing them to detect rust, leaks, or impact damage in seconds, thereby improving both workplace safety and buyer confidence. Our primary contribution is a rig-aware Structure-from-Motion (SfM) pipeline specifically designed to overcome the challenges of wide-angle lens distortion and low-parallax scenes. Our method overcomes the challenges of wide-angle lens distortion and low-parallax scenes by integrating precise camera calibration, synchronized video streams, and strong geometric priors from the camera rig. We use a constrained matching strategy with learned components, the DISK feature extractor, and the attention-based LightGlue matcher to generate high-quality sparse point clouds that are often unattainable with standard SfM pipelines. These point clouds seed the Gaussian splatting process to generate photorealistic undercarriage models that render in real-time. Our experiments and ablation studies demonstrate that our design choices are essential to achieve state-of-the-art quality.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.14208">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.14208.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.14208.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ParkingTwin: Training-Free Streaming 3D Reconstruction for Parking-Lot Digital Twins</span>
        <span class="paper-authors">Xinhao Liu, Yu Wang, Xiansheng Guo, Gordon Owusu Boateng, Yu Cao, Haonan Si, Xingchen Guo, Nirwan Ansari</span>
        <span class="paper-meta">Updated 2026-01-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">High-fidelity parking-lot digital twins provide essential priors for path planning, collision checking, and perception validation in Automated Valet Parking (AVP). Yet robot-oriented reconstruction faces a trilemma: sparse forward-facing views cause weak parallax and ill-posed geometry; dynamic occlusions and extreme lighting hinder stable texture fusion; and neural rendering typically needs expensive offline optimization, violating edge-side streaming constraints. We propose ParkingTwin, a training-free, lightweight system for online streaming 3D reconstruction. First, OSM-prior-driven geometric construction uses OpenStreetMap semantic topology to directly generate a metric-consistent TSDF, replacing blind geometric search with deterministic mapping and avoiding costly optimization. Second, geometry-aware dynamic filtering employs a quad-modal constraint field (normal/height/depth consistency) to reject moving vehicles and transient occlusions in real time. Third, illumination-robust fusion in CIELAB decouples luminance and chromaticity via adaptive L-channel weighting and depth-gradient suppression, reducing seams under abrupt lighting changes. ParkingTwin runs at 30+ FPS on an entry-level GTX 1660. On a 68,000 m^2 real-world dataset, it achieves SSIM 0.87 (+16.0%), delivers about 15x end-to-end speedup, and reduces GPU memory by 83.3% compared with state-of-the-art 3D Gaussian Splatting (3DGS) that typically requires high-end GPUs (RTX 4090D). The system outputs explicit triangle meshes compatible with Unity/Unreal digital-twin pipelines. Project page: https://mihoutao-liu.github.io/ParkingTwin/</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.13706">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.13706.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.13706.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Three-dimensional properties of a coronal shock and the longitudinal distribution of its related solar energetic particles</span>
        <span class="paper-authors">Yue Zhou, Li Feng, Guanglu Shi, Jingnan Guo, Liuguan Ding, Yi Yang, Jianchao Xue, Jun Chen, Weiqun Gan</span>
        <span class="paper-meta">Updated 2026-01-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">This study aims to investigate the relationship between the spatial-temporal evolution of shock properties and the longitudinal dependence of SEP intensities and spectra. The shock parameters, including the normal speed, oblique angles, compression ratio, and Alfven Mach number, were derived by combining a steady-state solar-wind simulation with the three-dimensional (3D) reconstruction of the shock surface based on multi-view observations. We compared the local shock parameters at the magnetic connecting points with in situ proton intensities and peak spectra to establish the link between shock evolution and SEP characteristics. The shock nose consistently exhibited higher particle-acceleration efficiency with the largest normal speed, compression ratio, and supercritical Alfven Mach number, while the flanks showed delayed transition to supercritical Alfven Mach number with weaker efficiency. The earliest and most rapid proton enhancement of STEREO-B correlated with efficient shock acceleration and prompt magnetic connectivity to the shock. Spectral analysis revealed that proton energy spectra were consistent with the relativistic diffusive shock acceleration (DSA) estimations. The initial shock acceleration began at about 1.4-5 Rsun and caused the widespread longitudinal SEP distribution. The longitudinal dependence of SEP intensity and spectral variations arise from the combined influence of 3D shock properties, magnetic connectivity, and particle transport processes. The agreement between in situ proton indices and relativistic DSA estimations supports DSA in this SEP event and provides insights into the early-stage acceleration at the source region.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.13692">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.13692.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.13692.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DCCVT: Differentiable Clipped Centroidal Voronoi Tessellation</span>
        <span class="paper-authors">Wylliam Cantin Charawi, Adrien Gruson, Jane Wu, Christian Desrosiers, Diego Thomas</span>
        <span class="paper-meta">Updated 2026-01-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">While Marching Cubes (MC) and Marching Tetrahedra (MTet) are widely adopted in 3D reconstruction pipelines due to their simplicity and efficiency, their differentiable variants remain suboptimal for mesh extraction. This often limits the quality of 3D meshes reconstructed from point clouds or images in learning-based frameworks. In contrast, clipped CVTs offer stronger theoretical guarantees and yield higher-quality meshes. However, the lack of a differentiable formulation has prevented their integration into modern machine learning pipelines. To bridge this gap, we propose DCCVT, a differentiable algorithm that extracts high-quality 3D meshes from noisy signed distance fields (SDFs) using clipped CVTs. We derive a fully differentiable formulation for computing clipped CVTs and demonstrate its integration with deep learning-based SDF estimation to reconstruct accurate 3D meshes from input point clouds. Our experiments with synthetic data demonstrate the superior ability of DCCVT against state-of-the-art methods in mesh quality and reconstruction fidelity. https://wylliamcantincharawi.dev/DCCVT.github.io/</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.13603">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.13603.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.13603.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Think3D: Thinking with Space for Spatial Reasoning</span>
        <span class="paper-authors">Zaibin Zhang, Yuhan Wu, Lianjie Jia, Yifan Wang, Zhongbo Zhang, Yijiang Li, Binghao Ran, Fuxi Zhang, Zhuohan Sun, Zhenfei Yin, Lijun Wang, Huchuan Lu</span>
        <span class="paper-meta">Updated 2026-01-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Understanding and reasoning about the physical world requires spatial intelligence: the ability to interpret geometry, perspective, and spatial relations beyond 2D perception. While recent vision large models (VLMs) excel at visual understanding, they remain fundamentally 2D perceivers and struggle with genuine 3D reasoning. We introduce Think3D, a framework that enables VLM agents to think with 3D space. By leveraging 3D reconstruction models that recover point clouds and camera poses from images or videos, Think3D allows the agent to actively manipulate space through camera-based operations and ego/global-view switching, transforming spatial reasoning into an interactive 3D chain-of-thought process. Without additional training, Think3D significantly improves the spatial reasoning performance of advanced models such as GPT-4.1 and Gemini 2.5 Pro, yielding average gains of +7.8% on BLINK Multi-view and MindCube, and +4.7% on VSI-Bench. We further show that smaller models, which struggle with spatial exploration, benefit significantly from a reinforcement learning policy that enables the model to select informative viewpoints and operations. With RL, the benefit from tool usage increases from +0.7% to +6.8%. Our findings demonstrate that training-free, tool-augmented spatial exploration is a viable path toward more flexible and human-like 3D reasoning in multimodal agents, establishing a new dimension of multimodal intelligence. Code and weights are released at https://github.com/zhangzaibin/spagent.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.13029">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.13029.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.13029.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Generalizable and Animatable 3D Full-Head Gaussian Avatar from a Single Image</span>
        <span class="paper-authors">Shuling Zhao, Dan Xu</span>
        <span class="paper-meta">Updated 2026-01-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Building 3D animatable head avatars from a single image is an important yet challenging problem. Existing methods generally collapse under large camera pose variations, compromising the realism of 3D avatars. In this work, we propose a new framework to tackle the novel setting of one-shot 3D full-head animatable avatar reconstruction in a single feed-forward pass, enabling real-time animation and simultaneous 360$^\circ$ rendering views. To facilitate efficient animation control, we model 3D head avatars with Gaussian primitives embedded on the surface of a parametric face model within the UV space. To obtain knowledge of full-head geometry and textures, we leverage rich 3D full-head priors within a pretrained 3D generative adversarial network (GAN) for global full-head feature extraction and multi-view supervision. To increase the fidelity of the 3D reconstruction of the input image, we take advantage of the symmetric nature of the UV space and human faces to fuse local fine-grained input image features with the global full-head textures. Extensive experiments demonstrate the effectiveness of our method, achieving high-quality 3D full-head modeling as well as real-time animation, thereby improving the realism of 3D talking avatars.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.12770">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.12770.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.12770.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">NeuralFur: Animal Fur Reconstruction From Multi-View Images</span>
        <span class="paper-authors">Vanessa Sklyarova, Berna Kabadayi, Anastasios Yiannakidis, Giorgio Becherini, Michael J. Black, Justus Thies</span>
        <span class="paper-meta">Updated 2026-01-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Reconstructing realistic animal fur geometry from images is a challenging task due to the fine-scale details, self-occlusion, and view-dependent appearance of fur. In contrast to human hairstyle reconstruction, there are also no datasets that can be leveraged to learn a fur prior for different animals. In this work, we present a first multi-view-based method for high-fidelity 3D fur modeling of animals using a strand-based representation, leveraging the general knowledge of a vision language model. Given multi-view RGB images, we first reconstruct a coarse surface geometry using traditional multi-view stereo techniques. We then use a vision language model (VLM) system to retrieve information about the realistic length structure of the fur for each part of the body. We use this knowledge to construct the animal&#x27;s furless geometry and grow strands atop it. The fur reconstruction is supervised with both geometric and photometric losses computed from multi-view images. To mitigate orientation ambiguities stemming from the Gabor filters that are applied to the input images, we additionally utilize the VLM to guide the strands&#x27; growth direction and their relation to the gravity vector that we incorporate as a loss. With this new schema of using a VLM to guide 3D reconstruction from multi-view inputs, we show generalization across a variety of animals with different fur types. For additional results and code, please refer to https://neuralfur.is.tue.mpg.de.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.12481">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.12481.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.12481.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">OpenNavMap: Structure-Free Topometric Mapping via Large-Scale Collaborative Localization</span>
        <span class="paper-authors">Jianhao Jiao, Changkun Liu, Jingwen Yu, Boyi Liu, Qianyi Zhang, Yue Wang, Dimitrios Kanoulas</span>
        <span class="paper-meta">Updated 2026-01-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Scalable and maintainable map representations are fundamental to enabling large-scale visual navigation and facilitating the deployment of robots in real-world environments. While collaborative localization across multi-session mapping enhances efficiency, traditional structure-based methods struggle with high maintenance costs and fail in feature-less environments or under significant viewpoint changes typical of crowd-sourced data. To address this, we propose OPENNAVMAP, a lightweight, structure-free topometric system leveraging 3D geometric foundation models for on-demand reconstruction. Our method unifies dynamic programming-based sequence matching, geometric verification, and confidence-calibrated optimization to robust, coarse-to-fine submap alignment without requiring pre-built 3D models. Evaluations on the Map-Free benchmark demonstrate superior accuracy over structure-from-motion and regression baselines, achieving an average translation error of 0.62m. Furthermore, the system maintains global consistency across 15km of multi-session data with an absolute trajectory error below 3m for map merging. Finally, we validate practical utility through 12 successful autonomous image-goal navigation tasks on simulated and physical robots. Code and datasets will be publicly available in https://rpl-cs-ucl.github.io/OpenNavMap_page.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.12291">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.12291.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.12291.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Soft Shadow Diffusion (SSD): Physics-inspired Learning for 3D Computational Periscopy</span>
        <span class="paper-authors">Fadlullah Raji, John Murray-Bruce</span>
        <span class="paper-meta">Updated 2026-01-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Conventional imaging requires a line of sight to create accurate visual representations of a scene. In certain circumstances, however, obtaining a suitable line of sight may be impractical, dangerous, or even impossible. Non-line-of-sight (NLOS) imaging addresses this challenge by reconstructing the scene from indirect measurements. Recently, passive NLOS methods that use an ordinary photograph of the subtle shadow cast onto a visible wall by the hidden scene have gained interest. These methods are currently limited to 1D or low-resolution 2D color imaging or to localizing a hidden object whose shape is approximately known. Here, we generalize this class of methods and demonstrate a 3D reconstruction of a hidden scene from an ordinary NLOS photograph. To achieve this, we propose a novel reformulation of the light transport model that conveniently decomposes the hidden scene into \textit{light-occluding} and \textit{non-light-occluding} components to yield a separable non-linear least squares (SNLLS) inverse problem. We develop two solutions: A gradient-based optimization method and a physics-inspired neural network approach, which we call Soft Shadow diffusion (SSD). Despite the challenging ill-conditioned inverse problem encountered here, our approaches are effective on numerous 3D scenes in real experimental scenarios. Moreover, SSD is trained in simulation but generalizes well to unseen classes in simulation and real-world NLOS scenes. SSD also shows surprising robustness to noise and ambient illumination.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.12257">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.12257.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.12257.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Vision-as-Inverse-Graphics Agent via Interleaved Multimodal Reasoning</span>
        <span class="paper-authors">Shaofeng Yin, Jiaxin Ge, Zora Zhiruo Wang, Xiuyu Li, Michael J. Black, Trevor Darrell, Angjoo Kanazawa, Haiwen Feng</span>
        <span class="paper-meta">Updated 2026-01-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Vision-as-inverse-graphics, the concept of reconstructing an image as an editable graphics program is a long-standing goal of computer vision. Yet even strong VLMs aren&#x27;t able to achieve this in one-shot as they lack fine-grained spatial and physical grounding capability. Our key insight is that closing this gap requires interleaved multimodal reasoning through iterative execution and verification. Stemming from this, we present VIGA (Vision-as-Inverse-Graphic Agent) that starts from an empty world and reconstructs or edits scenes through a closed-loop write-run-render-compare-revise procedure. To support long-horizon reasoning, VIGA combines (i) a skill library that alternates generator and verifier roles and (ii) an evolving context memory that contains plans, code diffs, and render history. VIGA is task-agnostic as it doesn&#x27;t require auxiliary modules, covering a wide range of tasks such as 3D reconstruction, multi-step scene editing, 4D physical interaction, and 2D document editing, etc. Empirically, we found VIGA substantially improves one-shot baselines on BlenderGym (35.32%) and SlideBench (117.17%). Moreover, VIGA is also model-agnostic as it doesn&#x27;t require finetuning, enabling a unified protocol to evaluate heterogeneous foundation VLMs. To better support this protocol, we introduce BlenderBench, a challenging benchmark that stress-tests interleaved multimodal reasoning with graphics engine, where VIGA improves by 124.70%.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.11109">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.11109.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.11109.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SurfSLAM: Sim-to-Real Underwater Stereo Reconstruction For Real-Time SLAM</span>
        <span class="paper-authors">Onur Bagoren, Seth Isaacson, Sacchin Sundar, Yung-Ching Sun, Anja Sheppard, Haoyu Ma, Abrar Shariff, Ram Vasudevan, Katherine A. Skinner</span>
        <span class="paper-meta">Updated 2026-01-15</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Localization and mapping are core perceptual capabilities for underwater robots. Stereo cameras provide a low-cost means of directly estimating metric depth to support these tasks. However, despite recent advances in stereo depth estimation on land, computing depth from image pairs in underwater scenes remains challenging. In underwater environments, images are degraded by light attenuation, visual artifacts, and dynamic lighting conditions. Furthermore, real-world underwater scenes frequently lack rich texture useful for stereo depth estimation and 3D reconstruction. As a result, stereo estimation networks trained on in-air data cannot transfer directly to the underwater domain. In addition, there is a lack of real-world underwater stereo datasets for supervised training of neural networks. Poor underwater depth estimation is compounded in stereo-based Simultaneous Localization and Mapping (SLAM) algorithms, making it a fundamental challenge for underwater robot perception. To address these challenges, we propose a novel framework that enables sim-to-real training of underwater stereo disparity estimation networks using simulated data and self-supervised finetuning. We leverage our learned depth predictions to develop \algname, a novel framework for real-time underwater SLAM that fuses stereo cameras with IMU, barometric, and Doppler Velocity Log (DVL) measurements. Lastly, we collect a challenging real-world dataset of shipwreck surveys using an underwater robot. Our dataset features over 24,000 stereo pairs, along with high-quality, dense photogrammetry models and reference trajectories for evaluation. Through extensive experiments, we demonstrate the advantages of the proposed training approach on real-world data for improving stereo estimation in the underwater domain and for enabling accurate trajectory estimation and 3D reconstruction of complex shipwreck sites.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.10814">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.10814.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.10814.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Euclid preparation. 3D reconstruction of the cosmic web with simulated Euclid Deep spectroscopic samples</span>
        <span class="paper-authors">Euclid Collaboration, K. Kraljic, C. Laigle, M. Balogh, P. Jablonka, U. Kuchner, N. Malavasi, F. Sarron, C. Pichon, G. De Lucia, M. Bethermin, F. Durret, M. Fumagalli, C. Gouin, M. Magliocchetti, J. G. Sorce, O. Cucciati, F. Fontanot, M. Hirschmann, Y. Kang, M. Spinelli, N. Aghanim, A. Amara, S. Andreon, N. Auricchio, C. Baccigalupi, M. Baldi, S. Bardelli, A. Biviano, E. Branchini, M. Brescia, J. Brinchmann, S. Camera, G. Cañas-Herrera, V. Capobianco, C. Carbone, J. Carretero, R. Casas, S. Casas, F. J. Castander, M. Castellano, G. Castignani, S. Cavuoti, K. C. Chambers, A. Cimatti, C. Colodro-Conde, G. Congedo, C. J. Conselice, L. Conversi, Y. Copin, F. Courbin, H. M. Courtois, A. Da Silva, H. Degaudenzi, S. de la Torre, H. Dole, M. Douspis, F. Dubath, C. A. J. Duncan, X. Dupac, S. Dusini, S. Escoffier, M. Farina, R. Farinelli, S. Ferriol, F. Finelli, P. Fosalba, N. Fourmanoit, M. Frailis, E. Franceschi, M. Fumana, S. Galeotta, K. George, W. Gillard, B. Gillis, C. Giocoli, J. Gracia-Carpio, A. Grazian, F. Grupp, S. V. H. Haugan, W. Holmes, F. Hormuth, A. Hornstrup, K. Jahnke, M. Jhabvala, B. Joachimi, E. Keihänen, S. Kermiche, A. Kiessling, M. Kilbinger, B. Kubik, M. Kümmel, M. Kunz, H. Kurki-Suonio, A. M. C. Le Brun, S. Ligori, P. B. Lilje, V. Lindholm, I. Lloro, G. Mainetti, D. Maino, E. Maiorano, O. Mansutti, S. Marcin, O. Marggraf, M. Martinelli, N. Martinet, F. Marulli, R. Massey, S. Maurogordato, E. Medinaceli, S. Mei, Y. Mellier, M. Meneghetti, E. Merlin, G. Meylan, A. Mora, M. Moresco, L. Moscardini, R. Nakajima, C. Neissner, S. -M. Niemi, C. Padilla, S. Paltani, F. Pasian, K. Pedersen, W. J. Percival, V. Pettorino, S. Pires, G. Polenta, M. Poncet, L. A. Popa, L. Pozzetti, F. Raison, R. Rebolo, A. Renzi, J. Rhodes, G. Riccio, E. Romelli, M. Roncarelli, C. Rosset, E. Rossetti, R. Saglia, Z. Sakr, A. G. Sánchez, D. Sapone, B. Sartoris, P. Schneider, T. Schrabback, M. Scodeggio, A. Secroun, E. Sefusatti, G. Seidel, M. Seiffert, S. Serrano, P. Simon, C. Sirignano, G. Sirri, L. Stanco, J. Steinwagner, P. Tallada-Crespí, A. N. Taylor, H. I. Teplitz, I. Tereno, N. Tessore, S. Toft, R. Toledo-Moreo, F. Torradeflot, I. Tutusaus, L. Valenziano, J. Valiviita, T. Vassallo, G. Verdoes Kleijn, A. Veropalumbo, D. Vibert, Y. Wang, J. Weller, A. Zacchei, G. Zamorani, E. Zucca, V. Allevato, M. Ballardini, M. Bolzonella, E. Bozzo, C. Burigana, R. Cabanac, M. Calabrese, A. Cappi, D. Di Ferdinando, J. A. Escartin Vigo, L. Gabarra, W. G. Hartley, J. Martín-Fleitas, S. Matthew, N. Mauri, R. B. Metcalf, A. A. Nucita, A. Pezzotta, M. Pöntinen, C. Porciani, I. Risso, V. Scottez, M. Sereno, M. Tenti, M. Viel, M. Wiesmann, Y. Akrami, S. Alvi, I. T. Andika, S. Anselmi, M. Archidiacono, F. Atrio-Barandela, A. Balaguera-Antolinez, P. Bergamini, D. Bertacca, A. Blanchard, L. Blot, H. Böhringer, S. Borgani, M. L. Brown, S. Bruton, A. Calabro, B. Camacho Quevedo, F. Caro, C. S. Carvalho, T. Castro, R. Chary, F. Cogato, S. Conseil, T. Contini, A. R. Cooray, S. Davini, F. De Paolis, G. Desprez, A. Díaz-Sánchez, J. J. Diaz, S. Di Domizio, J. M. Diego, P. Dimauro, P. -A. Duc, A. Enia, Y. Fang, A. G. Ferrari, A. Finoguenov, A. Fontana, A. Franco, K. Ganga, J. García-Bellido, T. Gasparetto, R. Gavazzi, E. Gaztanaga, F. Giacomini, F. Gianotti, G. Gozaliasl, M. Guidi, C. M. Gutierrez, A. Hall, H. Hildebrandt, J. Hjorth, S. Joudaki, J. J. E. Kajava, V. Kansal, D. Karagiannis, K. Kiiveri, C. C. Kirkpatrick, S. Kruk, M. Lattanzi, V. Le Brun, J. Le Graet, L. Legrand, M. Lembo, F. Lepori, G. Leroy, G. F. Lesci, J. Lesgourgues, L. Leuzzi, T. I. Liaudat, S. J. Liu, A. Loureiro, J. Macias-Perez, G. Maggio, E. A. Magnier, F. Mannucci, R. Maoli, C. J. A. P. Martins, L. Maurin, M. Miluzio, P. Monaco, C. Moretti, G. Morgante, S. Nadathur, K. Naidoo, A. Navarro-Alsina, S. Nesseris, L. Pagano, F. Passalacqua, K. Paterson, L. Patrizii, A. Pisani, D. Potter, S. Quai, M. Radovich, P. -F. Rocci, G. Rodighiero, S. Sacquegna, M. Sahlén, D. B. Sanders, A. Schneider, D. Sciotti, E. Sellentin, L. C. Smith, K. Tanidis, C. Tao, G. Testera, R. Teyssier, S. Tosi, A. Troja, M. Tucci, C. Valieri, A. Venhola, D. Vergani, G. Verza, P. Vielzeuf, N. A. Walton</span>
        <span class="paper-meta">Updated 2026-01-15</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">The ongoing Euclid mission aims to measure spectroscopic redshifts for approximately two million galaxies using the H $α$ line emission detected in near-infrared slitless spectroscopic data from the Euclid Deep Fields (EDFs). These measurements will reach a flux limit of $5\times 10^{-17}\,{\rm erg}\,{\rm cm}^{-2}\,{\rm s}^{-1}$ in the redshift range $0.4&lt;z&lt;1.8$, opening the door to numerous investigations involving galaxy evolution, extending well beyond the mission&#x27;s core objectives. The achieved H $α$ luminosity depth will lead to a sufficiently high sampling, enabling the reconstruction of the large-scale galaxy environment. We assess the quality of the reconstruction of the galaxy cosmic web environment with the expected spectroscopic dataset in EDFs. The analysis is carried out on the Flagship and GAEA galaxy mock catalogues. The quality of the reconstruction is first evaluated using geometrical and topological statistics measured on the cosmic web, namely the length of filaments, the area of walls, the volume of voids, and its connectivity and multiplicity. We then quantify how accurately gradients in galaxy properties with distance from filaments can be recovered. As expected, the small-scale redshift-space distortions, have a strong impact on filament lengths and connectivity, but can be mitigated by compressing galaxy groups before skeleton extraction. The cosmic web reconstruction is biased when relying solely on H $α$ emitters. This limitation can be mitigated by applying stellar mass weighting during the reconstruction. However, this approach introduces non-trivial biases that need to be accounted for when comparing to theoretical predictions. Redshift uncertainties pose the greatest challenge in recovering the expected dependence of galaxy properties, though the well-established stellar mass transverse gradients towards filaments can still be observed.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.10709">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.10709.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.10709.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SPARK: Scalable Real-Time Point Cloud Aggregation with Multi-View Self-Calibration</span>
        <span class="paper-authors">Chentian Sun</span>
        <span class="paper-meta">Updated 2026-01-15</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Real-time multi-camera 3D reconstruction is crucial for 3D perception, immersive interaction, and robotics. Existing methods struggle with multi-view fusion, camera extrinsic uncertainty, and scalability for large camera setups. We propose SPARK, a self-calibrating real-time multi-camera point cloud reconstruction framework that jointly handles point cloud fusion and extrinsic uncertainty. SPARK consists of: (1) a geometry-aware online extrinsic estimation module leveraging multi-view priors and enforcing cross-view and temporal consistency for stable self-calibration, and (2) a confidence-driven point cloud fusion strategy modeling depth reliability and visibility at pixel and point levels to suppress noise and view-dependent inconsistencies. By performing frame-wise fusion without accumulation, SPARK produces stable point clouds in dynamic scenes while scaling linearly with the number of cameras. Extensive experiments on real-world multi-camera systems show that SPARK outperforms existing approaches in extrinsic accuracy, geometric consistency, temporal stability, and real-time performance, demonstrating its effectiveness and scalability for large-scale multi-camera 3D reconstruction.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.08414">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.08414.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.08414.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Efficient Camera-Controlled Video Generation of Static Scenes via Sparse Diffusion and 3D Rendering</span>
        <span class="paper-authors">Jieying Chen, Jeffrey Hu, Joan Lasenby, Ayush Tewari</span>
        <span class="paper-meta">Updated 2026-01-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Modern video generative models based on diffusion models can produce very realistic clips, but they are computationally inefficient, often requiring minutes of GPU time for just a few seconds of video. This inefficiency poses a critical barrier to deploying generative video in applications that require real-time interactions, such as embodied AI and VR/AR. This paper explores a new strategy for camera-conditioned video generation of static scenes: using diffusion-based generative models to generate a sparse set of keyframes, and then synthesizing the full video through 3D reconstruction and rendering. By lifting keyframes into a 3D representation and rendering intermediate views, our approach amortizes the generation cost across hundreds of frames while enforcing geometric consistency. We further introduce a model that predicts the optimal number of keyframes for a given camera trajectory, allowing the system to adaptively allocate computation. Our final method, SRENDER, uses very sparse keyframes for simple trajectories and denser ones for complex camera motion. This results in video generation that is more than 40 times faster than the diffusion-based baseline in generating 20 seconds of video, while maintaining high visual fidelity and temporal stability, offering a practical path toward efficient and controllable video synthesis.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.09697">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.09697.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.09697.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SCE-SLAM: Scale-Consistent Monocular SLAM via Scene Coordinate Embeddings</span>
        <span class="paper-authors">Yuchen Wu, Jiahe Li, Xiaohan Yu, Lina Yu, Jin Zheng, Xiao Bai</span>
        <span class="paper-meta">Updated 2026-01-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Monocular visual SLAM enables 3D reconstruction from internet video and autonomous navigation on resource-constrained platforms, yet suffers from scale drift, i.e., the gradual divergence of estimated scale over long sequences. Existing frame-to-frame methods achieve real-time performance through local optimization but accumulate scale drift due to the lack of global constraints among independent windows. To address this, we propose SCE-SLAM, an end-to-end SLAM system that maintains scale consistency through scene coordinate embeddings, which are learned patch-level representations encoding 3D geometric relationships under a canonical scale reference. The framework consists of two key modules: geometry-guided aggregation that leverages 3D spatial proximity to propagate scale information from historical observations through geometry-modulated attention, and scene coordinate bundle adjustment that anchors current estimates to the reference scale through explicit 3D coordinate constraints decoded from the scene coordinate embeddings. Experiments on KITTI, Waymo, and vKITTI demonstrate substantial improvements: our method reduces absolute trajectory error by 8.36m on KITTI compared to the best prior approach, while maintaining 36 FPS and achieving scale consistency across large-scale scenes.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.09665">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.09665.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.09665.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">V-DPM: 4D Video Reconstruction with Dynamic Point Maps</span>
        <span class="paper-authors">Edgar Sucar, Eldar Insafutdinov, Zihang Lai, Andrea Vedaldi</span>
        <span class="paper-meta">Updated 2026-01-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Powerful 3D representations such as DUSt3R invariant point maps, which encode 3D shape and camera parameters, have significantly advanced feed forward 3D reconstruction. While point maps assume static scenes, Dynamic Point Maps (DPMs) extend this concept to dynamic 3D content by additionally representing scene motion. However, existing DPMs are limited to image pairs and, like DUSt3R, require post processing via optimization when more than two views are involved. We argue that DPMs are more useful when applied to videos and introduce V-DPM to demonstrate this. First, we show how to formulate DPMs for video input in a way that maximizes representational power, facilitates neural prediction, and enables reuse of pretrained models. Second, we implement these ideas on top of VGGT, a recent and powerful 3D reconstructor. Although VGGT was trained on static scenes, we show that a modest amount of synthetic data is sufficient to adapt it into an effective V-DPM predictor. Our approach achieves state of the art performance in 3D and 4D reconstruction for dynamic scenes. In particular, unlike recent dynamic extensions of VGGT such as P3, DPMs recover not only dynamic depth but also the full 3D motion of every point in the scene.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.09499">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.09499.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.09499.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Affostruction: 3D Affordance Grounding with Generative Reconstruction</span>
        <span class="paper-authors">Chunghyun Park, Seunghyeon Lee, Minsu Cho</span>
        <span class="paper-meta">Updated 2026-01-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">This paper addresses the problem of affordance grounding from RGBD images of an object, which aims to localize surface regions corresponding to a text query that describes an action on the object. While existing methods predict affordance regions only on visible surfaces, we propose Affostruction, a generative framework that reconstructs complete geometry from partial observations and grounds affordances on the full shape including unobserved regions. We make three core contributions: generative multi-view reconstruction via sparse voxel fusion that extrapolates unseen geometry while maintaining constant token complexity, flow-based affordance grounding that captures inherent ambiguity in affordance distributions, and affordance-driven active view selection that leverages predicted affordances for intelligent viewpoint sampling. Affostruction achieves 19.1 aIoU on affordance grounding (40.4\% improvement) and 32.67 IoU for 3D reconstruction (67.7\% improvement), enabling accurate affordance prediction on complete shapes.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.09211">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.09211.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.09211.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Second-order Gaussian directional derivative representations for image high-resolution corner detection</span>
        <span class="paper-authors">Dongbo Xie, Junjie Qiu, Changming Sun, Weichuan Zhang</span>
        <span class="paper-meta">Updated 2026-01-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Corner detection is widely used in various computer vision tasks, such as image matching and 3D reconstruction. Our research indicates that there are theoretical flaws in Zhang et al.&#x27;s use of a simple corner model to obtain a series of corner characteristics, as the grayscale information of two adjacent corners can affect each other. In order to address the above issues, a second-order Gaussian directional derivative (SOGDD) filter is used in this work to smooth two typical high-resolution angle models (i.e. END-type and L-type models). Then, the SOGDD representations of these two corner models were derived separately, and many characteristics of high-resolution corners were discovered, which enabled us to demonstrate how to select Gaussian filtering scales to obtain intensity variation information from images, accurately depicting adjacent corners. In addition, a new high-resolution corner detection method for images has been proposed for the first time, which can accurately detect adjacent corner points. The experimental results have verified that the proposed method outperforms state-of-the-art methods in terms of localization error, robustness to image blur transformation, image matching, and 3D reconstruction.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.08182">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.08182.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.08182.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ViewMorpher3D: A 3D-aware Diffusion Framework for Multi-Camera Novel View Synthesis in Autonomous Driving</span>
        <span class="paper-authors">Farhad G. Zanjani, Hong Cai, Amirhossein Habibian</span>
        <span class="paper-meta">Updated 2026-01-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Autonomous driving systems rely heavily on multi-view images to ensure accurate perception and robust decision-making. To effectively develop and evaluate perception stacks and planning algorithms, realistic closed-loop simulators are indispensable. While 3D reconstruction techniques such as Gaussian Splatting offer promising avenues for simulator construction, the rendered novel views often exhibit artifacts, particularly in extrapolated perspectives or when available observations are sparse.   We introduce ViewMorpher3D, a multi-view image enhancement framework based on image diffusion models, designed to elevate photorealism and multi-view coherence in driving scenes. Unlike single-view approaches, ViewMorpher3D jointly processes a set of rendered views conditioned on camera poses, 3D geometric priors, and temporally adjacent or spatially overlapping reference views. This enables the model to infer missing details, suppress rendering artifacts, and enforce cross-view consistency.   Our framework accommodates variable numbers of cameras and flexible reference/target view configurations, making it adaptable to diverse sensor setups. Experiments on real-world driving datasets demonstrate substantial improvements in image quality metrics, effectively reducing artifacts while preserving geometric fidelity.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.07540">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.07540.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.07540.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">HERE: Hierarchical Active Exploration of Radiance Field with Epistemic Uncertainty Minimization</span>
        <span class="paper-authors">Taekbeom Lee, Dabin Kim, Youngseok Jang, H. Jin Kim</span>
        <span class="paper-meta">Updated 2026-01-12</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We present HERE, an active 3D scene reconstruction framework based on neural radiance fields, enabling high-fidelity implicit mapping. Our approach centers around an active learning strategy for camera trajectory generation, driven by accurate identification of unseen regions, which supports efficient data acquisition and precise scene reconstruction. The key to our approach is epistemic uncertainty quantification based on evidential deep learning, which directly captures data insufficiency and exhibits a strong correlation with reconstruction errors. This allows our framework to more reliably identify unexplored or poorly reconstructed regions compared to existing methods, leading to more informed and targeted exploration. Additionally, we design a hierarchical exploration strategy that leverages learned epistemic uncertainty, where local planning extracts target viewpoints from high-uncertainty voxels based on visibility for trajectory generation, and global planning uses uncertainty to guide large-scale coverage for efficient and comprehensive reconstruction. The effectiveness of the proposed method in active 3D reconstruction is demonstrated by achieving higher reconstruction completeness compared to previous approaches on photorealistic simulated scenes across varying scales, while a hardware demonstration further validates its real-world applicability.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.07242">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.07242.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.07242.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">PRISM: Color-Stratified Point Cloud Sampling</span>
        <span class="paper-authors">Hansol Lim, Minhyeok Im, Jongseong Brad Choi</span>
        <span class="paper-meta">Updated 2026-01-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We present PRISM, a novel color-guided stratified sampling method for RGB-LiDAR point clouds. Our approach is motivated by the observation that unique scene features often exhibit chromatic diversity while repetitive, redundant features are homogeneous in color. Conventional downsampling methods (Random Sampling, Voxel Grid, Normal Space Sampling) enforce spatial uniformity while ignoring this photometric content. In contrast, PRISM allocates sampling density proportional to chormatic diversity. By treating RGB color space as the stratification domain and imposing a maximum capacity k per color bin, the method preserves texture-rich regions with high color variation while substantially reducing visually homogeneous surfaces. This shifts the sampling space from spatial coverage to visual complexity to produce sparser point clouds that retain essential features for 3D reconstruction tasks.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.06839">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.06839.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.06839.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SARA: Scene-Aware Reconstruction Accelerator</span>
        <span class="paper-authors">Jee Won Lee, Hansol Lim, Minhyeok Im, Dohyeon Lee, Jongseong Brad Choi</span>
        <span class="paper-meta">Updated 2026-01-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We present SARA (Scene-Aware Reconstruction Accelerator), a geometry-driven pair selection module for Structure-from-Motion (SfM). Unlike conventional pipelines that select pairs based on visual similarity alone, SARA introduces geometry-first pair selection by scoring reconstruction informativeness - the product of overlap and parallax - before expensive matching. A lightweight pre-matching stage uses mutual nearest neighbors and RANSAC to estimate these cues, then constructs an Information-Weighted Spanning Tree (IWST) augmented with targeted edges for loop closure, long-baseline anchors, and weak-view reinforcement. Compared to exhaustive matching, SARA reduces rotation errors by 46.5+-5.5% and translation errors by 12.5+-6.5% across modern learned detectors, while achieving at most 50x speedup through 98% pair reduction (from 30,848 to 580 pairs). This reduces matching complexity from quadratic to quasi-linear, maintaining within +-3% of baseline reconstruction metrics for 3D Gaussian Splatting and SVRaster.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.06831">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.06831.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.06831.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MoE3D: A Mixture-of-Experts Module for 3D Reconstruction</span>
        <span class="paper-authors">Zichen Wang, Ang Cao, Liam J. Wang, Jeong Joon Park</span>
        <span class="paper-meta">Updated 2026-01-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">MoE3D is a mixture-of-experts module designed to sharpen depth boundaries and mitigate flying-point artifacts (highlighted in red) of existing feed-forward 3D reconstruction models (left side). MoE3D predicts multiple candidate depth maps and fuses them via dynamic weighting (visualized by MoE weights on the right side). When integrated with a pre-trained 3D reconstruction backbone such as VGGT, it substantially enhances reconstruction quality with minimal additional computational overhead. Best viewed digitally.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.05208">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.05208.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.05208.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Segmentation-Driven Monocular Shape from Polarization based on Physical Model</span>
        <span class="paper-authors">Jinyu Zhang, Xu Ma, Weili Chen, Gonzalo R. Arce</span>
        <span class="paper-meta">Updated 2026-01-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Monocular shape-from-polarization (SfP) leverages the intrinsic relationship between light polarization properties and surface geometry to recover surface normals from single-view polarized images, providing a compact and robust approach for three-dimensional (3D) reconstruction. Despite its potential, existing monocular SfP methods suffer from azimuth angle ambiguity, an inherent limitation of polarization analysis, that severely compromises reconstruction accuracy and stability. This paper introduces a novel segmentation-driven monocular SfP (SMSfP) framework that reformulates global shape recovery into a set of local reconstructions over adaptively segmented convex sub-regions. Specifically, a polarization-aided adaptive region growing (PARG) segmentation strategy is proposed to decompose the global convexity assumption into locally convex regions, effectively suppressing azimuth ambiguities and preserving surface continuity. Furthermore, a multi-scale fusion convexity prior (MFCP) constraint is developed to ensure local surface consistency and enhance the recovery of fine textural and structural details. Extensive experiments on both synthetic and real-world datasets validate the proposed approach, showing significant improvements in disambiguation accuracy and geometric fidelity compared with existing physics-based monocular SfP techniques.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.04776">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.04776.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.04776.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">360-GeoGS: Geometrically Consistent Feed-Forward 3D Gaussian Splatting Reconstruction for 360 Images</span>
        <span class="paper-authors">Jiaqi Yao, Zhongmiao Yan, Jingyi Xu, Songpengcheng Xia, Yan Xiang, Ling Pei</span>
        <span class="paper-meta">Updated 2026-01-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">3D scene reconstruction is fundamental for spatial intelligence applications such as AR, robotics, and digital twins. Traditional multi-view stereo struggles with sparse viewpoints or low-texture regions, while neural rendering approaches, though capable of producing high-quality results, require per-scene optimization and lack real-time efficiency. Explicit 3D Gaussian Splatting (3DGS) enables efficient rendering, but most feed-forward variants focus on visual quality rather than geometric consistency, limiting accurate surface reconstruction and overall reliability in spatial perception tasks. This paper presents a novel feed-forward 3DGS framework for 360 images, capable of generating geometrically consistent Gaussian primitives while maintaining high rendering quality. A Depth-Normal geometric regularization is introduced to couple rendered depth gradients with normal information, supervising Gaussian rotation, scale, and position to improve point cloud and surface accuracy. Experimental results show that the proposed method maintains high rendering quality while significantly improving geometric consistency, providing an effective solution for 3D reconstruction in spatial perception tasks.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.02102">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.02102.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.02102.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">EdgeNeRF: Edge-Guided Regularization for Neural Radiance Fields from Sparse Views</span>
        <span class="paper-authors">Weiqi Yu, Yiyang Yao, Lin He, Jianming Lv</span>
        <span class="paper-meta">Updated 2026-01-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Neural Radiance Fields (NeRF) achieve remarkable performance in dense multi-view scenarios, but their reconstruction quality degrades significantly under sparse inputs due to geometric artifacts. Existing methods utilize global depth regularization to mitigate artifacts, leading to the loss of geometric boundary details. To address this problem, we propose EdgeNeRF, an edge-guided sparse-view 3D reconstruction algorithm. Our method leverages the prior that abrupt changes in depth and normals generate edges. Specifically, we first extract edges from input images, then apply depth and normal regularization constraints to non-edge regions, enhancing geometric consistency while preserving high-frequency details at boundaries. Experiments on LLFF and DTU datasets demonstrate EdgeNeRF&#x27;s superior performance, particularly in retaining sharp geometric boundaries and suppressing artifacts. Additionally, the proposed edge-guided depth regularization module can be seamlessly integrated into other methods in a plug-and-play manner, significantly improving their performance without substantially increasing training time. Code is available at https://github.com/skyhigh404/edgenerf.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.01431">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.01431.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.01431.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ParkGaussian: Surround-view 3D Gaussian Splatting for Autonomous Parking</span>
        <span class="paper-authors">Xiaobao Wei, Zhangjie Ye, Yuxiang Gu, Zunjie Zhu, Yunfei Guo, Yingying Shen, Shan Zhao, Ming Lu, Haiyang Sun, Bing Wang, Guang Chen, Rongfeng Lu, Hangjun Ye</span>
        <span class="paper-meta">Updated 2026-01-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Parking is a critical task for autonomous driving systems (ADS), with unique challenges in crowded parking slots and GPS-denied environments. However, existing works focus on 2D parking slot perception, mapping, and localization, 3D reconstruction remains underexplored, which is crucial for capturing complex spatial geometry in parking scenarios. Naively improving the visual quality of reconstructed parking scenes does not directly benefit autonomous parking, as the key entry point for parking is the slots perception module. To address these limitations, we curate the first benchmark named ParkRecon3D, specifically designed for parking scene reconstruction. It includes sensor data from four surround-view fisheye cameras with calibrated extrinsics and dense parking slot annotations. We then propose ParkGaussian, the first framework that integrates 3D Gaussian Splatting (3DGS) for parking scene reconstruction. To further improve the alignment between reconstruction and downstream parking slot detection, we introduce a slot-aware reconstruction strategy that leverages existing parking perception methods to enhance the synthesis quality of slot regions. Experiments on ParkRecon3D demonstrate that ParkGaussian achieves state-of-the-art reconstruction quality and better preserves perception consistency for downstream tasks. The code and dataset will be released at: https://github.com/wm-research/ParkGaussian</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.01386">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.01386.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.01386.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ShadowGS: Shadow-Aware 3D Gaussian Splatting for Satellite Imagery</span>
        <span class="paper-authors">Feng Luo, Hongbo Pan, Xiang Yang, Baoyu Jiang, Fengqing Liu, Tao Huang</span>
        <span class="paper-meta">Updated 2026-01-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">3D Gaussian Splatting (3DGS) has emerged as a novel paradigm for 3D reconstruction from satellite imagery. However, in multi-temporal satellite images, prevalent shadows exhibit significant inconsistencies due to varying illumination conditions. To address this, we propose ShadowGS, a novel framework based on 3DGS. It leverages a physics-based rendering equation from remote sensing, combined with an efficient ray marching technique, to precisely model geometrically consistent shadows while maintaining efficient rendering. Additionally, it effectively disentangles different illumination components and apparent attributes in the scene. Furthermore, we introduce a shadow consistency constraint that significantly enhances the geometric accuracy of 3D reconstruction. We also incorporate a novel shadow map prior to improve performance with sparse-view inputs. Extensive experiments demonstrate that ShadowGS outperforms current state-of-the-art methods in shadow decoupling accuracy, 3D reconstruction precision, and novel view synthesis quality, with only a few minutes of training. ShadowGS exhibits robust performance across various settings, including RGB, pansharpened, and sparse-view satellite inputs.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.00939">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.00939.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.00939.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">VISO: Robust Underwater Visual-Inertial-Sonar SLAM with Photometric Rendering for Dense 3D Reconstruction</span>
        <span class="paper-authors">Shu Pan, Simon Archieri, Ahmet Cinar, Jonatan Scharff Willners, Ignacio Carlucho, Yvan Petillot</span>
        <span class="paper-meta">Updated 2026-01-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Visual challenges in underwater environments significantly hinder the accuracy of vision-based localisation and the high-fidelity dense reconstruction. In this paper, we propose VISO, a robust underwater SLAM system that fuses a stereo camera, an inertial measurement unit (IMU), and a 3D sonar to achieve accurate 6-DoF localisation and enable efficient dense 3D reconstruction with high photometric fidelity. We introduce a coarse-to-fine online calibration approach for extrinsic parameters estimation between the 3D sonar and the camera. Additionally, a photometric rendering strategy is proposed for the 3D sonar point cloud to enrich the sonar map with visual information. Extensive experiments in a laboratory tank and an open lake demonstrate that VISO surpasses current state-of-the-art underwater and visual-based SLAM algorithms in terms of localisation robustness and accuracy, while also exhibiting real-time dense 3D reconstruction performance comparable to the offline dense mapping method.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.01144">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.01144.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.01144.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GaMO: Geometry-aware Multi-view Diffusion Outpainting for Sparse-View 3D Reconstruction</span>
        <span class="paper-authors">Yi-Chuan Huang, Hao-Jen Chien, Chin-Yang Lin, Ying-Huan Chen, Yu-Lun Liu</span>
        <span class="paper-meta">Updated 2025-12-31</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Recent advances in 3D reconstruction have achieved remarkable progress in high-quality scene capture from dense multi-view imagery, yet struggle when input views are limited. Various approaches, including regularization techniques, semantic priors, and geometric constraints, have been implemented to address this challenge. Latest diffusion-based methods have demonstrated substantial improvements by generating novel views from new camera poses to augment training data, surpassing earlier regularization and prior-based techniques. Despite this progress, we identify three critical limitations in these state-of-the-art approaches: inadequate coverage beyond known view peripheries, geometric inconsistencies across generated views, and computationally expensive pipelines. We introduce GaMO (Geometry-aware Multi-view Outpainter), a framework that reformulates sparse-view reconstruction through multi-view outpainting. Instead of generating new viewpoints, GaMO expands the field of view from existing camera poses, which inherently preserves geometric consistency while providing broader scene coverage. Our approach employs multi-view conditioning and geometry-aware denoising strategies in a zero-shot manner without training. Extensive experiments on Replica and ScanNet++ demonstrate state-of-the-art reconstruction quality across 3, 6, and 9 input views, outperforming prior methods in PSNR and LPIPS, while achieving a $25\times$ speedup over SOTA diffusion-based methods with processing time under 10 minutes. Project page: https://yichuanh.github.io/GaMO/</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.25073">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.25073.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.25073.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">3D Semantic Segmentation for Post-Disaster Assessment</span>
        <span class="paper-authors">Nhut Le, Maryam Rahnemoonfar</span>
        <span class="paper-meta">Updated 2025-12-31</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">The increasing frequency of natural disasters poses severe threats to human lives and leads to substantial economic losses. While 3D semantic segmentation is crucial for post-disaster assessment, existing deep learning models lack datasets specifically designed for post-disaster environments. To address this gap, we constructed a specialized 3D dataset using unmanned aerial vehicles (UAVs)-captured aerial footage of Hurricane Ian (2022) over affected areas, employing Structure-from-Motion (SfM) and Multi-View Stereo (MVS) techniques to reconstruct 3D point clouds. We evaluated the state-of-the-art (SOTA) 3D semantic segmentation models, Fast Point Transformer (FPT), Point Transformer v3 (PTv3), and OA-CNNs on this dataset, exposing significant limitations in existing methods for disaster-stricken regions. These findings underscore the urgent need for advancements in 3D segmentation techniques and the development of specialized 3D benchmark datasets to improve post-disaster scene understanding and response.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.24593">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.24593.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.24593.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">RANGER: A Monocular Zero-Shot Semantic Navigation Framework through Contextual Adaptation</span>
        <span class="paper-authors">Ming-Ming Yu, Yi Chen, Börje F. Karlsson, Wenjun Wu</span>
        <span class="paper-meta">Updated 2025-12-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Efficiently finding targets in complex environments is fundamental to real-world embodied applications. While recent advances in multimodal foundation models have enabled zero-shot object goal navigation, allowing robots to search for arbitrary objects without fine-tuning, existing methods face two key limitations: (1) heavy reliance on precise depth and pose information provided by simulators, which restricts applicability in real-world scenarios; and (2) lack of in-context learning (ICL) capability, making it difficult to quickly adapt to new environments, as in leveraging short videos. To address these challenges, we propose RANGER, a novel zero-shot, open-vocabulary semantic navigation framework that operates using only a monocular camera. Leveraging powerful 3D foundation models, RANGER eliminates the dependency on depth and pose while exhibiting strong ICL capability. By simply observing a short video of a new environment, the system can also significantly improve task efficiency without requiring architectural modifications or fine-tuning. The framework integrates several key components: keyframe-based 3D reconstruction, semantic point cloud generation, vision-language model (VLM)-driven exploration value estimation, high-level adaptive waypoint selection, and low-level action execution. Experiments on the HM3D benchmark and real-world environments demonstrate that RANGER achieves competitive performance in terms of navigation success rate and exploration efficiency, while showing superior ICL adaptability, with no previous 3D mapping of the environment required.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.24212">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.24212.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.24212.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">RealX3D: A Physically-Degraded 3D Benchmark for Multi-view Visual Restoration and Reconstruction</span>
        <span class="paper-authors">Shuhong Liu, Chenyu Bao, Ziteng Cui, Yun Liu, Xuangeng Chu, Lin Gu, Marcos V. Conde, Ryo Umagami, Tomohiro Hashimoto, Zijian Hu, Tianhan Xu, Yuan Gan, Yusuke Kurose, Tatsuya Harada</span>
        <span class="paper-meta">Updated 2025-12-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We introduce RealX3D, a real-capture benchmark for multi-view visual restoration and 3D reconstruction under diverse physical degradations. RealX3D groups corruptions into four families, including illumination, scattering, occlusion, and blurring, and captures each at multiple severity levels using a unified acquisition protocol that yields pixel-aligned LQ/GT views. Each scene includes high-resolution capture, RAW images, and dense laser scans, from which we derive world-scale meshes and metric depth. Benchmarking a broad range of optimization-based and feed-forward methods shows substantial degradation in reconstruction quality under physical corruptions, underscoring the fragility of current multi-view pipelines in real-world challenging environments.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.23437">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.23437.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.23437.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MGCA-Net: Multi-Graph Contextual Attention Network for Two-View Correspondence Learning</span>
        <span class="paper-authors">Shuyuan Lin, Mengtin Lo, Haosheng Chen, Yanjie Liang, Qiangqiang Wu</span>
        <span class="paper-meta">Updated 2025-12-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Two-view correspondence learning is a key task in computer vision, which aims to establish reliable matching relationships for applications such as camera pose estimation and 3D reconstruction. However, existing methods have limitations in local geometric modeling and cross-stage information optimization, which make it difficult to accurately capture the geometric constraints of matched pairs and thus reduce the robustness of the model. To address these challenges, we propose a Multi-Graph Contextual Attention Network (MGCA-Net), which consists of a Contextual Geometric Attention (CGA) module and a Cross-Stage Multi-Graph Consensus (CSMGC) module. Specifically, CGA dynamically integrates spatial position and feature information via an adaptive attention mechanism and enhances the capability to capture both local and global geometric relationships. Meanwhile, CSMGC establishes geometric consensus via a cross-stage sparse graph network, ensuring the consistency of geometric information across different stages. Experimental results on two representative YFCC100M and SUN3D datasets show that MGCA-Net significantly outperforms existing SOTA methods in the outlier rejection and camera pose estimation tasks. Source code is available at http://www.linshuyuan.com.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.23369">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.23369.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.23369.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Selfi: Self Improving Reconstruction Engine via 3D Geometric Feature Alignment</span>
        <span class="paper-authors">Youming Deng et.al.</span>
        <span class="paper-meta">Updated 2025-12-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.08930">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.08930.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.08930.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Robust Multi-view Camera Calibration from Dense Matches</span>
        <span class="paper-authors">Johannes Hägerlind et.al.</span>
        <span class="paper-meta">Updated 2025-12-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.15608">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.15608.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.15608.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">3D Blood Pulsation Maps</span>
        <span class="paper-authors">Maurice Rohr et.al.</span>
        <span class="paper-meta">Updated 2025-12-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.10517">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.10517.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.10517.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">The Dynamic Prior: Understanding 3D Structures for Casual Dynamic Videos</span>
        <span class="paper-authors">Zhuoyuan Wu et.al.</span>
        <span class="paper-meta">Updated 2025-12-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.05398">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.05398.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.05398.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">PoolNet: Deep Learning for 2D to 3D Video Process Validation</span>
        <span class="paper-authors">Sanchit Kaul et.al.</span>
        <span class="paper-meta">Updated 2025-12-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.05362">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.05362.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.05362.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Deep infant brain segmentation from multi-contrast MRI</span>
        <span class="paper-authors">Malte Hoffmann et.al.</span>
        <span class="paper-meta">Updated 2025-12-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.05114">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.05114.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.05114.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">QKAN-LSTM: Quantum-inspired Kolmogorov-Arnold Long Short-term Memory</span>
        <span class="paper-authors">Yu-Chao Hsu et.al.</span>
        <span class="paper-meta">Updated 2025-12-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.05049">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.05049.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.05049.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Geometric Data Science</span>
        <span class="paper-authors">Olga D Anosova et.al.</span>
        <span class="paper-meta">Updated 2025-12-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.05040">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.05040.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.05040.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Internal superfluid response and torque evolution in the giant glitch of PSR J1718-3718</span>
        <span class="paper-authors">Peng Liu et.al.</span>
        <span class="paper-meta">Updated 2025-12-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.04972">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.04972.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.04972.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Canonical Rough Path over Tempered Fractional Brownian Motion: Existence, Construction, and Applications</span>
        <span class="paper-authors">Atef Lechiheb et.al.</span>
        <span class="paper-meta">Updated 2025-12-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.04646">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.04646.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.04646.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Refaçade: Editing Object with Given Reference Texture</span>
        <span class="paper-authors">Youze Huang et.al.</span>
        <span class="paper-meta">Updated 2025-12-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.04534">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.04534.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.04534.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Development of a 15-Degree-of-Freedom Bionic Hand with Cable-Driven Transmission and Distributed Actuation</span>
        <span class="paper-authors">Haoqi Han et.al.</span>
        <span class="paper-meta">Updated 2025-12-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.04399">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.04399.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.04399.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Gamma-from-Mono: Road-Relative, Metric, Self-Supervised Monocular Geometry for Vehicular Applications</span>
        <span class="paper-authors">Gasser Elazab et.al.</span>
        <span class="paper-meta">Updated 2025-12-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.04303">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.04303.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.04303.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Emergent Outlier View Rejection in Visual Geometry Grounded Transformers</span>
        <span class="paper-authors">Jisang Han et.al.</span>
        <span class="paper-meta">Updated 2025-12-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.04012">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.04012.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.04012.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DirectDrag: High-Fidelity, Mask-Free, Prompt-Free Drag-based Image Editing via Readout-Guided Feature Alignment</span>
        <span class="paper-authors">Sheng-Hao Liao et.al.</span>
        <span class="paper-meta">Updated 2025-12-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.03981">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.03981.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.03981.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GLOW: Global Illumination-Aware Inverse Rendering of Indoor Scenes Captured with Dynamic Co-Located Light &amp; Camera</span>
        <span class="paper-authors">Jiaye Wu et.al.</span>
        <span class="paper-meta">Updated 2025-11-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.22857">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.22857.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.22857.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">TraceGen: World Modeling in 3D Trace Space Enables Learning from Cross-Embodiment Videos</span>
        <span class="paper-authors">Seungjae Lee et.al.</span>
        <span class="paper-meta">Updated 2025-11-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.21690">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.21690.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.21690.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">UAVLight: A Benchmark for Illumination-Robust 3D Reconstruction in Unmanned Aerial Vehicle (UAV) Scenes</span>
        <span class="paper-authors">Kang Du et.al.</span>
        <span class="paper-meta">Updated 2025-11-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.21565">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.21565.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.21565.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">From Observation to Action: Latent Action-based Primitive Segmentation for VLA Pre-training in Industrial Settings</span>
        <span class="paper-authors">Jiajie Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-11-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.21428">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.21428.pdf">PDF</a>
          <a class="chip" href="https://github.com/jiajiezhang7/LAPS">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.21428.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DeepRFTv2: Kernel-level Learning for Image Deblurring</span>
        <span class="paper-authors">Xintian Mao et.al.</span>
        <span class="paper-meta">Updated 2025-11-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.21132">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.21132.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.21132.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Hund-projected Kanamori model: an effective description of Hund&#x27;s metals near the Mott insulating regime</span>
        <span class="paper-authors">Johan Carlström et.al.</span>
        <span class="paper-meta">Updated 2025-11-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.20788">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.20788.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.20788.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">From Observations to Simulations: A Neural-Network Approach to Intracluster Medium Kinematics</span>
        <span class="paper-authors">E. Gatuzz et.al.</span>
        <span class="paper-meta">Updated 2025-11-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.20755">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.20755.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.20755.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Diverse Video Generation with Determinantal Point Process-Guided Policy Optimization</span>
        <span class="paper-authors">Tahira Kazimi et.al.</span>
        <span class="paper-meta">Updated 2025-11-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.20647">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.20647.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.20647.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Dance Style Classification using Laban-Inspired and Frequency-Domain Motion Features</span>
        <span class="paper-authors">Ben Hamscher et.al.</span>
        <span class="paper-meta">Updated 2025-11-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.20469">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.20469.pdf">PDF</a>
          <a class="chip" href="https://github.com/benhamscher/dance-style-classification">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.20469.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">AMB3R: Accurate Feed-forward Metric-scale 3D Reconstruction with Backend</span>
        <span class="paper-authors">Hengyi Wang et.al.</span>
        <span class="paper-meta">Updated 2025-11-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.20343">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.20343.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.20343.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Stochastic Dynamics of Skyrmions on a Racetrack: Impact of Equilibrium and Nonequilibrium Noise</span>
        <span class="paper-authors">Anton V. Hlushchenko et.al.</span>
        <span class="paper-meta">Updated 2025-11-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.20287">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.20287.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.20287.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Dynamic Multi-Species Bird Soundscape Generation with Acoustic Patterning and 3D Spatialization</span>
        <span class="paper-authors">Ellie L. Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.19275">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.19275.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.19275.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A Deep-Learning-Based Framework for Focal Mechanism Determination and Its Application to the 2022 Luding Earthquake Sequence</span>
        <span class="paper-authors">Ziye Yu et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.19185">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.19185.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.19185.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">The variability of blazars throughout the electromagnetic spectrum</span>
        <span class="paper-authors">Claudia M. Raiteri et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.18975">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.18975.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.18975.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MagicWorld: Interactive Geometry-driven Video World Exploration</span>
        <span class="paper-authors">Guangyuan Li et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.18886">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.18886.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.18886.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">STCDiT: Spatio-Temporally Consistent Diffusion Transformer for High-Quality Video Super-Resolution</span>
        <span class="paper-authors">Junyang Chen et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.18786">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.18786.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.18786.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">On the role of fractional Brownian motion in models of chemotaxis and stochastic gradient ascent</span>
        <span class="paper-authors">Gustavo Cornejo-Olea et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.18745">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.18745.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.18745.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">C3Po: Cross-View Cross-Modality Correspondence by Pointmap Prediction</span>
        <span class="paper-authors">Kuan Wei Huang et.al.</span>
        <span class="paper-meta">Updated 2025-11-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.18559">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.18559.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.18559.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Non-Symplectic Deformations of Geometric Quantisation</span>
        <span class="paper-authors">Kerr Maxwell et.al.</span>
        <span class="paper-meta">Updated 2025-11-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.18549">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.18549.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.18549.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Zero-Shot Video Deraining with Video Diffusion Models</span>
        <span class="paper-authors">Tuomas Varanka et.al.</span>
        <span class="paper-meta">Updated 2025-11-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.18537">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.18537.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.18537.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Expanding the Workspace of Electromagnetic Navigation Systems Using Dynamic Feedback for Single- and Multi-agent Control</span>
        <span class="paper-authors">Jasan Zughaibi et.al.</span>
        <span class="paper-meta">Updated 2025-11-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.18486">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.18486.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.18486.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MambaIO: Global-Coordinate Inertial Odometry for Pedestrians via Multi-Scale Frequency-Decoupled Modeling</span>
        <span class="paper-authors">Shanshan Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-11-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.15645">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.15645.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.15645.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Covariant Measures of Non-Markovianity in Curved Spacetime</span>
        <span class="paper-authors">Tushar Waghmare et.al.</span>
        <span class="paper-meta">Updated 2025-11-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.15365">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.15365.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.15365.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Generating Natural-Language Surgical Feedback: From Structured Representation to Domain-Grounded Evaluation</span>
        <span class="paper-authors">Firdavs Nasriddinov et.al.</span>
        <span class="paper-meta">Updated 2025-11-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.15159">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.15159.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.15159.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SceneEdited: A City-Scale Benchmark for 3D HD Map Updating via Image-Guided Change Detection</span>
        <span class="paper-authors">Chun-Jung Lin et.al.</span>
        <span class="paper-meta">Updated 2025-11-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.15153">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.15153.pdf">PDF</a>
          <a class="chip" href="https://github.com/ChadLin9596/ScenePoint-ETK">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.15153.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Gaussian See, Gaussian Do: Semantic 3D Motion Transfer from Multiview Video</span>
        <span class="paper-authors">Yarin Bekor et.al.</span>
        <span class="paper-meta">Updated 2025-11-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.14848">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.14848.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.14848.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Blur-Robust Detection via Feature Restoration: An End-to-End Framework for Prior-Guided Infrared UAV Target Detection</span>
        <span class="paper-authors">Xiaolin Wang et.al.</span>
        <span class="paper-meta">Updated 2025-11-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.14371">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.14371.pdf">PDF</a>
          <a class="chip" href="https://github.com/IVPLabs/JFD3">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.14371.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Hubble Space Telescope proper motions of Large Magellanic Cloud star clusters -- II. Kinematic structure of young and intermediate-age clusters</span>
        <span class="paper-authors">F. Niederhofer et.al.</span>
        <span class="paper-meta">Updated 2025-11-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.14351">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.14351.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.14351.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Vortex stability in pseudo-Hermitian theories</span>
        <span class="paper-authors">R. A. Battye et.al.</span>
        <span class="paper-meta">Updated 2025-11-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.14300">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.14300.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.14300.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Model-Based Clustering of Football Event Sequences: A Marked Spatio-Temporal Point Process Mixture Approach</span>
        <span class="paper-authors">Koffi Amezouwui et.al.</span>
        <span class="paper-meta">Updated 2025-11-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.14297">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.14297.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.14297.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Newborn jet in the symbiotic system R Aquarii</span>
        <span class="paper-authors">T. Liimets et.al.</span>
        <span class="paper-meta">Updated 2025-11-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.14243">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.14243.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.14243.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Towards Rotation-only Imaging Geometry: Rotation Estimation</span>
        <span class="paper-authors">Xinrui Li et.al.</span>
        <span class="paper-meta">Updated 2025-11-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.12415">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.12415.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.12415.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Cycle-Sync: Robust Global Camera Pose Estimation through Enhanced Cycle-Consistent Synchronization</span>
        <span class="paper-authors">Shaohan Li et.al.</span>
        <span class="paper-meta">Updated 2025-11-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.02329">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.02329.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.02329.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Oitijjo-3D: Generative AI Framework for Rapid 3D Heritage Reconstruction from Street View Imagery</span>
        <span class="paper-authors">Momen Khandoker Ope et.al.</span>
        <span class="paper-meta">Updated 2025-11-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.00362">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.00362.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.00362.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">RubbleSim: A Photorealistic Structural Collapse Simulator for Confined Space Mapping</span>
        <span class="paper-authors">Constantine Frost et.al.</span>
        <span class="paper-meta">Updated 2025-10-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.20529">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.20529.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.20529.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DeepDetect: Learning All-in-One Dense Keypoints</span>
        <span class="paper-authors">Shaharyar Ahmed Khan Tareen et.al.</span>
        <span class="paper-meta">Updated 2025-10-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.17422">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.17422.pdf">PDF</a>
          <a class="chip" href="https://github.com/saktx/DeepDetect">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.17422.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Initialize to Generalize: A Stronger Initialization Pipeline for Sparse-View 3DGS</span>
        <span class="paper-authors">Feng Zhou et.al.</span>
        <span class="paper-meta">Updated 2025-10-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.17479">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.17479.pdf">PDF</a>
          <a class="chip" href="https://github.com/zss171999645/ItG-GS">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.17479.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LightGlueStick: a Fast and Robust Glue for Joint Point-Line Matching</span>
        <span class="paper-authors">Aidyn Ubingazhibov et.al.</span>
        <span class="paper-meta">Updated 2025-10-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.16438">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.16438.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.16438.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MRASfM: Multi-Camera Reconstruction and Aggregation through Structure-from-Motion in Driving Scenes</span>
        <span class="paper-authors">Lingfeng Xuan et.al.</span>
        <span class="paper-meta">Updated 2025-10-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.15467">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.15467.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.15467.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">CuSfM: CUDA-Accelerated Structure-from-Motion</span>
        <span class="paper-authors">Jingrui Yu et.al.</span>
        <span class="paper-meta">Updated 2025-10-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.15271">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.15271.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.15271.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Learning Neural Parametric 3D Breast Shape Models for Metrical Surface Reconstruction From Monocular RGB Videos</span>
        <span class="paper-authors">Maximilian Weiherer et.al.</span>
        <span class="paper-meta">Updated 2025-10-15</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.13540">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.13540.pdf">PDF</a>
          <a class="chip" href="https://github.com/mweiherer/local-irbsm">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.13540.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">InstantSfM: Fully Sparse and Parallel Structure-from-Motion</span>
        <span class="paper-authors">Jiankun Zhong et.al.</span>
        <span class="paper-meta">Updated 2025-10-15</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.13310">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.13310.pdf">PDF</a>
          <a class="chip" href="https://github.com/cre185/InstantSfM">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.13310.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Scene Coordinate Reconstruction Priors</span>
        <span class="paper-authors">Wenjing Bian et.al.</span>
        <span class="paper-meta">Updated 2025-10-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.12387">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.12387.pdf">PDF</a>
          <a class="chip" href="https://github.com/nianticspatial/scr-priors">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.12387.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Two-Stage Gaussian Splatting Optimization for Outdoor Scene Reconstruction</span>
        <span class="paper-authors">Deborah Pintani et.al.</span>
        <span class="paper-meta">Updated 2025-10-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.09489">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.09489.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.09489.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">VGGT-X: When VGGT Meets Dense Novel View Synthesis</span>
        <span class="paper-authors">Yang Liu et.al.</span>
        <span class="paper-meta">Updated 2025-10-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.25191">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.25191.pdf">PDF</a>
          <a class="chip" href="https://github.com/Linketic/VGGT-X">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.25191.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Non-Rigid Structure-from-Motion via Differential Geometry with Recoverable Conformal Scale</span>
        <span class="paper-authors">Yongbo Chen et.al.</span>
        <span class="paper-meta">Updated 2025-10-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.01665">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.01665.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.01665.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">BOSfM: A View Planning Framework for Optimal 3D Reconstruction of Agricultural Scenes</span>
        <span class="paper-authors">Athanasios Bacharis et.al.</span>
        <span class="paper-meta">Updated 2025-09-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.24126">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.24126.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.24126.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">RPG360: Robust 360 Depth Estimation with Perspective Foundation Models and Graph Optimization</span>
        <span class="paper-authors">Dongki Jung et.al.</span>
        <span class="paper-meta">Updated 2025-09-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.23991">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.23991.pdf">PDF</a>
          <a class="chip" href="https://github.com/jdk9405/RPG360">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.23991.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">CrashSplat: 2D to 3D Vehicle Damage Segmentation in Gaussian Splatting</span>
        <span class="paper-authors">Dragoş-Andrei Chileban et.al.</span>
        <span class="paper-meta">Updated 2025-09-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.23947">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.23947.pdf">PDF</a>
          <a class="chip" href="https://github.com/DragosChileban/CrashSplat">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.23947.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild</span>
        <span class="paper-authors">Deming Li et.al.</span>
        <span class="paper-meta">Updated 2025-09-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.15548">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.15548.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.15548.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Aerial-Ground Image Feature Matching via 3D Gaussian Splatting-based Intermediate View Rendering</span>
        <span class="paper-authors">Jiangxue Yu et.al.</span>
        <span class="paper-meta">Updated 2025-09-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.19898">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.19898.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.19898.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DeblurSplat: SfM-free 3D Gaussian Splatting with Event Camera for Robust Deblurring</span>
        <span class="paper-authors">Pengteng Li et.al.</span>
        <span class="paper-meta">Updated 2025-09-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.18898">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.18898.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.18898.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MapAnything: Universal Feed-Forward Metric 3D Reconstruction</span>
        <span class="paper-authors">Nikhil Keetha et.al.</span>
        <span class="paper-meta">Updated 2025-09-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.13414">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.13414.pdf">PDF</a>
          <a class="chip" href="https://github.com/facebookresearch/map-anything">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.13414.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Neural 3D Object Reconstruction with Small-Scale Unmanned Aerial Vehicles</span>
        <span class="paper-authors">Àlmos Veres-Vitàlyos et.al.</span>
        <span class="paper-meta">Updated 2025-09-15</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.12458">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.12458.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.12458.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Segmentation-Driven Initialization for Sparse-view 3D Gaussian Splatting</span>
        <span class="paper-authors">Yi-Hsin Li et.al.</span>
        <span class="paper-meta">Updated 2025-09-15</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.11853">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.11853.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.11853.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">3DAeroRelief: The first 3D Benchmark UAV Dataset for Post-Disaster Assessment</span>
        <span class="paper-authors">Nhut Le et.al.</span>
        <span class="paper-meta">Updated 2025-09-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.11097">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.11097.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.11097.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">VIM-GS: Visual-Inertial Monocular Gaussian Splatting via Object-level Guidance in Large Scenes</span>
        <span class="paper-authors">Shengkai Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-09-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.06685">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.06685.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.06685.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Australian Supermarket Object Set (ASOS): A Benchmark Dataset of Physical Objects and 3D Models for Robotics and Computer Vision</span>
        <span class="paper-authors">Akansel Cosgun et.al.</span>
        <span class="paper-meta">Updated 2025-09-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.09720">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.09720.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.09720.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Doctoral Thesis: Geometric Deep Learning For Camera Pose Prediction, Registration, Depth Estimation, and 3D Reconstruction</span>
        <span class="paper-authors">Xueyang Kang et.al.</span>
        <span class="paper-meta">Updated 2025-09-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.01873">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.01873.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.01873.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SAIL-Recon: Large SfM by Augmenting Scene Regression with Localization</span>
        <span class="paper-authors">Junyuan Deng et.al.</span>
        <span class="paper-meta">Updated 2025-08-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2508.17972">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2508.17972.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2508.17972.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">HOSt3R: Keypoint-free Hand-Object 3D Reconstruction from RGB images</span>
        <span class="paper-authors">Anilkumar Swamy et.al.</span>
        <span class="paper-meta">Updated 2025-08-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2508.16465">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2508.16465.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2508.16465.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">NeuralMeshing: Complete Object Mesh Extraction from Casual Captures</span>
        <span class="paper-authors">Floris Erich et.al.</span>
        <span class="paper-meta">Updated 2025-08-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2508.16026">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2508.16026.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2508.16026.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Enhancing Novel View Synthesis from extremely sparse views with SfM-free 3D Gaussian Splatting Framework</span>
        <span class="paper-authors">Zongqi He et.al.</span>
        <span class="paper-meta">Updated 2025-08-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2508.15457">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2508.15457.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2508.15457.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GeMS: Efficient Gaussian Splatting for Extreme Motion Blur</span>
        <span class="paper-authors">Gopi Raju Matta et.al.</span>
        <span class="paper-meta">Updated 2025-08-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2508.14682">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2508.14682.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2508.14682.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GS4Buildings: Prior-Guided Gaussian Splatting for 3D Building Reconstruction</span>
        <span class="paper-authors">Qilin Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-08-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2508.07355">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2508.07355.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2508.07355.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">EndoMatcher: Generalizable Endoscopic Image Matcher via Multi-Domain Pre-training for Robot-Assisted Surgery</span>
        <span class="paper-authors">Bingyu Yang et.al.</span>
        <span class="paper-meta">Updated 2025-08-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2508.05205">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2508.05205.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2508.05205.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Refining Gaussian Splatting: A Volumetric Densification Approach</span>
        <span class="paper-authors">Mohamed Abdul Gafoor et.al.</span>
        <span class="paper-meta">Updated 2025-08-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2508.05187">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2508.05187.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2508.05187.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Enhancing In-Domain and Out-Domain EmoFake Detection via Cooperative Multilingual Speech Foundation Models</span>
        <span class="paper-authors">Orchid Chetia Phukan et.al.</span>
        <span class="paper-meta">Updated 2025-07-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.12595">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.12595.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.12595.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">BRUM: Robust 3D Vehicle Reconstruction from 360 Sparse Images</span>
        <span class="paper-authors">Davide Di Nucci et.al.</span>
        <span class="paper-meta">Updated 2025-07-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.12095">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.12095.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.12095.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Spatial Frequency Modulation for Semantic Segmentation</span>
        <span class="paper-authors">Linwei Chen et.al.</span>
        <span class="paper-meta">Updated 2025-07-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.11893">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.11893.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.11893.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Supporting SENĆOTEN Language Documentation Efforts with Automatic Speech Recognition</span>
        <span class="paper-authors">Mengzhe Geng et.al.</span>
        <span class="paper-meta">Updated 2025-07-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.10827">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.10827.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.10827.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Review of Feed-forward 3D Reconstruction: From DUSt3R to VGGT</span>
        <span class="paper-authors">Wei Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-07-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.08448">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.08448.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.08448.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Wild refitting for black box prediction</span>
        <span class="paper-authors">Martin J. Wainwright et.al.</span>
        <span class="paper-meta">Updated 2025-07-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.21460">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.21460.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.21460.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MGSfM: Multi-Camera Geometry Driven Global Structure-from-Motion</span>
        <span class="paper-authors">Peilin Tao et.al.</span>
        <span class="paper-meta">Updated 2025-07-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.03306">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.03306.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.03306.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Towards Initialization-free Calibrated Bundle Adjustment</span>
        <span class="paper-authors">Carl Olsson et.al.</span>
        <span class="paper-meta">Updated 2025-06-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.23808">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.23808.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.23808.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">AttentionGS: Towards Initialization-Free 3D Gaussian Splatting via Structural Attention</span>
        <span class="paper-authors">Ziao Liu et.al.</span>
        <span class="paper-meta">Updated 2025-06-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.23611">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.23611.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.23611.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Single-Scanline Relative Pose Estimation for Rolling Shutter Cameras</span>
        <span class="paper-authors">Petr Hruby et.al.</span>
        <span class="paper-meta">Updated 2025-06-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.22069">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.22069.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.22069.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ICP-3DGS: SfM-free 3D Gaussian Splatting for Large-scale Unbounded Scenes</span>
        <span class="paper-authors">Chenhao Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-06-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.21629">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.21629.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.21629.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Experimental Assessment of Neural 3D Reconstruction for Small UAV-based Applications</span>
        <span class="paper-authors">Genís Castillo Gómez-Raya et.al.</span>
        <span class="paper-meta">Updated 2025-06-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.19491">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.19491.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.19491.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ViDAR: Video Diffusion-Aware 4D Reconstruction From Monocular Inputs</span>
        <span class="paper-authors">Michal Nazarczuk et.al.</span>
        <span class="paper-meta">Updated 2025-06-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.18792">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.18792.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.18792.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Room temperature spin injection into commercial VCSELs at non-resonant wavelengths</span>
        <span class="paper-authors">Timur Almabetov et.al.</span>
        <span class="paper-meta">Updated 2025-06-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.18376">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.18376.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.18376.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">OWSM-Biasing: Contextualizing Open Whisper-Style Speech Models for Automatic Speech Recognition with Dynamic Vocabulary</span>
        <span class="paper-authors">Yui Sudo et.al.</span>
        <span class="paper-meta">Updated 2025-06-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.09448">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.09448.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.09448.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SurGSplat: Progressive Geometry-Constrained Gaussian Splatting for Surgical Scene Reconstruction</span>
        <span class="paper-authors">Yuchao Zheng et.al.</span>
        <span class="paper-meta">Updated 2025-06-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.05935">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.05935.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.05935.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">On-the-fly Reconstruction for Large-Scale Novel View Synthesis from Unposed Images</span>
        <span class="paper-authors">Andreas Meuleman et.al.</span>
        <span class="paper-meta">Updated 2025-06-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.05558">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.05558.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.05558.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SupeRANSAC: One RANSAC to Rule Them All</span>
        <span class="paper-authors">Daniel Barath et.al.</span>
        <span class="paper-meta">Updated 2025-06-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.04803">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.04803.pdf">PDF</a>
          <a class="chip" href="https://github.com/danini/superansac">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.04803.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Voyager: Long-Range and World-Consistent Video Diffusion for Explorable 3D Scene Generation</span>
        <span class="paper-authors">Tianyu Huang et.al.</span>
        <span class="paper-meta">Updated 2025-06-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.04225">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.04225.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.04225.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Accelerating SfM-based Pose Estimation with Dominating Set</span>
        <span class="paper-authors">Joji Joseph et.al.</span>
        <span class="paper-meta">Updated 2025-06-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.03667">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.03667.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.03667.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Nearby dwarf galaxies with extreme star formation rates: a window into dwarf-galaxy evolution in the early Universe</span>
        <span class="paper-authors">S. Kaviraj et.al.</span>
        <span class="paper-meta">Updated 2025-06-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.03265">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.03265.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.03265.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Improving Multilingual Speech Models on ML-SUPERB 2.0: Fine-tuning with Data Augmentation and LID-Aware CTC</span>
        <span class="paper-authors">Qingzheng Wang et.al.</span>
        <span class="paper-meta">Updated 2025-06-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.24200">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.24200.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.24200.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Fast and Robust Rotation Averaging with Anisotropic Coordinate Descent</span>
        <span class="paper-authors">Yaroslava Lochman et.al.</span>
        <span class="paper-meta">Updated 2025-06-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.01940">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.01940.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.01940.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FAMA: The First Large-Scale Open-Science Speech Foundation Model for English and Italian</span>
        <span class="paper-authors">Sara Papi et.al.</span>
        <span class="paper-meta">Updated 2025-05-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.22759">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.22759.pdf">PDF</a>
          <a class="chip" href="https://github.com/hlt-mt/fbk-fairseq">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.22759.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Towards Robust Assessment of Pathological Voices via Combined Low-Level Descriptors and Foundation Model Representations</span>
        <span class="paper-authors">Whenty Ariyanti et.al.</span>
        <span class="paper-meta">Updated 2025-05-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.21356">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.21356.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.21356.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Rooms from Motion: Un-posed Indoor 3D Object Detection as Localization and Mapping</span>
        <span class="paper-authors">Justin Lazarow et.al.</span>
        <span class="paper-meta">Updated 2025-05-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.23756">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.23756.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.23756.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Sparse2DGS: Sparse-View Surface Reconstruction using 2D Gaussian Splatting with Dense Point Cloud</span>
        <span class="paper-authors">Natsuki Takama et.al.</span>
        <span class="paper-meta">Updated 2025-05-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.19854">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.19854.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.19854.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">UAVPairs: A Challenging Benchmark for Match Pair Retrieval of Large-scale UAV Images</span>
        <span class="paper-authors">Junhuan Liu et.al.</span>
        <span class="paper-meta">Updated 2025-05-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.22098">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.22098.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.22098.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Fast Feature Matching of UAV Images via Matrix Band Reduction-based GPU Data Schedule</span>
        <span class="paper-authors">San Jiang et.al.</span>
        <span class="paper-meta">Updated 2025-05-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.22089">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.22089.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.22089.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Intern-GS: Vision Model Guided Sparse-View 3D Gaussian Splatting</span>
        <span class="paper-authors">Xiangyu Sun et.al.</span>
        <span class="paper-meta">Updated 2025-05-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.20729">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.20729.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.20729.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Robust fine-tuning of speech recognition models via model merging: application to disordered speech</span>
        <span class="paper-authors">Alexandre Ducorroy et.al.</span>
        <span class="paper-meta">Updated 2025-05-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.20477">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.20477.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.20477.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Improving Novel view synthesis of 360$^\circ$ Scenes in Extremely Sparse Views by Jointly Training Hemisphere Sampled Synthetic Images</span>
        <span class="paper-authors">Guangan Chen et.al.</span>
        <span class="paper-meta">Updated 2025-05-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.19264">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.19264.pdf">PDF</a>
          <a class="chip" href="https://github.com/angchen-dev/hemisparsegs">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.19264.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Token-Level Logits Matter: A Closer Look at Speech Foundation Models for Ambiguous Emotion Recognition</span>
        <span class="paper-authors">Jule Valendo Halim et.al.</span>
        <span class="paper-meta">Updated 2025-05-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.18484">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.18484.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.18484.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Tracking the Flight: Exploring a Computational Framework for Analyzing Escape Responses in Plains Zebra (Equus quagga)</span>
        <span class="paper-authors">Isla Duporge et.al.</span>
        <span class="paper-meta">Updated 2025-05-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.16882">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.16882.pdf">PDF</a>
          <a class="chip" href="https://github.com/neuroinformatics-unit/zebras-stitching">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.16882.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A Taxonomy of Structure from Motion Methods</span>
        <span class="paper-authors">Federica Arrigoni et.al.</span>
        <span class="paper-meta">Updated 2025-05-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.15814">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.15814.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.15814.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FastMap: Revisiting Dense and Scalable Structure from Motion</span>
        <span class="paper-authors">Jiahao Li et.al.</span>
        <span class="paper-meta">Updated 2025-05-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.04612">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.04612.pdf">PDF</a>
          <a class="chip" href="https://github.com/pals-ttic/fastmap">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.04612.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Shallow Flow Matching for Coarse-to-Fine Text-to-Speech Synthesis</span>
        <span class="paper-authors">Dong Yang et.al.</span>
        <span class="paper-meta">Updated 2025-05-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.12226">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.12226.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.12226.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Mapping Semantic Segmentation to Point Clouds Using Structure from Motion for Forest Analysis</span>
        <span class="paper-authors">Francisco Raverta Capua et.al.</span>
        <span class="paper-meta">Updated 2025-05-15</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.10751">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.10751.pdf">PDF</a>
          <a class="chip" href="https://github.com/lrse/sodm">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.10751.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Estimating the Diameter at Breast Height of Trees in a Forest With a Single 360 Camera</span>
        <span class="paper-authors">Siming He et.al.</span>
        <span class="paper-meta">Updated 2025-05-15</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.03093">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.03093.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.03093.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Unveiling the Best Practices for Applying Speech Foundation Models to Speech Intelligibility Prediction for Hearing-Impaired People</span>
        <span class="paper-authors">Haoshuai Zhou et.al.</span>
        <span class="paper-meta">Updated 2025-05-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.08215">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.08215.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.08215.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">RDD: Robust Feature Detector and Descriptor using Deformable Transformer</span>
        <span class="paper-authors">Gonglin Chen et.al.</span>
        <span class="paper-meta">Updated 2025-05-12</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.08013">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.08013.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.08013.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Geometric Prior-Guided Neural Implicit Surface Reconstruction in the Wild</span>
        <span class="paper-authors">Lintao Xiang et.al.</span>
        <span class="paper-meta">Updated 2025-05-12</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.07373">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.07373.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.07373.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Symmetry in Fundamental Parameters of Galaxies on the Star-forming Main Sequence</span>
        <span class="paper-authors">Zhicheng He et.al.</span>
        <span class="paper-meta">Updated 2025-05-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.06868">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.06868.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.06868.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">TPK: Trustworthy Trajectory Prediction Integrating Prior Knowledge For Interpretability and Kinematic Feasibility</span>
        <span class="paper-authors">Marius Baden et.al.</span>
        <span class="paper-meta">Updated 2025-05-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.06743">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.06743.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.06743.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DiffusionSfM: Predicting Structure and Motion via Ray Origin and Endpoint Diffusion</span>
        <span class="paper-authors">Qitao Zhao et.al.</span>
        <span class="paper-meta">Updated 2025-05-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.05473">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.05473.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.05473.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">AquaGS: Fast Underwater Scene Reconstruction with SfM-Free Gaussian Splatting</span>
        <span class="paper-authors">Junhao Shi et.al.</span>
        <span class="paper-meta">Updated 2025-05-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.01799">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.01799.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.01799.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">PosePilot: Steering Camera Pose for Generative World Models with Self-supervised Depth</span>
        <span class="paper-authors">Bu Jin et.al.</span>
        <span class="paper-meta">Updated 2025-05-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.01729">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.01729.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.01729.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Are Minimal Radial Distortion Solvers Really Necessary for Relative Pose Estimation?</span>
        <span class="paper-authors">Viktor Kocur et.al.</span>
        <span class="paper-meta">Updated 2025-05-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.00866">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.00866.pdf">PDF</a>
          <a class="chip" href="https://github.com/kocurvik/rdnet">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.00866.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Large-scale visual SLAM for in-the-wild videos</span>
        <span class="paper-authors">Shuo Sun et.al.</span>
        <span class="paper-meta">Updated 2025-04-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.20496">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.20496.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.20496.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Sparse2DGS: Geometry-Prioritized Gaussian Splatting for Surface Reconstruction from Sparse Views</span>
        <span class="paper-authors">Jiang Wu et.al.</span>
        <span class="paper-meta">Updated 2025-04-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.20378">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.20378.pdf">PDF</a>
          <a class="chip" href="https://github.com/wuuu3511/sparse2dgs">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.20378.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MP-SfM: Monocular Surface Priors for Robust Structure-from-Motion</span>
        <span class="paper-authors">Zador Pataki et.al.</span>
        <span class="paper-meta">Updated 2025-04-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.20040">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.20040.pdf">PDF</a>
          <a class="chip" href="https://github.com/cvg/mpsfm">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.20040.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Dynamic Camera Poses and Where to Find Them</span>
        <span class="paper-authors">Chris Rockwell et.al.</span>
        <span class="paper-meta">Updated 2025-04-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.17788">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.17788.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.17788.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">EdgePoint2: Compact Descriptors for Superior Efficiency and Accuracy</span>
        <span class="paper-authors">Haodi Yao et.al.</span>
        <span class="paper-meta">Updated 2025-04-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.17280">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.17280.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.17280.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A Low-Cost Photogrammetry System for 3D Plant Modeling and Phenotyping</span>
        <span class="paper-authors">Joe Hrzich et.al.</span>
        <span class="paper-meta">Updated 2025-04-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.16840">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.16840.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.16840.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">PRaDA: Projective Radial Distortion Averaging</span>
        <span class="paper-authors">Daniil Sinitsyn et.al.</span>
        <span class="paper-meta">Updated 2025-04-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.16499">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.16499.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.16499.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Traversing the Star-Forming Main Sequence with Molecular Gas Stacks of z~1.6 Cluster Galaxies</span>
        <span class="paper-authors">Alex Pigarelli et.al.</span>
        <span class="paper-meta">Updated 2025-04-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.15381">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.15381.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.15381.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Towards Understanding Camera Motions in Any Video</span>
        <span class="paper-authors">Zhiqiu Lin et.al.</span>
        <span class="paper-meta">Updated 2025-04-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.15376">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.15376.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.15376.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">StableQuant: Layer Adaptive Post-Training Quantization for Speech Foundation Models</span>
        <span class="paper-authors">Yeona Hong et.al.</span>
        <span class="paper-meta">Updated 2025-04-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.14915">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.14915.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.14915.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Volume Encoding Gaussians: Transfer Function-Agnostic 3D Gaussians for Volume Rendering</span>
        <span class="paper-authors">Landon Dyken et.al.</span>
        <span class="paper-meta">Updated 2025-04-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.13339">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.13339.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.13339.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">EDGS: Eliminating Densification for Efficient Convergence of 3DGS</span>
        <span class="paper-authors">Dmytro Kotovenko et.al.</span>
        <span class="paper-meta">Updated 2025-04-15</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.13204">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.13204.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.13204.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Deep Learning-based Bathymetry Retrieval without In-situ Depths using Remote Sensing Imagery and SfM-MVS DSMs with Data Gaps</span>
        <span class="paper-authors">Panagiotis Agrafiotis et.al.</span>
        <span class="paper-meta">Updated 2025-04-15</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.11416">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.11416.pdf">PDF</a>
          <a class="chip" href="https://github.com/pagraf/swin-bathyunet">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.11416.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A Constrained Optimization Approach for Gaussian Splatting from Coarsely-posed Images and Noisy Lidar Point Clouds</span>
        <span class="paper-authors">Jizong Peng et.al.</span>
        <span class="paper-meta">Updated 2025-04-12</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.09129">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.09129.pdf">PDF</a>
          <a class="chip" href="https://github.com/eldentse/contrained-optimization-3dgs">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.09129.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Stereophotoclinometry Revisited</span>
        <span class="paper-authors">Travis Driver et.al.</span>
        <span class="paper-meta">Updated 2025-04-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.08252">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.08252.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.08252.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FIORD: A Fisheye Indoor-Outdoor Dataset with LIDAR Ground Truth for 3D Scene Reconstruction and Benchmarking</span>
        <span class="paper-authors">Ulas Gunes et.al.</span>
        <span class="paper-meta">Updated 2025-04-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.01732">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.01732.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.01732.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Implementation of a Zed 2i Stereo Camera for High-Frequency Shoreline Change and Coastal Elevation Monitoring</span>
        <span class="paper-authors">José A. Pilartes-Congo et.al.</span>
        <span class="paper-meta">Updated 2025-04-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.06464">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.06464.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.06464.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Decoding the variability in the star-formation histories of z ~ 0.8 galaxies</span>
        <span class="paper-authors">Jenny T. Wan et.al.</span>
        <span class="paper-meta">Updated 2025-04-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.05281">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.05281.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.05281.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">3R-GS: Best Practice in Optimizing Camera Poses Along with 3DGS</span>
        <span class="paper-authors">Zhisheng Huang et.al.</span>
        <span class="paper-meta">Updated 2025-04-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.04294">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.04294.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.04294.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">An Algebraic Geometry Approach to Viewing Graph Solvability</span>
        <span class="paper-authors">Federica Arrigoni et.al.</span>
        <span class="paper-meta">Updated 2025-04-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.03637">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.03637.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.03637.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Endo3R: Unified Online Reconstruction from Dynamic Monocular Endoscopic Video</span>
        <span class="paper-authors">Jiaxin Guo et.al.</span>
        <span class="paper-meta">Updated 2025-04-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.03198">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.03198.pdf">PDF</a>
          <a class="chip" href="https://github.com/wrld/Endo3R">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.03198.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Adaptive Frequency Enhancement Network for Remote Sensing Image Semantic Segmentation</span>
        <span class="paper-authors">Feng Gao et.al.</span>
        <span class="paper-meta">Updated 2025-04-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.02647">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.02647.pdf">PDF</a>
          <a class="chip" href="https://github.com/oucailab/afenet">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.02647.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LITA-GS: Illumination-Agnostic Novel View Synthesis via Reference-Free 3D Gaussian Splatting and Physical Priors</span>
        <span class="paper-authors">Han Zhou et.al.</span>
        <span class="paper-meta">Updated 2025-03-31</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.00219">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.00219.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.00219.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">AnyCam: Learning to Recover Camera Poses and Intrinsics from Casual Videos</span>
        <span class="paper-authors">Felix Wimbauer et.al.</span>
        <span class="paper-meta">Updated 2025-03-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.23282">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.23282.pdf">PDF</a>
          <a class="chip" href="https://github.com/Brummi/anycam">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.23282.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ProtoGS: Efficient and High-Quality Rendering with 3D Gaussian Prototypes</span>
        <span class="paper-authors">Zhengqing Gao et.al.</span>
        <span class="paper-meta">Updated 2025-03-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.17486">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.17486.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.17486.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Ground Penetrating Radar-Assisted Multimodal Robot Odometry Using Subsurface Feature Matrix</span>
        <span class="paper-authors">Haifeng Li et.al.</span>
        <span class="paper-meta">Updated 2025-03-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.18301">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.18301.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.18301.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">3D Modeling: Camera Movement Estimation and path Correction for SFM Model using the Combination of Modified A-SIFT and Stereo System</span>
        <span class="paper-authors">Usha Kumari et.al.</span>
        <span class="paper-meta">Updated 2025-03-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.17668">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.17668.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.17668.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Euclid Quick Data Release (Q1). A first view of the star-forming main sequence in the Euclid Deep Fields</span>
        <span class="paper-authors">Euclid Collaboration et.al.</span>
        <span class="paper-meta">Updated 2025-03-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.15314">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.15314.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.15314.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ColabSfM: Collaborative Structure-from-Motion by Point Cloud Registration</span>
        <span class="paper-authors">Johan Edstedt et.al.</span>
        <span class="paper-meta">Updated 2025-03-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.17093">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.17093.pdf">PDF</a>
          <a class="chip" href="https://github.com/ericssonresearch/colabsfm">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.17093.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">From Monocular Vision to Autonomous Action: Guiding Tumor Resection via 3D Reconstruction</span>
        <span class="paper-authors">Ayberk Acar et.al.</span>
        <span class="paper-meta">Updated 2025-03-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.16263">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.16263.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.16263.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Multi-view Reconstruction via SfM-guided Monocular Depth Estimation</span>
        <span class="paper-authors">Haoyu Guo et.al.</span>
        <span class="paper-meta">Updated 2025-03-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.14483">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.14483.pdf">PDF</a>
          <a class="chip" href="https://github.com/zju3dv/Murre">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.14483.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A-SCoRe: Attention-based Scene Coordinate Regression for wide-ranging scenarios</span>
        <span class="paper-authors">Huy-Hoang Bui et.al.</span>
        <span class="paper-meta">Updated 2025-03-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.13982">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.13982.pdf">PDF</a>
          <a class="chip" href="https://github.com/ais-lab/a-score">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.13982.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Endo-FASt3r: Endoscopic Foundation model Adaptation for Structure from motion</span>
        <span class="paper-authors">Mona Sheikh Zeinoddin et.al.</span>
        <span class="paper-meta">Updated 2025-03-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.07204">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.07204.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.07204.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Improving Geometric Consistency for 360-Degree Neural Radiance Fields in Indoor Scenarios</span>
        <span class="paper-authors">Iryna Repinetska et.al.</span>
        <span class="paper-meta">Updated 2025-03-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.13710">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.13710.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.13710.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Gaussian On-the-Fly Splatting: A Progressive Framework for Robust Near Real-Time 3DGS Optimization</span>
        <span class="paper-authors">Yiwei Xu et.al.</span>
        <span class="paper-meta">Updated 2025-03-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.13086">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.13086.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.13086.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SFMNet: Sparse Focal Modulation for 3D Object Detection</span>
        <span class="paper-authors">Oren Shrout et.al.</span>
        <span class="paper-meta">Updated 2025-03-15</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.12093">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.12093.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.12093.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A Framework for Reducing the Complexity of Geometric Vision Problems and its Application to Two-View Triangulation with Approximation Bounds</span>
        <span class="paper-authors">Felix Rydell et.al.</span>
        <span class="paper-meta">Updated 2025-03-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.08142">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.08142.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.08142.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DaD: Distilled Reinforcement Learning for Diverse Keypoint Detection</span>
        <span class="paper-authors">Johan Edstedt et.al.</span>
        <span class="paper-meta">Updated 2025-03-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.07347">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.07347.pdf">PDF</a>
          <a class="chip" href="https://github.com/parskatt/dad">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.07347.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">VidBot: Learning Generalizable 3D Actions from In-the-Wild 2D Human Videos for Zero-Shot Robotic Manipulation</span>
        <span class="paper-authors">Hanzhi Chen et.al.</span>
        <span class="paper-meta">Updated 2025-03-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.07135">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.07135.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.07135.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">AxisPose: Model-Free Matching-Free Single-Shot 6D Object Pose Estimation via Axis Generation</span>
        <span class="paper-authors">Yang Zou et.al.</span>
        <span class="paper-meta">Updated 2025-03-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.06660">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.06660.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.06660.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LiDAR-enhanced 3D Gaussian Splatting Mapping</span>
        <span class="paper-authors">Jian Shen et.al.</span>
        <span class="paper-meta">Updated 2025-03-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.05425">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.05425.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.05425.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">PLMP -- Point-Line Minimal Problems for Projective SfM</span>
        <span class="paper-authors">Kim Kiehn et.al.</span>
        <span class="paper-meta">Updated 2025-03-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.04351">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.04351.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.04351.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A Multi-Sensor Fusion Approach for Rapid Orthoimage Generation in Large-Scale UAV Mapping</span>
        <span class="paper-authors">Jialei He et.al.</span>
        <span class="paper-meta">Updated 2025-03-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.01202">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.01202.pdf">PDF</a>
          <a class="chip" href="https://github.com/zhan994/ortho_mapper">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.01202.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MUSt3R: Multi-view Network for Stereo 3D Reconstruction</span>
        <span class="paper-authors">Yohann Cabon et.al.</span>
        <span class="paper-meta">Updated 2025-03-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.01661">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.01661.pdf">PDF</a>
          <a class="chip" href="https://github.com/naver/must3r">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.01661.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ecg2o: A Seamless Extension of g2o for Equality-Constrained Factor Graph Optimization</span>
        <span class="paper-authors">Anas Abdelkarim et.al.</span>
        <span class="paper-meta">Updated 2025-03-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.01311">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.01311.pdf">PDF</a>
          <a class="chip" href="https://github.com/snt-arg/ecg2o">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.01311.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
        </div>
      </div>
    </details>
  </article>
</section>
