---
layout: default
title: Image Matching
---

<section class="topic-hero" style="--accent: #39ff88;">
  <div>
    <p class="eyebrow">Topic</p>
    <h1>Image Matching</h1>
    <p class="topic-lede">Updated 2026.03.16 · 152 papers</p>
  </div>
  <a class="btn ghost" href="../index.html#topics">← Back to topics</a>
</section>

<section class="paper-grid">
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">CM-Bench: A Comprehensive Cross-Modal Feature Matching Benchmark Bridging Visible and Infrared Images</span>
        <span class="paper-authors">Liangzheng Sun, Mengfan He, Xingyu Shao, Binbin Li, Zhiqiang Yan, Chunyu Li, Ziyang Meng, Fei Xing</span>
        <span class="paper-meta">Updated 2026-03-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Infrared-visible (IR-VIS) feature matching plays an essential role in cross-modality visual localization, navigation and perception. Along with the rapid development of deep learning techniques, a number of representative image matching methods have been proposed. However, crossmodal feature matching is still a challenging task due to the significant appearance difference. A significant gap for cross-modal feature matching research lies in the absence of standardized benchmarks and metrics for evaluations. In this paper, we introduce a comprehensive cross-modal feature matching benchmark, CM-Bench, which encompasses 30 feature matching algorithms across diverse cross-modal datasets. Specifically, state-of-the-art traditional and deep learning-based methods are first summarized and categorized into sparse, semidense, and dense methods. These methods are evaluated by different tasks including homography estimation, relative pose estimation, and feature-matching-based geo-localization. In addition, we introduce a classification-network-based adaptive preprocessing front-end that automatically selects suitable enhancement strategies before matching. We also present a novel infrared-satellite cross-modal dataset with manually annotated ground-truth correspondences for practical geo-localization evaluation. The dataset and resource will be available at: https://github.com/SLZ98/CM-Bench.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.12690">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.12690.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.12690.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Understanding and Optimizing Attention-Based Sparse Matching for Diverse Local Features</span>
        <span class="paper-authors">Qiang Wang</span>
        <span class="paper-meta">Updated 2026-03-12</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We revisit the problem of training attention-based sparse image matching models for various local features. We first identify one critical design choice that has been previously overlooked, which significantly impacts the performance of the LightGlue model. We then investigate the role of detectors and descriptors within the transformer-based matching framework, finding that detectors, rather than descriptors, are often the primary cause for performance difference. Finally, we propose a novel approach to fine-tune existing image matching models using keypoints from a diverse set of detectors, resulting in a universal, detector-agnostic model. When deployed as a zero-shot matcher for novel detectors, the resulting model achieves or exceeds the accuracy of models specifically trained for those features. Our findings offer valuable insights for the deployment of transformer-based matching models and the future design of local features.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.08430">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.08430.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.08430.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Enhancing Cross-View UAV Geolocalization via LVLM-Driven Relational Modeling</span>
        <span class="paper-authors">Bowen Liu, Pengyue Jia, Wanyu Wang, Derong Xu, Jiawei Cheng, Jiancheng Dong, Xiao Han, Zimo Zhao, Chao Zhang, Bowen Yu, Fangyu Hong, Xiangyu Zhao</span>
        <span class="paper-meta">Updated 2026-03-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">The primary objective of cross-view UAV geolocalization is to identify the exact spatial coordinates of drone-captured imagery by aligning it with extensive, geo-referenced satellite databases. Current approaches typically extract features independently from each perspective and rely on basic heuristics to compute similarity, thereby failing to explicitly capture the essential interactions between different views. To address this limitation, we introduce a novel, plug-and-play ranking architecture designed to explicitly perform joint relational modeling for improved UAV-to-satellite image matching. By harnessing the capabilities of a Large Vision-Language Model (LVLM), our framework effectively learns the deep visual-semantic correlations linking UAV and satellite imagery. Furthermore, we present a novel relational-aware loss function to optimize the training phase. By employing soft labels, this loss provides fine-grained supervision that avoids overly penalizing near-positive matches, ultimately boosting both the model&#x27;s discriminative power and training stability. Comprehensive evaluations across various baseline architectures and standard benchmarks reveal that the proposed method substantially boosts the retrieval accuracy of existing models, yielding superior performance even under highly demanding conditions.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.08063">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.08063.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.08063.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">EventGeM: Global-to-Local Feature Matching for Event-Based Visual Place Recognition</span>
        <span class="paper-authors">Adam D. Hines, Gokul B. Nair, Nicolás Marticorena, Michael Milford, Tobias Fischer</span>
        <span class="paper-meta">Updated 2026-03-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Dynamic vision sensors, also known as event cameras, are rapidly rising in popularity for robotic and computer vision tasks due to their sparse activation and high-temporal resolution. Event cameras have been used in robotic navigation and localization tasks where accurate positioning needs to occur on small and frequent time scales, or when energy concerns are paramount. In this work, we present EventGeM, a state-of-the-art global to local feature fusion pipeline for event-based Visual Place Recognition. We use a pre-trained vision transformer (ViT-S/16) backbone to obtain global feature patch for initial match predictions embeddings from event histogram images. Local feature keypoints were then detected using a pre-trained MaxViT backbone for 2D-homography based re-ranking with RANSAC. For additional re-ranking refinement, we subsequently used a pre-trained vision foundation model for depth estimation to compare structural similarity between references and queries. Our work performs state-of-the-art localization when compared to the best currently available event-based place recognition method across several benchmark datasets and lighting conditions all whilst being fully capable of running in real-time when deployed across a variety of compute architectures. We demonstrate the capability of EventGeM in a real-world deployment on a robotic platform for online localization using event streams directly from an event camera. Project page: https://eventgemvpr.github.io/</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.05807">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.05807.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.05807.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">No Calibration, No Depth, No Problem: Cross-Sensor View Synthesis with 3D Consistency</span>
        <span class="paper-authors">Cho-Ying Wu, Zixun Huang, Xinyu Huang, Liu Ren</span>
        <span class="paper-meta">Updated 2026-02-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We present the first study of cross-sensor view synthesis across different modalities. We examine a practical, fundamental, yet widely overlooked problem: getting aligned RGB-X data, where most RGB-X prior work assumes such pairs exist and focuses on modality fusion, but it empirically requires huge engineering effort in calibration. We propose a match-densify-consolidate method. First, we perform RGB-X image matching followed by guided point densification. Using the proposed confidence-aware densification and self-matching filtering, we attain better view synthesis and later consolidate them in 3D Gaussian Splatting (3DGS). Our method uses no 3D priors for X-sensor and only assumes nearly no-cost COLMAP for RGB. We aim to remove the cumbersome calibration for various RGB-X sensors and advance the popularity of cross-sensor learning by a scalable solution that breaks through the bottleneck in large-scale real-world RGB-X data collection.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.23559">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.23559.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.23559.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FlowFixer: Towards Detail-Preserving Subject-Driven Generation</span>
        <span class="paper-authors">Jinyoung Jun, Won-Dong Jang, Wenbin Ouyang, Raghudeep Gadde, Jungbeom Lee</span>
        <span class="paper-meta">Updated 2026-02-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We present FlowFixer, a refinement framework for subject-driven generation (SDG) that restores fine details lost during generation caused by changes in scale and perspective of a subject. FlowFixer proposes direct image-to-image translation from visual references, avoiding ambiguities in language prompts. To enable image-to-image training, we introduce a one-step denoising scheme to generate self-supervised training data, which automatically removes high-frequency details while preserving global structure, effectively simulating real-world SDG errors. We further propose a keypoint matching-based metric to properly assess fidelity in details beyond semantic similarities usually measured by CLIP or DINO. Experimental results demonstrate that FlowFixer outperforms state-of-the-art SDG methods in both qualitative and quantitative evaluations, setting a new benchmark for high-fidelity subject-driven generation.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.21402">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.21402.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.21402.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Generative 6D Pose Estimation via Conditional Flow Matching</span>
        <span class="paper-authors">Amir Hamza, Davide Boscaini, Weihang Li, Benjamin Busam, Fabio Poiesi</span>
        <span class="paper-meta">Updated 2026-02-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Existing methods for instance-level 6D pose estimation typically rely on neural networks that either directly regress the pose in $\mathrm{SE}(3)$ or estimate it indirectly via local feature matching. The former struggle with object symmetries, while the latter fail in the absence of distinctive local features. To overcome these limitations, we propose a novel formulation of 6D pose estimation as a conditional flow matching problem in $\mathbb{R}^3$. We introduce Flose, a generative method that infers object poses via a denoising process conditioned on local features. While prior approaches based on conditional flow matching perform denoising solely based on geometric guidance, Flose integrates appearance-based semantic features to mitigate ambiguities caused by object symmetries. We further incorporate RANSAC-based registration to handle outliers. We validate Flose on five datasets from the established BOP benchmark. Flose outperforms prior methods with an average improvement of +4.5 Average Recall. Project Website : https://tev-fbk.github.io/Flose/</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.19719">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.19719.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.19719.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Matching of SAR and optical images based on transformation to shared modality</span>
        <span class="paper-authors">Alexey Borisov, Evgeny Myasnikov, Vladislav Myasnikov</span>
        <span class="paper-meta">Updated 2026-02-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Significant differences in optical images and Synthetic Aperture Radar (SAR) images are caused by fundamental differences in the physical principles underlying their acquisition by Earth remote sensing platforms. These differences make precise image matching (co-registration) of these two types of images difficult. In this paper, we propose a new approach to image matching of optical and SAR images, which is based on transforming the images to a new modality. The new image modality is common to both optical and SAR images and satisfies the following conditions. First, the transformed images must have an equal pre-defined number of channels. Second, the transformed and co-registered images must be as similar as possible. Third, the transformed images must be non-degenerate, meaning they must preserve the significant features of the original images. To further match images transformed to this shared modality, we train the RoMa image matching model, which is one of the leading solutions for matching of regular digital photographs. We evaluated the proposed approach on the publicly available MultiSenGE dataset containing both optical and SAR images. We demonstrated its superiority over alternative approaches based on image translation between original modalities and various feature matching algorithms. The proposed solution not only provides better quality of matching, but is also more versatile. It enables the use of ready-made RoMa and DeDoDe models, pre-trained for regular images, without retraining for a new modality, while maintaining high-quality matching of optical and SAR images.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.12515">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.12515.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.12515.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SOMA-1M: A Large-Scale SAR-Optical Multi-resolution Alignment Dataset for Multi-Task Remote Sensing</span>
        <span class="paper-authors">Peihao Wu, Yongxiang Yao, Yi Wan, Wenfei Zhang, Ruipeng Zhao, Jiayuan Li, Yongjun Zhang</span>
        <span class="paper-meta">Updated 2026-02-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Synthetic Aperture Radar (SAR) and optical imagery provide complementary strengths that constitute the critical foundation for transcending single-modality constraints and facilitating cross-modal collaborative processing and intelligent interpretation. However, existing benchmark datasets often suffer from limitations such as single spatial resolution, insufficient data scale, and low alignment accuracy, making them inadequate for supporting the training and generalization of multi-scale foundation models. To address these challenges, we introduce SOMA-1M (SAR-Optical Multi-resolution Alignment), a pixel-level precisely aligned dataset containing over 1.3 million pairs of georeferenced images with a specification of 512 x 512 pixels. This dataset integrates imagery from Sentinel-1, PIESAT-1, Capella Space, and Google Earth, achieving global multi-scale coverage from 0.5 m to 10 m. It encompasses 12 typical land cover categories, effectively ensuring scene diversity and complexity. To address multimodal projection deformation and massive data registration, we designed a rigorous coarse-to-fine image matching framework ensuring pixel-level alignment. Based on this dataset, we established comprehensive evaluation benchmarks for four hierarchical vision tasks, including image matching, image fusion, SAR-assisted cloud removal, and cross-modal translation, involving over 30 mainstream algorithms. Experimental results demonstrate that supervised training on SOMA-1M significantly enhances performance across all tasks. Notably, multimodal remote sensing image (MRSI) matching performance achieves current state-of-the-art (SOTA) levels. SOMA-1M serves as a foundational resource for robust multimodal algorithms and remote sensing foundation models. The dataset will be released publicly at: https://github.com/PeihaoWu/SOMA-1M.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.05480">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.05480.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.05480.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Quantile Transfer for Reliable Operating Point Selection in Visual Place Recognition</span>
        <span class="paper-authors">Dhyey Manish Rajani, Michael Milford, Tobias Fischer</span>
        <span class="paper-meta">Updated 2026-02-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Visual Place Recognition (VPR) is a key component for localisation in GNSS-denied environments, but its performance critically depends on selecting an image matching threshold (operating point) that balances precision and recall. Thresholds are typically hand-tuned offline for a specific environment and fixed during deployment, leading to degraded performance under environmental change. We propose a method that, given a user-defined precision requirement, automatically selects the operating point of a VPR system to maximise recall. The method uses a small calibration traversal with known correspondences and transfers thresholds to deployment via quantile normalisation of similarity score distributions. This quantile transfer ensures that thresholds remain stable across calibration sizes and query subsets, making the method robust to sampling variability. Experiments with multiple state-of-the-art VPR techniques and datasets show that the proposed approach consistently outperforms the state-of-the-art, delivering up to 25% higher recall in high-precision operating regimes. The method eliminates manual tuning by adapting to new environments and generalising across operating conditions. Our code will be released upon acceptance.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.04401">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.04401.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.04401.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Detecting 3D Line Segments for 6DoF Pose Estimation with Limited Data</span>
        <span class="paper-authors">Matej Mok, Lukáš Gajdošech, Michal Mesároš, Martin Madaras, Viktor Kocur</span>
        <span class="paper-meta">Updated 2026-02-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">The task of 6DoF object pose estimation is one of the fundamental problems of 3D vision with many practical applications such as industrial automation. Traditional deep learning approaches for this task often require extensive training data or CAD models, limiting their application in real-world industrial settings where data is scarce and object instances vary. We propose a novel method for 6DoF pose estimation focused specifically on bins used in industrial settings. We exploit the cuboid geometry of bins by first detecting intermediate 3D line segments corresponding to their top edges. Our approach extends the 2D line segment detection network LeTR to operate on structured point cloud data. The detected 3D line segments are then processed using a simple geometric procedure to robustly determine the bin&#x27;s 6DoF pose. To evaluate our method, we extend an existing dataset with a newly collected and annotated dataset, which we make publicly available. We show that incorporating synthetic training data significantly improves pose estimation accuracy on real scans. Moreover, we show that our method significantly outperforms current state-of-the-art 6DoF pose estimation methods in terms of the pose accuracy (3 cm translation error, 8.2$^\circ$ rotation error) while not requiring instance-specific CAD models during inference.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.12090">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.12090.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.12090.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Gaussian-Constrained LeJEPA Representations for Unsupervised Scene Discovery and Pose Consistency</span>
        <span class="paper-authors">Mohsen Mostafa</span>
        <span class="paper-meta">Updated 2026-01-31</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Unsupervised 3D scene reconstruction from unstructured image collections remains a fundamental challenge in computer vision, particularly when images originate from multiple unrelated scenes and contain significant visual ambiguity. The Image Matching Challenge 2025 (IMC2025) highlights these difficulties by requiring both scene discovery and camera pose estimation under real-world conditions, including outliers and mixed content. This paper investigates the application of Gaussian-constrained representations inspired by LeJEPA (Joint Embedding Predictive Architecture) to address these challenges. We present three progressively refined pipelines, culminating in a LeJEPA-inspired approach that enforces isotropic Gaussian constraints on learned image embeddings. Rather than introducing new theoretical guarantees, our work empirically evaluates how these constraints influence clustering consistency and pose estimation robustness in practice. Experimental results on IMC2025 demonstrate that Gaussian-constrained embeddings can improve scene separation and pose plausibility compared to heuristic-driven baselines, particularly in visually ambiguous settings. These findings suggest that theoretically motivated representation constraints offer a promising direction for bridging self-supervised learning principles and practical structure-from-motion pipelines.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.07016">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.07016.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.07016.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A Streamlined Attention-Based Network for Descriptor Extraction</span>
        <span class="paper-authors">Mattia D&#x27;Urso, Emanuele Santellani, Christian Sormann, Mattia Rossi, Andreas Kuhn, Friedrich Fraundorfer</span>
        <span class="paper-meta">Updated 2026-01-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We introduce SANDesc, a Streamlined Attention-Based Network for Descriptor extraction that aims to improve on existing architectures for keypoint description.   Our descriptor network learns to compute descriptors that improve matching without modifying the underlying keypoint detector. We employ a revised U-Net-like architecture enhanced with Convolutional Block Attention Modules and residual paths, enabling effective local representation while maintaining computational efficiency. We refer to the building blocks of our model as Residual U-Net Blocks with Attention. The model is trained using a modified triplet loss in combination with a curriculum learning-inspired hard negative mining strategy, which improves training stability.   Extensive experiments on HPatches, MegaDepth-1500, and the Image Matching Challenge 2021 show that training SANDesc on top of existing keypoint detectors leads to improved results on multiple matching tasks compared to the original keypoint descriptors. At the same time, SANDesc has a model complexity of just 2.4 million parameters.   As a further contribution, we introduce a new urban dataset featuring 4K images and pre-calibrated intrinsics, designed to evaluate feature extractors. On this benchmark, SANDesc achieves substantial performance gains over the existing descriptors while operating with limited computational resources.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.13126">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.13126.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.13126.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">XRefine: Attention-Guided Keypoint Match Refinement</span>
        <span class="paper-authors">Jan Fabian Schmid, Annika Hagemann</span>
        <span class="paper-meta">Updated 2026-01-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Sparse keypoint matching is crucial for 3D vision tasks, yet current keypoint detectors often produce spatially inaccurate matches. Existing refinement methods mitigate this issue through alignment of matched keypoint locations, but they are typically detector-specific, requiring retraining for each keypoint detector. We introduce XRefine, a novel, detector-agnostic approach for sub-pixel keypoint refinement that operates solely on image patches centered at matched keypoints. Our cross-attention-based architecture learns to predict refined keypoint coordinates without relying on internal detector representations, enabling generalization across detectors. Furthermore, XRefine can be extended to handle multi-view feature tracks. Experiments on MegaDepth, KITTI, and ScanNet demonstrate that the approach consistently improves geometric estimation accuracy, achieving superior performance compared to existing refinement methods while maintaining runtime efficiency. Our code and trained models can be found at https://github.com/boschresearch/xrefine.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.12530">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.12530.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.12530.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SupScene: Learning Overlap-Aware Global Descriptor for Unconstrained SfM</span>
        <span class="paper-authors">Xulei Shi, Maoyu Wang, Yuning Peng, Guanbo Wang, Xin Wang, Qi Chen, Pengjie Tao</span>
        <span class="paper-meta">Updated 2026-01-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Image retrieval is a critical step for alleviating the quadratic complexity of image matching in unconstrained Structure-from-Motion (SfM). However, in this context, image retrieval typically focuses more on the image pairs of geometric matchability than on those of semantic similarity, a nuance that most existing deep learning-based methods guided by batched binaries (overlapping vs. non-overlapping pairs) fail to capture. In this paper, we introduce SupScene, a novel solution that learns global descriptors tailored for finding overlapping image pairs of similar geometric nature for SfM. First, to better underline co-visible regions, we employ a subgraph-based training strategy that moves beyond equally important isolated pairs, leveraging ground-truth geometric overlapping relationships with various weights to provide fine-grained supervision via a soft supervised contrastive loss. Second, we introduce DiVLAD, a DINO-inspired VLAD aggregator that leverages the inherent multi-head attention maps from the last block of ViT. And then, a learnable gating mechanism is designed to adaptively utilize these semantically salient cues with visual features, enabling a more discriminative global descriptor. Extensive experiments on the GL3D dataset demonstrate that our method achieves state-of-the-art performance, significantly outperforming NetVLAD while introducing a negligible number of additional trainable parameters. Furthermore, we show that the proposed training strategy brings consistent gains across different aggregation techniques. Code and models are available at https://anonymous.4open.science/r/SupScene-5B73.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.11930">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.11930.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.11930.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">CLIDD: Cross-Layer Independent Deformable Description for Efficient and Discriminative Local Feature Representation</span>
        <span class="paper-authors">Haodi Yao, Fenghua He, Ning Hao, Yao Su</span>
        <span class="paper-meta">Updated 2026-01-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Robust local feature representations are essential for spatial intelligence tasks such as robot navigation and augmented reality. Establishing reliable correspondences requires descriptors that provide both high discriminative power and computational efficiency. To address this, we introduce Cross-Layer Independent Deformable Description (CLIDD), a method that achieves superior distinctiveness by sampling directly from independent feature hierarchies. This approach utilizes learnable offsets to capture fine-grained structural details across scales while bypassing the computational burden of unified dense representations. To ensure real-time performance, we implement a hardware-aware kernel fusion strategy that maximizes inference throughput. Furthermore, we develop a scalable framework that integrates lightweight architectures with a training protocol leveraging both metric learning and knowledge distillation. This scheme generates a wide spectrum of model variants optimized for diverse deployment constraints. Extensive evaluations demonstrate that our approach achieves superior matching accuracy and exceptional computational efficiency simultaneously. Specifically, the ultra-compact variant matches the precision of SuperPoint while utilizing only 0.004M parameters, achieving a 99.7% reduction in model size. Furthermore, our high-performance configuration outperforms all current state-of-the-art methods, including high-capacity DINOv2-based frameworks, while exceeding 200 FPS on edge devices. These results demonstrate that CLIDD delivers high-precision local feature matching with minimal computational overhead, providing a robust and scalable solution for real-time spatial intelligence tasks.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.09230">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.09230.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.09230.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Near-perfect photo-ID of the Hula painted frog with zero-shot deep local-feature matching</span>
        <span class="paper-authors">Maayan Yesharim, R. G. Bina Perl, Uri Roll, Sarig Gafny, Eli Geffen, Yoav Ram</span>
        <span class="paper-meta">Updated 2026-01-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Accurate individual identification is essential for monitoring rare amphibians, yet invasive marking is often unsuitable for critically endangered species. We evaluate state-of-the-art computer-vision methods for photographic re-identification of the Hula painted frog (Latonia nigriventer) using 1,233 ventral images from 191 individuals collected during 2013-2020 capture-recapture surveys. We compare deep local-feature matching in a zero-shot setting with deep global-feature embedding models. The local-feature pipeline achieves 98% top-1 closed-set identification accuracy, outperforming all global-feature models; fine-tuning improves the best global-feature model to 60% top-1 (91% top-10) but remains below local matching. To combine scalability with accuracy, we implement a two-stage workflow in which a fine-tuned global-feature model retrieves a short candidate list that is re-ranked by local-feature matching, reducing end-to-end runtime from 6.5-7.8 hours to ~38 minutes while maintaining ~96% top-1 closed-set accuracy on the labeled dataset. Separation of match scores between same- and different-individual pairs supports thresholding for open-set identification, enabling practical handling of novel individuals. We deploy this pipeline as a web application for routine field use, providing rapid, standardized, non-invasive identification to support conservation monitoring and capture-recapture analyses. Overall, in this species, zero-shot deep local-feature matching outperformed global-feature embedding and provides a strong default for photo-identification.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.08798">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.08798.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.08798.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Stationaere Kurven auf endlichdimensionalen Mannigfaltigkeiten</span>
        <span class="paper-authors">Tobias Starke</span>
        <span class="paper-meta">Updated 2026-01-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">In this work we discuss the notion of stationary curves of the length functional, the so-called (weak) geodesics, on a Riemannian manifold. The motivation behind this work is to give a detailed description of many key concepts from differential geometry that one needs in order to understand the important notion of a (weak) geodesic. For this, we mainly focus on finite-dimensional smooth manifolds, so that we can develop an intuitive and geometric understanding of the concepts that we want to discuss. At the end of this work, we also provide a rough description of how one can generalise these ideas into infinite dimensions and how one can use (weak) geodesics in special algorithms for image matching (see [21]).</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.05695">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.05695.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.05695.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Exact Clique Number Manipulation via Edge Interdiction</span>
        <span class="paper-authors">Yi Zhou, Haoyu Jiang, Chenghao Zhu, André Rossi</span>
        <span class="paper-meta">Updated 2026-01-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">The Edge Interdiction Clique Problem (EICP) aims to remove at most $k$ edges from a graph so as to minimize the size of the largest clique in the remaining graph. This problem captures a fundamental question in graph manipulation: which edges are structurally critical for preserving large cliques? Such a problem is also motivated by practical applications including protein function maintenance and image matching. The EICP is computationally challenging and belongs to a complexity class beyond NP. Existing approaches rely on general mixed-integer bilevel programming solvers or reformulate the problem into a single-level mixed integer linear program. However, they are still not scalable when the graph size and interdiction budget $k$ grow. To overcome this, we investigate new mixed integer linear formulations, which recast the problem into a sequence of parameterized Edge Blocker Clique Problems (EBCP). This perspective decomposes the original problem into simpler subproblems and enables tighter modeling of clique-related inequalities. Furthermore, we propose a two-stage exact algorithm, \textsc{RLCM}, which first applies problem-specific reduction techniques to shrink the graph and then solves the reduced problem using a tailored branch-and-cut framework. Extensive computational experiments on maximum clique benchmark graphs, large real-world sparse networks, and random graphs demonstrate that \textsc{RLCM} consistently outperforms existing approaches.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.01869">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.01869.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.01869.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Quantum Visual Word Sense Disambiguation: Unraveling Ambiguities Through Quantum Inference Model</span>
        <span class="paper-authors">Wenbo Qiao, Peng Zhang, Qinghua Hu</span>
        <span class="paper-meta">Updated 2025-12-31</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Visual word sense disambiguation focuses on polysemous words, where candidate images can be easily confused. Traditional methods use classical probability to calculate the likelihood of an image matching each gloss of the target word, summing these to form a posterior probability. However, due to the challenge of semantic uncertainty, glosses from different sources inevitably carry semantic biases, which can lead to biased disambiguation results. Inspired by quantum superposition in modeling uncertainty, this paper proposes a Quantum Inference Model for Unsupervised Visual Word Sense Disambiguation (Q-VWSD). It encodes multiple glosses of the target word into a superposition state to mitigate semantic biases. Then, the quantum circuit is executed, and the results are observed. By formalizing our method, we find that Q-VWSD is a quantum generalization of the method based on classical probability. Building on this, we further designed a heuristic version of Q-VWSD that can run more efficiently on classical computing. The experiments demonstrate that our method outperforms state-of-the-art classical methods, particularly by effectively leveraging non-specialized glosses from large language models, which further enhances performance. Our approach showcases the potential of quantum machine learning in practical applications and provides a case for leveraging quantum modeling advantages on classical computers while quantum hardware remains immature.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.24687">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.24687.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.24687.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SPIDER: Spatial Image CorresponDence Estimator for Robust Calibration</span>
        <span class="paper-authors">Zhimin Shao, Abhay Yadav, Rama Chellappa, Cheng Peng</span>
        <span class="paper-meta">Updated 2025-12-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Reliable image correspondences form the foundation of vision-based spatial perception, enabling recovery of 3D structure and camera poses. However, unconstrained feature matching across domains such as aerial, indoor, and outdoor scenes remains challenging due to large variations in appearance, scale and viewpoint. Feature matching has been conventionally formulated as a 2D-to-2D problem; however, recent 3D foundation models provides spatial feature matching properties based on two-view geometry. While powerful, we observe that these spatially coherent matches often concentrate on dominant planar regions, e.g., walls or ground surfaces, while being less sensitive to fine-grained geometric details, particularly under large viewpoint changes. To better understand these trade-offs, we first perform linear probe experiments to evaluate the performance of various vision foundation models for image matching. Building on these insights, we introduce SPIDER, a universal feature matching framework that integrates a shared feature extraction backbone with two specialized network heads for estimating both 2D-based and 3D-based correspondences from coarse to fine. Finally, we introduce an image-matching evaluation benchmark that focuses on unconstrained scenarios with large baselines. SPIDER significantly outperforms SoTA methods, demonstrating its strong ability as a universal image-matching method.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.17750">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.17750.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.17750.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">VisRes Bench: On Evaluating the Visual Reasoning Capabilities of VLMs</span>
        <span class="paper-authors">Brigitta Malagurski Törtei, Yasser Dahou, Ngoc Dung Huynh, Wamiq Reyaz Para, Phúc H. Lê Khac, Ankit Singh, Sofian Chaybouti, Sanath Narayan</span>
        <span class="paper-meta">Updated 2025-12-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Vision-Language Models (VLMs) have achieved remarkable progress across tasks such as visual question answering and image captioning. Yet, the extent to which these models perform visual reasoning as opposed to relying on linguistic priors remains unclear. To address this, we introduce VisRes Bench, a benchmark designed to study visual reasoning in naturalistic settings without contextual language supervision. Analyzing model behavior across three levels of complexity, we uncover clear limitations in perceptual and relational visual reasoning capacities. VisRes isolates distinct reasoning abilities across its levels. Level 1 probes perceptual completion and global image matching under perturbations such as blur, texture changes, occlusion, and rotation; Level 2 tests rule-based inference over a single attribute (e.g., color, count, orientation); and Level 3 targets compositional reasoning that requires integrating multiple visual attributes. Across more than 19,000 controlled task images, we find that state-of-the-art VLMs perform near random under subtle perceptual perturbations, revealing limited abstraction beyond pattern recognition. We conclude by discussing how VisRes provides a unified framework for advancing abstract visual reasoning in multimodal research.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.21194">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.21194.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.21194.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Analog Quantum Image Representation with Qubit-Frugal Encoding</span>
        <span class="paper-authors">Vikrant Sharma, Neel Kanth Kundu</span>
        <span class="paper-meta">Updated 2025-12-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">In this work, we introduce a fundamentally new paradigm for quantum image representation tailored for neutral-atom quantum devices. The proposed method constructs a qubit-efficient image representation by first applying a cartographic generalization algorithm to a classical edge-extracted input image, yielding a highly optimized sparse-dot based geometric description. While ensuring the structural integrity of the image, this sparse representation is then embedded into the atomic configuration of Aquila (QuEra Computing Inc.), modeled through the Bloqade simulation software stack. By encoding visual information through physical atom placement rather than digital basis-state coding, the approach avoids the costly state-preparation overhead inherent to digital quantum image processing circuits. Additionally, pruning sparse dot images, akin to map feature reduction, compresses representations without fidelity loss, thereby substantially reducing qubit requirements when implemented on an analog neutral-atom quantum device. The resulting quantum-native images have been successfully evaluated through matching tasks against an image database, thus illustrating the feasibility of this approach for image matching applications. Since sparse-dot image representations enable seamless generation of synthetic datasets, this work constitutes an initial step towards fully quantum-native machine-learning pipelines for visual data and highlights the potential of scalable analog quantum computing to enable resource-efficient alternatives to energy-intensive classical AI-based image processing frameworks.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.18451">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.18451.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.18451.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">The Perceptual Observatory Characterizing Robustness and Grounding in MLLMs</span>
        <span class="paper-authors">Tejas Anvekar, Fenil Bardoliya, Pavan K. Turaga, Chitta Baral, Vivek Gupta</span>
        <span class="paper-meta">Updated 2025-12-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Recent advances in multimodal large language models (MLLMs) have yielded increasingly powerful models, yet their perceptual capacities remain poorly characterized. In practice, most model families scale language component while reusing nearly identical vision encoders (e.g., Qwen2.5-VL 3B/7B/72B), which raises pivotal concerns about whether progress reflects genuine visual grounding or reliance on internet-scale textual world knowledge. Existing evaluation methods emphasize end-task accuracy, overlooking robustness, attribution fidelity, and reasoning under controlled perturbations. We present The Perceptual Observatory, a framework that characterizes MLLMs across verticals like: (i) simple vision tasks, such as face matching and text-in-vision comprehension capabilities; (ii) local-to-global understanding, encompassing image matching, grid pointing game, and attribute localization, which tests general visual grounding. Each vertical is instantiated with ground-truth datasets of faces and words, systematically perturbed through pixel-based augmentations and diffusion-based stylized illusions. The Perceptual Observatory moves beyond leaderboard accuracy to yield insights into how MLLMs preserve perceptual grounding and relational structure under perturbations, providing a principled foundation for analyzing strengths and weaknesses of current and future models.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.15949">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.15949.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.15949.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MotionEdit: Benchmarking and Learning Motion-Centric Image Editing</span>
        <span class="paper-authors">Yixin Wan, Lei Ke, Wenhao Yu, Kai-Wei Chang, Dong Yu</span>
        <span class="paper-meta">Updated 2025-12-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We introduce MotionEdit, a novel dataset for motion-centric image editing-the task of modifying subject actions and interactions while preserving identity, structure, and physical plausibility. Unlike existing image editing datasets that focus on static appearance changes or contain only sparse, low-quality motion edits, MotionEdit provides high-fidelity image pairs depicting realistic motion transformations extracted and verified from continuous videos. This new task is not only scientifically challenging but also practically significant, powering downstream applications such as frame-controlled video synthesis and animation.   To evaluate model performance on the novel task, we introduce MotionEdit-Bench, a benchmark that challenges models on motion-centric edits and measures model performance with generative, discriminative, and preference-based metrics. Benchmark results reveal that motion editing remains highly challenging for existing state-of-the-art diffusion-based editing models. To address this gap, we propose MotionNFT (Motion-guided Negative-aware Fine Tuning), a post-training framework that computes motion alignment rewards based on how well the motion flow between input and model-edited images matches the ground-truth motion, guiding models toward accurate motion transformations. Extensive experiments on FLUX.1 Kontext and Qwen-Image-Edit show that MotionNFT consistently improves editing quality and motion fidelity of both base models on the motion editing task without sacrificing general editing ability, demonstrating its effectiveness. Our code is at https://github.com/elainew728/motion-edit/.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.10284">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.10284.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.10284.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Self-Supervised Contrastive Embedding Adaptation for Endoscopic Image Matching</span>
        <span class="paper-authors">Alberto Rota, Elena De Momi</span>
        <span class="paper-meta">Updated 2025-12-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Accurate spatial understanding is essential for image-guided surgery, augmented reality integration and context awareness. In minimally invasive procedures, where visual input is the sole intraoperative modality, establishing precise pixel-level correspondences between endoscopic frames is critical for 3D reconstruction, camera tracking, and scene interpretation. However, the surgical domain presents distinct challenges: weak perspective cues, non-Lambertian tissue reflections, and complex, deformable anatomy degrade the performance of conventional computer vision techniques. While Deep Learning models have shown strong performance in natural scenes, their features are not inherently suited for fine-grained matching in surgical images and require targeted adaptation to meet the demands of this domain. This research presents a novel Deep Learning pipeline for establishing feature correspondences in endoscopic image pairs, alongside a self-supervised optimization framework for model training. The proposed methodology leverages a novel-view synthesis pipeline to generate ground-truth inlier correspondences, subsequently utilized for mining triplets within a contrastive learning paradigm. Through this self-supervised approach, we augment the DINOv2 backbone with an additional Transformer layer, specifically optimized to produce embeddings that facilitate direct matching through cosine similarity thresholding. Experimental evaluation demonstrates that our pipeline surpasses state-of-the-art methodologies on the SCARED datasets improved matching precision and lower epipolar error compared to the related work. The proposed framework constitutes a valuable contribution toward enabling more accurate high-level computer vision applications in surgical endoscopy.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.10379">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.10379.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.10379.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Value Gradient Guidance for Flow Matching Alignment</span>
        <span class="paper-authors">Zhen Liu et.al.</span>
        <span class="paper-meta">Updated 2025-12-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.05116">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.05116.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.05116.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Deep Forcing: Training-Free Long Video Generation with Deep Sink and Participative Compression</span>
        <span class="paper-authors">Jung Yi et.al.</span>
        <span class="paper-meta">Updated 2025-12-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.05081">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.05081.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.05081.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Improving Posterior Inference of Galaxy Properties with Image-Based Conditional Flow Matching</span>
        <span class="paper-authors">Mikaeel Yunus et.al.</span>
        <span class="paper-meta">Updated 2025-12-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.05078">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.05078.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.05078.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Generative Neural Video Compression via Video Diffusion Prior</span>
        <span class="paper-authors">Qi Mao et.al.</span>
        <span class="paper-meta">Updated 2025-12-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.05016">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.05016.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.05016.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Environment-Aware Channel Inference via Cross-Modal Flow: From Multimodal Sensing to Wireless Channels</span>
        <span class="paper-authors">Guangming Liang et.al.</span>
        <span class="paper-meta">Updated 2025-12-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.04966">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.04966.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.04966.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LatentFM: A Latent Flow Matching Approach for Generative Medical Image Segmentation</span>
        <span class="paper-authors">Huynh Trinh Ngoc et.al.</span>
        <span class="paper-meta">Updated 2025-12-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.04821">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.04821.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.04821.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Unveiling gravitational waves from core-collapse supernovae with MUSE</span>
        <span class="paper-authors">Alessandro Veutro et.al.</span>
        <span class="paper-meta">Updated 2025-12-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.04804">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.04804.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.04804.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Live Avatar: Streaming Real-time Audio-Driven Avatar Generation with Infinite Length</span>
        <span class="paper-authors">Yubo Huang et.al.</span>
        <span class="paper-meta">Updated 2025-12-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.04677">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.04677.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.04677.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Spectral micro-CT for quantitative analysis of calcification in fibrocartilage</span>
        <span class="paper-authors">Vittoria Mazzini et.al.</span>
        <span class="paper-meta">Updated 2025-12-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.04662">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.04662.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.04662.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DINO-RotateMatch: A Rotation-Aware Deep Framework for Robust Image Matching in Large-Scale 3D Reconstruction</span>
        <span class="paper-authors">Kaichen Zhang, Tianxiang Sheng, Xuanming Shi</span>
        <span class="paper-meta">Updated 2025-12-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">This paper presents DINO-RotateMatch, a deep-learning framework designed to address the chal lenges of image matching in large-scale 3D reconstruction from unstructured Internet images. The   method integrates a dataset-adaptive image pairing strategy with rotation-aware keypoint extraction and   matching. DINO is employed to retrieve semantically relevant image pairs in large collections, while   rotation-based augmentation captures orientation-dependent local features using ALIKED and Light Glue. Experiments on the Kaggle Image Matching Challenge 2025 demonstrate consistent improve ments in mean Average Accuracy (mAA), achieving a Silver Award (47th of 943 teams). The results   confirm that combining self-supervised global descriptors with rotation-enhanced local matching offers   a robust and scalable solution for large-scale 3D reconstruction.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.03715">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.03715.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.03715.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Fast 3D Ultrasound Localization Microscopy via Projection-based Processing Framework</span>
        <span class="paper-authors">Jingke Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-11-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.21647">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.21647.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.21647.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MoGAN: Improving Motion Quality in Video Diffusion via Few-Step Motion Adversarial Post-Training</span>
        <span class="paper-authors">Haotian Xue et.al.</span>
        <span class="paper-meta">Updated 2025-11-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.21592">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.21592.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.21592.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Semantic-Enhanced Feature Matching with Learnable Geometric Verification for Cross-Modal Neuron Registration</span>
        <span class="paper-authors">Wenwei Li et.al.</span>
        <span class="paper-meta">Updated 2025-11-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.21452">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.21452.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.21452.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">TSGM: Regular and Irregular Time-series Generation using Score-based Generative Models</span>
        <span class="paper-authors">Haksoo Lim et.al.</span>
        <span class="paper-meta">Updated 2025-11-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.21335">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.21335.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.21335.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Unlocking Zero-shot Potential of Semi-dense Image Matching via Gaussian Splatting</span>
        <span class="paper-authors">Juncheng Chen, Chao Xu, Yanjun Cao</span>
        <span class="paper-meta">Updated 2025-11-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Learning-based image matching critically depends on large-scale, diverse, and geometrically accurate training data. 3D Gaussian Splatting (3DGS) enables photorealistic novel-view synthesis and thus is attractive for data generation. However, its geometric inaccuracies and biased depth rendering currently prevent robust correspondence labeling. To address this, we introduce MatchGS, the first framework designed to systematically correct and leverage 3DGS for robust, zero-shot image matching. Our approach is twofold: (1) a geometrically-faithful data generation pipeline that refines 3DGS geometry to produce highly precise correspondence labels, enabling the synthesis of a vast and diverse range of viewpoints without compromising rendering fidelity; and (2) a 2D-3D representation alignment strategy that infuses 3DGS&#x27; explicit 3D knowledge into the 2D matcher, guiding 2D semi-dense matchers to learn viewpoint-invariant 3D representations. Our generated ground-truth correspondences reduce the epipolar error by up to 40 times compared to existing datasets, enable supervision under extreme viewpoint changes, and provide self-supervisory signals through Gaussian attributes. Consequently, state-of-the-art matchers trained solely on our data achieve significant zero-shot performance gains on public benchmarks, with improvements of up to 17.7%. Our work demonstrates that with proper geometric refinement, 3DGS can serve as a scalable, high-fidelity, and structurally-rich data source, paving the way for a new generation of robust zero-shot image matchers.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.21265">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.21265.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.21265.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">From Diffusion to One-Step Generation: A Comparative Study of Flow-Based Models with Application to Image Inpainting</span>
        <span class="paper-authors">Umang Agarwal et.al.</span>
        <span class="paper-meta">Updated 2025-11-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.21215">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.21215.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.21215.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Transformer Driven Visual Servoing and Dual Arm Impedance Control for Fabric Texture Matching</span>
        <span class="paper-authors">Fuyuki Tokuda et.al.</span>
        <span class="paper-meta">Updated 2025-11-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.21203">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.21203.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.21203.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Beyond Patch Aggregation: 3-Pass Pyramid Indexing for Vision-Enhanced Document Retrieval</span>
        <span class="paper-authors">Anup Roy et.al.</span>
        <span class="paper-meta">Updated 2025-11-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.21121">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.21121.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.21121.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">CLRecogEye : Curriculum Learning towards exploiting convolution features for Dynamic Iris Recognition</span>
        <span class="paper-authors">Geetanjali Sharma et.al.</span>
        <span class="paper-meta">Updated 2025-11-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.21097">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.21097.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.21097.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Deep Parameter Interpolation for Scalar Conditioning</span>
        <span class="paper-authors">Chicago Y. Park et.al.</span>
        <span class="paper-meta">Updated 2025-11-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.21028">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.21028.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.21028.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Breaking the Likelihood-Quality Trade-off in Diffusion Models by Merging Pretrained Experts</span>
        <span class="paper-authors">Yasin Esfandiari et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.19434">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.19434.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.19434.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Efficiency vs. Fidelity: A Comparative Analysis of Diffusion Probabilistic Models and Flow Matching on Low-Resource Hardware</span>
        <span class="paper-authors">Srishti Gupta et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.19379">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.19379.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.19379.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DeCo: Frequency-Decoupled Pixel Diffusion for End-to-End Image Generation</span>
        <span class="paper-authors">Zehong Ma et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.19365">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.19365.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.19365.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">BideDPO: Conditional Image Generation with Simultaneous Text and Condition Alignment</span>
        <span class="paper-authors">Dewei Zhou et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.19268">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.19268.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.19268.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DEAP-3DSAM: Decoder Enhanced and Auto Prompt SAM for 3D Medical Image Segmentation</span>
        <span class="paper-authors">Fangda Chen et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.19071">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.19071.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.19071.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Machine Learning Based Identification of Solar Disk and Plages in Kodaikanal Solar Observatory Historical Suncharts</span>
        <span class="paper-authors">Dibya Kirti Mishra et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.19040">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.19040.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.19040.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">VeCoR - Velocity Contrastive Regularization for Flow Matching</span>
        <span class="paper-authors">Zong-Wei Hong et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.18942">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.18942.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.18942.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FlowSteer: Guiding Few-Step Image Synthesis with Authentic Trajectories</span>
        <span class="paper-authors">Lei Ke et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.18834">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.18834.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.18834.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">VideoCompressa: Data-Efficient Video Understanding via Joint Temporal Compression and Spatial Reconstruction</span>
        <span class="paper-authors">Shaobo Wang et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.18831">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.18831.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.18831.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">NI-Tex: Non-isometric Image-based Garment Texture Generation</span>
        <span class="paper-authors">Hui Shan et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.18765">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.18765.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.18765.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MuM: Multi-View Masked Image Modeling for 3D Vision</span>
        <span class="paper-authors">David Nordström et.al.</span>
        <span class="paper-meta">Updated 2025-11-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.17309">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.17309.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.17309.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">RoMa v2: Harder Better Faster Denser Feature Matching</span>
        <span class="paper-authors">Johan Edstedt et.al.</span>
        <span class="paper-meta">Updated 2025-11-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.15706">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.15706.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.15706.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">What Your Features Reveal: Data-Efficient Black-Box Feature Inversion Attack for Split DNNs</span>
        <span class="paper-authors">Zhihan Ren et.al.</span>
        <span class="paper-meta">Updated 2025-11-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.15316">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.15316.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.15316.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Magnetic signal scan imaging system based on giant magnetoimpedance (GMI) differential sensor</span>
        <span class="paper-authors">Tao Yang et.al.</span>
        <span class="paper-meta">Updated 2025-11-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.15209">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.15209.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.15209.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">BokehFlow: Depth-Free Controllable Bokeh Rendering via Flow Matching</span>
        <span class="paper-authors">Yachuan Huang et.al.</span>
        <span class="paper-meta">Updated 2025-11-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.15066">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.15066.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.15066.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Computer Vision Modeling of the Development of Geometric and Numerical Concepts in Humans</span>
        <span class="paper-authors">Zekun Wang et.al.</span>
        <span class="paper-meta">Updated 2025-11-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.15029">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.15029.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.15029.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LFreeDA: Label-Free Drift Adaptation for Windows Malware Detection</span>
        <span class="paper-authors">Adrian Shuai Li et.al.</span>
        <span class="paper-meta">Updated 2025-11-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.14963">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.14963.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.14963.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FlowRoI A Fast Optical Flow Driven Region of Interest Extraction Framework for High-Throughput Image Compression in Immune Cell Migration Analysis</span>
        <span class="paper-authors">Xiaowei Xu et.al.</span>
        <span class="paper-meta">Updated 2025-11-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.14419">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.14419.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.14419.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Cranio-ID: Graph-Based Craniofacial Identification via Automatic Landmark Annotation in 2D Multi-View X-rays</span>
        <span class="paper-authors">Ravi Shankar Prasad et.al.</span>
        <span class="paper-meta">Updated 2025-11-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.14411">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.14411.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.14411.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Dental3R: Geometry-Aware Pairing for Intraoral 3D Reconstruction from Sparse-View Photographs</span>
        <span class="paper-authors">Yiyi Miao et.al.</span>
        <span class="paper-meta">Updated 2025-11-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.14315">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.14315.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.14315.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">NeuralBoneReg: A Novel Self-Supervised Method for Robust and Accurate Multi-Modal Bone Surface Registration</span>
        <span class="paper-authors">Luohong Wu et.al.</span>
        <span class="paper-meta">Updated 2025-11-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.14286">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.14286.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.14286.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SOMA: Feature Gradient Enhanced Affine-Flow Matching for SAR-Optical Registration</span>
        <span class="paper-authors">Haodong Wang et.al.</span>
        <span class="paper-meta">Updated 2025-11-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.13168">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.13168.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.13168.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">The Persistence of Cultural Memory: Investigating Multimodal Iconicity in Diffusion Models</span>
        <span class="paper-authors">Maria-Teresa De Rosa Palmini et.al.</span>
        <span class="paper-meta">Updated 2025-11-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.11435">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.11435.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.11435.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">U(PM)$^2$:Unsupervised polygon matching with pre-trained models for challenging stereo images</span>
        <span class="paper-authors">Chang Li et.al.</span>
        <span class="paper-meta">Updated 2025-11-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.05949">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.05949.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.05949.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Robust Alignment of the Human Embryo in 3D Ultrasound using PCA and an Ensemble of Heuristic, Atlas-based and Learning-based Classifiers Evaluated on the Rotterdam Periconceptional Cohort</span>
        <span class="paper-authors">Nikolai Herrmann et.al.</span>
        <span class="paper-meta">Updated 2025-11-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.03416">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.03416.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.03416.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Object Detection as an Optional Basis: A Graph Matching Network for Cross-View UAV Localization</span>
        <span class="paper-authors">Tao Liu et.al.</span>
        <span class="paper-meta">Updated 2025-11-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.02489">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.02489.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.02489.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">The MDW Hα Sky Survey: Data Release 1</span>
        <span class="paper-authors">Noor Aftab et.al.</span>
        <span class="paper-meta">Updated 2025-10-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.22900">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.22900.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.22900.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FairJudge: MLLM Judging for Social Attributes and Prompt Image Alignment</span>
        <span class="paper-authors">Zahraa Al Sahili et.al.</span>
        <span class="paper-meta">Updated 2025-10-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.22827">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.22827.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.22827.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SegMASt3R: Geometry Grounded Segment Matching</span>
        <span class="paper-authors">Rohit Jayanti et.al.</span>
        <span class="paper-meta">Updated 2025-10-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.05051">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.05051.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.05051.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Lattice-allocated Real-time Line Segment Feature Detection and Tracking Using Only an Event-based Camera</span>
        <span class="paper-authors">Mikihiro Ikura et.al.</span>
        <span class="paper-meta">Updated 2025-10-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.06829">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.06829.pdf">PDF</a>
          <a class="chip" href="https://github.com/event-driven-robotics/RT-EvLDT">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.06829.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">StyleKeeper: Prevent Content Leakage using Negative Visual Query Guidance</span>
        <span class="paper-authors">Jaeseok Jeong et.al.</span>
        <span class="paper-meta">Updated 2025-10-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.06827">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.06827.pdf">PDF</a>
          <a class="chip" href="https://github.com/naver-ai/StyleKeeper">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.06827.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Efficient Discriminative Joint Encoders for Large Scale Vision-Language Reranking</span>
        <span class="paper-authors">Mitchell Keren Taraday et.al.</span>
        <span class="paper-meta">Updated 2025-10-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.06820">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.06820.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.06820.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Loc$^2$: Interpretable Cross-View Localization via Depth-Lifted Local Feature Matching</span>
        <span class="paper-authors">Zimin Xia et.al.</span>
        <span class="paper-meta">Updated 2025-09-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.09792">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.09792.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.09792.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Hierarchical Neural Semantic Representation for 3D Semantic Correspondence</span>
        <span class="paper-authors">Keyu Du et.al.</span>
        <span class="paper-meta">Updated 2025-09-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.17431">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.17431.pdf">PDF</a>
          <a class="chip" href="https://github.com/mapledky/NSR_PyTorch">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.17431.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Handling Multiple Hypotheses in Coarse-to-Fine Dense Image Matching</span>
        <span class="paper-authors">Matthieu Vilain et.al.</span>
        <span class="paper-meta">Updated 2025-09-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.08805">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.08805.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.08805.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">PM25Vision: A Large-Scale Benchmark Dataset for Visual Estimation of Air Quality</span>
        <span class="paper-authors">Yang Han et.al.</span>
        <span class="paper-meta">Updated 2025-09-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.16519">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.16519.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.16519.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DistillMatch: Leveraging Knowledge Distillation from Vision Foundation Model for Multimodal Image Matching</span>
        <span class="paper-authors">Meng Yang et.al.</span>
        <span class="paper-meta">Updated 2025-09-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.16017">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.16017.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.16017.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">RoboEye: Enhancing 2D Robotic Object Identification with Selective 3D Geometric Keypoint Matching</span>
        <span class="paper-authors">Xingwu Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-09-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.14966">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.14966.pdf">PDF</a>
          <a class="chip" href="https://github.com/longkukuhi/RoboEye">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.14966.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A Geometrically Consistent Matching Framework for Side-Scan Sonar Mapping</span>
        <span class="paper-authors">Can Lei et.al.</span>
        <span class="paper-meta">Updated 2025-09-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.11255">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.11255.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.11255.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ObjectReact: Learning Object-Relative Control for Visual Navigation</span>
        <span class="paper-authors">Sourav Garg et.al.</span>
        <span class="paper-meta">Updated 2025-09-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.09594">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.09594.pdf">PDF</a>
          <a class="chip" href="https://github.com/oravus/object-react">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.09594.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">POEv2: a flexible and robust framework for generic line segment detection and wireframe line segment detection</span>
        <span class="paper-authors">Chenguang Liu et.al.</span>
        <span class="paper-meta">Updated 2025-09-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2508.19742">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2508.19742.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2508.19742.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Back To The Drawing Board: Rethinking Scene-Level Sketch-Based Image Retrieval</span>
        <span class="paper-authors">Emil Demić et.al.</span>
        <span class="paper-meta">Updated 2025-09-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.06566">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.06566.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.06566.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Dual-Scale Volume Priors with Wasserstein-Based Consistency for Semi-Supervised Medical Image Segmentation</span>
        <span class="paper-authors">Junying Meng et.al.</span>
        <span class="paper-meta">Updated 2025-09-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.04273">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.04273.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.04273.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Revisiting Cross-View Localization from Image Matching</span>
        <span class="paper-authors">Panwang Xia et.al.</span>
        <span class="paper-meta">Updated 2025-08-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2508.10716">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2508.10716.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2508.10716.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A Sub-Pixel Multimodal Optical Remote Sensing Images Matching Method</span>
        <span class="paper-authors">Tao Huang et.al.</span>
        <span class="paper-meta">Updated 2025-08-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2508.10294">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2508.10294.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2508.10294.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Episodic Memory Representation for Long-form Video Understanding</span>
        <span class="paper-authors">Yun Wang et.al.</span>
        <span class="paper-meta">Updated 2025-08-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2508.09486">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2508.09486.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2508.09486.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">VISOR: Visual Input-based Steering for Output Redirection in Vision-Language Models</span>
        <span class="paper-authors">Mansi Phute et.al.</span>
        <span class="paper-meta">Updated 2025-08-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2508.08521">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2508.08521.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2508.08521.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Semi-supervised Multiscale Matching for SAR-Optical Image</span>
        <span class="paper-authors">Jingze Gai et.al.</span>
        <span class="paper-meta">Updated 2025-08-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2508.07812">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2508.07812.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2508.07812.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Dual-Granularity Cross-Modal Identity Association for Weakly-Supervised Text-to-Person Image Matching</span>
        <span class="paper-authors">Yafei Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-07-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.06744">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.06744.pdf">PDF</a>
          <a class="chip" href="https://github.com/syl6312/DGCMIA">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.06744.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Q-Frame: Query-aware Frame Selection and Multi-Resolution Adaptation for Video-LLMs</span>
        <span class="paper-authors">Shaojie Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-07-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.22139">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.22139.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.22139.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">From Query to Explanation: Uni-RAG for Multi-Modal Retrieval-Augmented Learning in STEM</span>
        <span class="paper-authors">Xinyi Wu et.al.</span>
        <span class="paper-meta">Updated 2025-07-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.03868">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.03868.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.03868.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">What does really matter in image goal navigation?</span>
        <span class="paper-authors">Gianluca Monaci et.al.</span>
        <span class="paper-meta">Updated 2025-07-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.01667">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.01667.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.01667.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Efficient and Accurate Image Provenance Analysis: A Scalable Pipeline for Large-scale Images</span>
        <span class="paper-authors">Jiewei Lai et.al.</span>
        <span class="paper-meta">Updated 2025-06-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.23707">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.23707.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.23707.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Dynamic Contrastive Learning for Hierarchical Retrieval: A Case Study of Distance-Aware Cross-View Geo-Localization</span>
        <span class="paper-authors">Suofei Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-06-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.23077">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.23077.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.23077.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MatChA: Cross-Algorithm Matching with Feature Augmentation</span>
        <span class="paper-authors">Paula Carbó Cubero et.al.</span>
        <span class="paper-meta">Updated 2025-06-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.22336">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.22336.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.22336.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ZeroReg3D: A Zero-shot Registration Pipeline for 3D Consecutive Histopathology Image Reconstruction</span>
        <span class="paper-authors">Juming Xiong et.al.</span>
        <span class="paper-meta">Updated 2025-06-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.21923">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.21923.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.21923.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Fast entropy-regularized SDP relaxations for permutation synchronization</span>
        <span class="paper-authors">Michael Lindsey et.al.</span>
        <span class="paper-meta">Updated 2025-06-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.20191">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.20191.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.20191.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SR3D: Unleashing Single-view 3D Reconstruction for Transparent and Specular Object Grasping</span>
        <span class="paper-authors">Mingxu Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-06-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.24305">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.24305.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.24305.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ReSeDis: A Dataset for Referring-based Object Search across Large-Scale Image Collections</span>
        <span class="paper-authors">Ziling Huang et.al.</span>
        <span class="paper-meta">Updated 2025-06-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.15180">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.15180.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.15180.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">EmbodiedPlace: Learning Mixture-of-Features with Embodied Constraints for Visual Place Recognition</span>
        <span class="paper-authors">Bingxi Liu et.al.</span>
        <span class="paper-meta">Updated 2025-06-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.13133">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.13133.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.13133.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">RealKeyMorph: Keypoints in Real-world Coordinates for Resolution-agnostic Image Registration</span>
        <span class="paper-authors">Mina C. Moghadam et.al.</span>
        <span class="paper-meta">Updated 2025-06-12</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.10344">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.10344.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.10344.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Hierarchical Image Matching for UAV Absolute Visual Localization via Semantic and Structural Constraints</span>
        <span class="paper-authors">Xiangkai Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-06-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.09748">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.09748.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.09748.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ScaleLSD: Scalable Deep Line Segment Detection Streamlined</span>
        <span class="paper-authors">Zeran Ke et.al.</span>
        <span class="paper-meta">Updated 2025-06-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.09369">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.09369.pdf">PDF</a>
          <a class="chip" href="https://github.com/ant-research/scalelsd">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.09369.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Vanishing arcs for isolated plane curve singularities</span>
        <span class="paper-authors">Hanwool Bae et.al.</span>
        <span class="paper-meta">Updated 2025-06-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.04917">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.04917.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.04917.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Deep Learning Reforms Image Matching: A Survey and Outlook</span>
        <span class="paper-authors">Shihua Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-06-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.04619">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.04619.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.04619.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Universal Domain Adaptation for Semantic Segmentation</span>
        <span class="paper-authors">Seun-An Choe et.al.</span>
        <span class="paper-meta">Updated 2025-06-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.22458">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.22458.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.22458.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">To Glue or Not to Glue? Classical vs Learned Image Matching for Mobile Mapping Cameras to Textured Semantic 3D Building Models</span>
        <span class="paper-authors">Simone Gaisbauer et.al.</span>
        <span class="paper-meta">Updated 2025-05-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.17973">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.17973.pdf">PDF</a>
          <a class="chip" href="https://github.com/simbauer/to_glue_or_not_to_glue">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.17973.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Anti-interrupted sampling repeater jamming via linear canonical Wigner distribution lightweight LFM detection</span>
        <span class="paper-authors">Jia-Mian Li et.al.</span>
        <span class="paper-meta">Updated 2025-05-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.06302">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.06302.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.06302.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Multi-view dense image matching with similarity learning and geometry priors</span>
        <span class="paper-authors">Mohamed Ali Chebbi et.al.</span>
        <span class="paper-meta">Updated 2025-05-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.11264">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.11264.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.11264.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Mitigating Modality Bias in Multi-modal Entity Alignment from a Causal Perspective</span>
        <span class="paper-authors">Taoyu Su et.al.</span>
        <span class="paper-meta">Updated 2025-05-15</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.19458">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.19458.pdf">PDF</a>
          <a class="chip" href="https://github.com/sutaoyu/CDMEA">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.19458.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Boosting Global-Local Feature Matching via Anomaly Synthesis for Multi-Class Point Cloud Anomaly Detection</span>
        <span class="paper-authors">Yuqi Cheng et.al.</span>
        <span class="paper-meta">Updated 2025-05-12</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.07375">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.07375.pdf">PDF</a>
          <a class="chip" href="https://github.com/hustCYQ/GLFM-Multi-class-3DAD">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.07375.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LiftFeat: 3D Geometry-Aware Local Feature Matching</span>
        <span class="paper-authors">Yepeng Liu et.al.</span>
        <span class="paper-meta">Updated 2025-05-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.03422">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.03422.pdf">PDF</a>
          <a class="chip" href="https://github.com/lyp-deeplearning/liftfeat">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.03422.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">OBD-Finder: Explainable Coarse-to-Fine Text-Centric Oracle Bone Duplicates Discovery</span>
        <span class="paper-authors">Chongsheng Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-05-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.03836">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.03836.pdf">PDF</a>
          <a class="chip" href="https://github.com/cszhanglmu/obd-finder">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.03836.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Focus What Matters: Matchability-Based Reweighting for Local Feature Matching</span>
        <span class="paper-authors">Dongyue Li et.al.</span>
        <span class="paper-meta">Updated 2025-05-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.02161">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.02161.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.02161.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Dynamic Arthroscopic Navigation System for Anterior Cruciate Ligament Reconstruction Based on Multi-level Memory Architecture</span>
        <span class="paper-authors">Shuo Wang et.al.</span>
        <span class="paper-meta">Updated 2025-04-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.19398">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.19398.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.19398.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Road Similarity-Based BEV-Satellite Image Matching for UGV Localization</span>
        <span class="paper-authors">Zhenping Sun et.al.</span>
        <span class="paper-meta">Updated 2025-04-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.16346">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.16346.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.16346.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">To Match or Not to Match: Revisiting Image Matching for Reliable Visual Place Recognition</span>
        <span class="paper-authors">Davide Sferrazza et.al.</span>
        <span class="paper-meta">Updated 2025-04-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.06116">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.06116.pdf">PDF</a>
          <a class="chip" href="https://github.com/FarInHeight/To-Match-or-Not-to-Match">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.06116.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Outlier-Robust Multi-Model Fitting on Quantum Annealers</span>
        <span class="paper-authors">Saurabh Pandey et.al.</span>
        <span class="paper-meta">Updated 2025-04-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.13836">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.13836.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.13836.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Geometric Consistency Refinement for Single Image Novel View Synthesis via Test-Time Adaptation of Diffusion Models</span>
        <span class="paper-authors">Josef Bengtson et.al.</span>
        <span class="paper-meta">Updated 2025-04-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.08348">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.08348.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.08348.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Image registration of 2D optical thin sections in a 3D porous medium: Application to a Berea sandstone digital rock image</span>
        <span class="paper-authors">Jaehong Chung et.al.</span>
        <span class="paper-meta">Updated 2025-04-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.06604">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.06604.pdf">PDF</a>
          <a class="chip" href="https://github.com/jh-chung1/imgregister2dto3d">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.06604.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Learning Affine Correspondences by Integrating Geometric Constraints</span>
        <span class="paper-authors">Pengju Sun et.al.</span>
        <span class="paper-meta">Updated 2025-04-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.04834">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.04834.pdf">PDF</a>
          <a class="chip" href="https://github.com/stilcrad/denseaffine">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.04834.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Scaling Prompt Instructed Zero Shot Composed Image Retrieval with Image-Only Data</span>
        <span class="paper-authors">Yiqun Duan et.al.</span>
        <span class="paper-meta">Updated 2025-04-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.00812">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.00812.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.00812.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">CoMatch: Dynamic Covisibility-Aware Transformer for Bilateral Subpixel-Level Semi-Dense Image Matching</span>
        <span class="paper-authors">Zizhuo Li et.al.</span>
        <span class="paper-meta">Updated 2025-03-31</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.23925">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.23925.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.23925.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Pairwise Matching of Intermediate Representations for Fine-grained Explainability</span>
        <span class="paper-authors">Lauren Shrack et.al.</span>
        <span class="paper-meta">Updated 2025-03-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.22881">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.22881.pdf">PDF</a>
          <a class="chip" href="https://github.com/pairx-explains/pairx">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.22881.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Multimodal Image Matching based on Frequency-domain Information of Local Energy Response</span>
        <span class="paper-authors">Meng Yang et.al.</span>
        <span class="paper-meta">Updated 2025-03-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.20827">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.20827.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.20827.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Normalized Matching Transformer</span>
        <span class="paper-authors">Abtin Pourhadi et.al.</span>
        <span class="paper-meta">Updated 2025-03-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.17715">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.17715.pdf">PDF</a>
          <a class="chip" href="https://github.com/apollos1301/normmatchtrans">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.17715.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Loop Closure from Two Views: Revisiting PGO for Scalable Trajectory Estimation through Monocular Priors</span>
        <span class="paper-authors">Tian Yi Lim et.al.</span>
        <span class="paper-meta">Updated 2025-03-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.16275">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.16275.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.16275.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MapGlue: Multimodal Remote Sensing Image Matching</span>
        <span class="paper-authors">Peihao Wu et.al.</span>
        <span class="paper-meta">Updated 2025-03-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.16185">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.16185.pdf">PDF</a>
          <a class="chip" href="https://github.com/peihaowu/mapglue">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.16185.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">PAPI-Reg: Patch-to-Pixel Solution for Efficient Cross-Modal Registration between LiDAR Point Cloud and Camera Image</span>
        <span class="paper-authors">Yuanchao Yue et.al.</span>
        <span class="paper-meta">Updated 2025-03-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.15285">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.15285.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.15285.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Less Biased Noise Scale Estimation for Threshold-Robust RANSAC</span>
        <span class="paper-authors">Johan Edstedt et.al.</span>
        <span class="paper-meta">Updated 2025-03-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.13433">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.13433.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.13433.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SatDepth: A Novel Dataset for Satellite Image Matching</span>
        <span class="paper-authors">Rahul Deshmukh et.al.</span>
        <span class="paper-meta">Updated 2025-03-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.12706">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.12706.pdf">PDF</a>
          <a class="chip" href="https://github.com/rahuldeshmukh43/satdepth">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.12706.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Refining Image Edge Detection via Linear Canonical Riesz Transforms</span>
        <span class="paper-authors">Shuhui Yang et.al.</span>
        <span class="paper-meta">Updated 2025-03-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.11148">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.11148.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.11148.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Speedy MASt3R</span>
        <span class="paper-authors">Jingxing Li et.al.</span>
        <span class="paper-meta">Updated 2025-03-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.10017">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.10017.pdf">PDF</a>
          <a class="chip" href="https://github.com/ASU-ESIC-FAN-Lab/speedy_mast3r">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.10017.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Keypoint Detection and Description for Raw Bayer Images</span>
        <span class="paper-authors">Jiakai Lin et.al.</span>
        <span class="paper-meta">Updated 2025-03-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.08673">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.08673.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.08673.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Diff-Reg v2: Diffusion-Based Matching Matrix Estimation for Image Matching and 3D Registration</span>
        <span class="paper-authors">Qianliang Wu et.al.</span>
        <span class="paper-meta">Updated 2025-03-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.04127">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.04127.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.04127.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Learning 3D Medical Image Models From Brain Functional Connectivity Network Supervision For Mental Disorder Diagnosis</span>
        <span class="paper-authors">Xingcan Hu et.al.</span>
        <span class="paper-meta">Updated 2025-03-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.04205">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.04205.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.04205.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">JamMa: Ultra-lightweight Local Feature Matching with Joint Mamba</span>
        <span class="paper-authors">Xiaoyong Lu et.al.</span>
        <span class="paper-meta">Updated 2025-03-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.03437">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.03437.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.03437.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">CNSv2: Probabilistic Correspondence Encoded Neural Image Servo</span>
        <span class="paper-authors">Anzhe Chen et.al.</span>
        <span class="paper-meta">Updated 2025-02-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.00132">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.00132.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.00132.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A2-GNN: Angle-Annular GNN for Visual Descriptor-free Camera Relocalization</span>
        <span class="paper-authors">Yejun Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-02-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2502.20036">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2502.20036.pdf">PDF</a>
          <a class="chip" href="https://github.com/yejunzhang/a2-gnn">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2502.20036.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">RUBIK: A Structured Benchmark for Image Matching across Geometric Challenges</span>
        <span class="paper-authors">Thibaut Loiseau et.al.</span>
        <span class="paper-meta">Updated 2025-02-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2502.19955">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2502.19955.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2502.19955.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">BEV-LIO(LC): BEV Image Assisted LiDAR-Inertial Odometry with Loop Closure</span>
        <span class="paper-authors">Haoxin Cai et.al.</span>
        <span class="paper-meta">Updated 2025-02-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2502.19242">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2502.19242.pdf">PDF</a>
          <a class="chip" href="https://github.com/hxca1/bev-lio-lc">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2502.19242.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">PromptMID: Modal Invariant Descriptors Based on Diffusion and Vision Foundation Models for Optical-SAR Image Matching</span>
        <span class="paper-authors">Han Nie et.al.</span>
        <span class="paper-meta">Updated 2025-02-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2502.18104">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2502.18104.pdf">PDF</a>
          <a class="chip" href="https://github.com/hanniewhu/promptmid">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2502.18104.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
</section>
