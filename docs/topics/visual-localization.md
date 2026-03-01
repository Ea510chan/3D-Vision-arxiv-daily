---
layout: default
title: Visual Localization
---

<section class="topic-hero" style="--accent: #9bfffc;">
  <div>
    <p class="eyebrow">Topic</p>
    <h1>Visual Localization</h1>
    <p class="topic-lede">Updated 2026.03.01 · 360 papers</p>
  </div>
  <a class="btn ghost" href="../index.html#topics">← Back to topics</a>
</section>

<section class="paper-grid">
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">WISER: Wider Search, Deeper Thinking, and Adaptive Fusion for Training-Free Zero-Shot Composed Image Retrieval</span>
        <span class="paper-authors">Tianyue Wang, Leigang Qu, Tianyu Yang, Xiangzhao Hao, Yifan Xu, Haiyun Guo, Jinqiao Wang</span>
        <span class="paper-meta">Updated 2026-02-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Zero-Shot Composed Image Retrieval (ZS-CIR) aims to retrieve target images given a multimodal query (comprising a reference image and a modification text), without training on annotated triplets. Existing methods typically convert the multimodal query into a single modality-either as an edited caption for Text-to-Image retrieval (T2I) or as an edited image for Image-to-Image retrieval (I2I). However, each paradigm has inherent limitations: T2I often loses fine-grained visual details, while I2I struggles with complex semantic modifications. To effectively leverage their complementary strengths under diverse query intents, we propose WISER, a training-free framework that unifies T2I and I2I via a &quot;retrieve-verify-refine&quot; pipeline, explicitly modeling intent awareness and uncertainty awareness. Specifically, WISER first performs Wider Search by generating both edited captions and images for parallel retrieval to broaden the candidate pool. Then, it conducts Adaptive Fusion with a verifier to assess retrieval confidence, triggering refinement for uncertain retrievals, and dynamically fusing the dual-path for reliable ones. For uncertain retrievals, WISER generates refinement suggestions through structured self-reflection to guide the next retrieval round toward Deeper Thinking. Extensive experiments demonstrate that WISER significantly outperforms previous methods across multiple benchmarks, achieving relative improvements of 45% on CIRCO (mAP@5) and 57% on CIRR (Recall@1) over existing training-free methods. Notably, it even surpasses many training-dependent methods, highlighting its superiority and generalization under diverse scenarios. Code will be released at https://github.com/Physicsmile/WISER.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.23029">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.23029.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.23029.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Autoregressive Visual Decoding from EEG Signals</span>
        <span class="paper-authors">Sicheng Dai, Hongwang Xiao, Shan Yu, Qiwei Ye</span>
        <span class="paper-meta">Updated 2026-02-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Electroencephalogram (EEG) signals have become a popular medium for decoding visual information due to their cost-effectiveness and high temporal resolution. However, current approaches face significant challenges in bridging the modality gap between EEG and image data. These methods typically rely on complex adaptation processes involving multiple stages, making it hard to maintain consistency and manage compounding errors. Furthermore, the computational overhead imposed by large-scale diffusion models limit their practicality in real-world brain-computer interface (BCI) applications. In this work, we present AVDE, a lightweight and efficient framework for visual decoding from EEG signals. First, we leverage LaBraM, a pre-trained EEG model, and fine-tune it via contrastive learning to align EEG and image representations. Second, we adopt an autoregressive generative framework based on a &quot;next-scale prediction&quot; strategy: images are encoded into multi-scale token maps using a pre-trained VQ-VAE, and a transformer is trained to autoregressively predict finer-scale tokens starting from EEG embeddings as the coarsest representation. This design enables coherent generation while preserving a direct connection between the input EEG signals and the reconstructed images. Experiments on two datasets show that AVDE outperforms previous state-of-the-art methods in both image retrieval and reconstruction tasks, while using only 10% of the parameters. In addition, visualization of intermediate outputs shows that the generative process of AVDE reflects the hierarchical nature of human visual perception. These results highlight the potential of autoregressive models as efficient and interpretable tools for practical BCI applications.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.22555">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.22555.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.22555.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Pix2Key: Controllable Open-Vocabulary Retrieval with Semantic Decomposition and Self-Supervised Visual Dictionary Learning</span>
        <span class="paper-authors">Guoyizhe Wei, Yang Jiao, Nan Xi, Zhishen Huang, Jingjing Meng, Rama Chellappa, Yan Gao</span>
        <span class="paper-meta">Updated 2026-02-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Composed Image Retrieval (CIR) uses a reference image plus a natural-language edit to retrieve images that apply the requested change while preserving other relevant visual content. Classic fusion pipelines typically rely on supervised triplets and can lose fine-grained cues, while recent zero-shot approaches often caption the reference image and merge the caption with the edit, which may miss implicit user intent and return repetitive results. We present Pix2Key, which represents both queries and candidates as open-vocabulary visual dictionaries, enabling intent-aware constraint matching and diversity-aware reranking in a unified embedding space. A self-supervised pretraining component, V-Dict-AE, further improves the dictionary representation using only images, strengthening fine-grained attribute understanding without CIR-specific supervision. On the DFMM-Compose benchmark, Pix2Key improves Recall@10 up to 3.2 points, and adding V-Dict-AE yields an additional 2.3-point gain while improving intent consistency and maintaining high list diversity.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.22510">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.22510.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.22510.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Automatic Map Density Selection for Locally-Performant Visual Place Recognition</span>
        <span class="paper-authors">Somayeh Hussaini, Tobias Fischer, Michael Milford</span>
        <span class="paper-meta">Updated 2026-02-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">A key challenge in translating Visual Place Recognition (VPR) from the lab to long-term deployment is ensuring a priori that a system can meet user-specified performance requirements across different parts of an environment, rather than just on average globally. A critical mechanism for controlling local VPR performance is the density of the reference mapping database, yet this factor is largely neglected in existing work, where benchmark datasets with fixed, engineering-driven (sensors, storage, GPS frequency) sampling densities are typically used. In this paper, we propose a dynamic VPR mapping approach that uses pairs of reference traverses from the target environment to automatically select an appropriate map density to satisfy two user-defined requirements: (1) a target Local Recall@1 level, and (2) the proportion of the operational environment over which this requirement must be met or exceeded, which we term the Recall Achievement Rate (RAR). Our approach is based on the hypothesis that match patterns between multiple reference traverses, evaluated across different map densities, can be modelled to predict the density required to meet these performance targets on unseen deployment data. Through extensive experiments across multiple VPR methods and the Nordland and Oxford RobotCar benchmarks, we show that our system consistently achieves or exceeds the specified local recall level over at least the user-specified proportion of the environment. Comparisons with alternative baselines demonstrate that our approach reliably selects the correct operating point in map density, avoiding unnecessary over-densification. Finally, ablation studies and analysis evaluate sensitivity to reference map choice and local space definitions, and reveal that conventional global Recall@1 is a poor predictor of the often more operationally meaningful RAR metric.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.21473">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.21473.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.21473.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Seeing Through Words: Controlling Visual Retrieval Quality with Language Models</span>
        <span class="paper-authors">Jianglin Lu, Simon Jenni, Kushal Kafle, Jing Shi, Handong Zhao, Yun Fu</span>
        <span class="paper-meta">Updated 2026-02-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Text-to-image retrieval is a fundamental task in vision-language learning, yet in real-world scenarios it is often challenged by short and underspecified user queries. Such queries are typically only one or two words long, rendering them semantically ambiguous, prone to collisions across diverse visual interpretations, and lacking explicit control over the quality of retrieved images. To address these issues, we propose a new paradigm of quality-controllable retrieval, which enriches short queries with contextual details while incorporating explicit notions of image quality. Our key idea is to leverage a generative language model as a query completion function, extending underspecified queries into descriptive forms that capture fine-grained visual attributes such as pose, scene, and aesthetics. We introduce a general framework that conditions query completion on discretized quality levels, derived from relevance and aesthetic scoring models, so that query enrichment is not only semantically meaningful but also quality-aware. The resulting system provides three key advantages: 1) flexibility, it is compatible with any pretrained vision-language model (VLMs) without modification; 2) transparency, enriched queries are explicitly interpretable by users; and 3) controllability, enabling retrieval results to be steered toward user-preferred quality levels. Extensive experiments demonstrate that our proposed approach significantly improves retrieval results and provides effective quality control, bridging the gap between the expressive capacity of modern VLMs and the underspecified nature of short user queries. Our code is available at https://github.com/Jianglin954/QCQC.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.21175">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.21175.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.21175.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LST-SLAM: A Stereo Thermal SLAM System for Kilometer-Scale Dynamic Environments</span>
        <span class="paper-authors">Zeyu Jiang, Kuan Xu, Changhao Chen</span>
        <span class="paper-meta">Updated 2026-02-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Thermal cameras offer strong potential for robot perception under challenging illumination and weather conditions. However, thermal Simultaneous Localization and Mapping (SLAM) remains difficult due to unreliable feature extraction, unstable motion tracking, and inconsistent global pose and map construction, particularly in dynamic large-scale outdoor environments. To address these challenges, we propose LST-SLAM, a novel large-scale stereo thermal SLAM system that achieves robust performance in complex, dynamic scenes. Our approach combines self-supervised thermal feature learning, stereo dual-level motion tracking, and geometric pose optimization. We also introduce a semantic-geometric hybrid constraint that suppresses potentially dynamic features lacking strong inter-frame geometric consistency. Furthermore, we develop an online incremental bag-of-words model for loop closure detection, coupled with global pose optimization to mitigate accumulated drift. Extensive experiments on kilometer-scale dynamic thermal datasets show that LST-SLAM significantly outperforms recent representative SLAM systems, including AirSLAM and DROID-SLAM, in both robustness and accuracy.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.20925">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.20925.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.20925.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Unlocking Multimodal Document Intelligence: From Current Triumphs to Future Frontiers of Visual Document Retrieval</span>
        <span class="paper-authors">Yibo Yan, Jiahao Huo, Guanbo Feng, Mingdong Ou, Yi Cao, Xin Zou, Shuliang Liu, Yuanhuiyi Lyu, Yu Huang, Jungang Li, Kening Zheng, Xu Zheng, Philip S. Yu, James Kwok, Xuming Hu</span>
        <span class="paper-meta">Updated 2026-02-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">With the rapid proliferation of multimodal information, Visual Document Retrieval (VDR) has emerged as a critical frontier in bridging the gap between unstructured visually rich data and precise information acquisition. Unlike traditional natural image retrieval, visual documents exhibit unique characteristics defined by dense textual content, intricate layouts, and fine-grained semantic dependencies. This paper presents the first comprehensive survey of the VDR landscape, specifically through the lens of the Multimodal Large Language Model (MLLM) era. We begin by examining the benchmark landscape, and subsequently dive into the methodological evolution, categorizing approaches into three primary aspects: multimodal embedding models, multimodal reranker models, and the integration of Retrieval-Augmented Generation (RAG) and Agentic systems for complex document intelligence. Finally, we identify persistent challenges and outline promising future directions, aiming to provide a clear roadmap for future multimodal document intelligence.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.19961">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.19961.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.19961.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">VGGT-MPR: VGGT-Enhanced Multimodal Place Recognition in Autonomous Driving Environments</span>
        <span class="paper-authors">Jingyi Xu, Zhangshuo Qi, Zhongmiao Yan, Xuyu Gao, Qianyun Jiao, Songpengcheng Xia, Xieyuanli Chen, Ling Pei</span>
        <span class="paper-meta">Updated 2026-02-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">In autonomous driving, robust place recognition is critical for global localization and loop closure detection. While inter-modality fusion of camera and LiDAR data in multimodal place recognition (MPR) has shown promise in overcoming the limitations of unimodal counterparts, existing MPR methods basically attend to hand-crafted fusion strategies and heavily parameterized backbones that require costly retraining. To address this, we propose VGGT-MPR, a multimodal place recognition framework that adopts the Visual Geometry Grounded Transformer (VGGT) as a unified geometric engine for both global retrieval and re-ranking. In the global retrieval stage, VGGT extracts geometrically-rich visual embeddings through prior depth-aware and point map supervision, and densifies sparse LiDAR point clouds with predicted depth maps to improve structural representation. This enhances the discriminative ability of fused multimodal features and produces global descriptors for fast retrieval. Beyond global retrieval, we design a training-free re-ranking mechanism that exploits VGGT&#x27;s cross-view keypoint-tracking capability. By combining mask-guided keypoint extraction with confidence-aware correspondence scoring, our proposed re-ranking mechanism effectively refines retrieval results without additional parameter optimization. Extensive experiments on large-scale autonomous driving benchmarks and our self-collected data demonstrate that VGGT-MPR achieves state-of-the-art performance, exhibiting strong robustness to severe environmental changes, viewpoint shifts, and occlusions. Our code and data will be made publicly available.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.19735">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.19735.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.19735.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Evaluating the Impact of Data Anonymization on Image Retrieval</span>
        <span class="paper-authors">Marvin Chen, Manuel Eberhardinger, Johannes Maucher</span>
        <span class="paper-meta">Updated 2026-02-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">With the growing importance of privacy regulations such as the General Data Protection Regulation, anonymizing visual data is becoming increasingly relevant across institutions. However, anonymization can negatively affect the performance of Computer Vision systems that rely on visual features, such as Content-Based Image Retrieval (CBIR). Despite this, the impact of anonymization on CBIR has not been systematically studied. This work addresses this gap, motivated by the DOKIQ project, an artificial intelligence-based system for document verification actively used by the State Criminal Police Office Baden-Württemberg. We propose a simple evaluation framework: retrieval results after anonymization should match those obtained before anonymization as closely as possible. To this end, we systematically assess the impact of anonymization using two public datasets and the internal DOKIQ dataset. Our experiments span three anonymization methods, four anonymization degrees, and four training strategies, all based on the state of the art backbone Self-Distillation with No Labels (DINO)v2. Our results reveal a pronounced retrieval bias in favor of models trained on original data, which produce the most similar retrievals after anonymization. The findings of this paper offer practical insights for developing privacy-compliant CBIR systems while preserving performance.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.19641">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.19641.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.19641.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Knowledge-aware Visual Question Generation for Remote Sensing Images</span>
        <span class="paper-authors">Siran Li, Li Mi, Javiera Castillo-Navarro, Devis Tuia</span>
        <span class="paper-meta">Updated 2026-02-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">With the rapid development of remote sensing image archives, asking questions about images has become an effective way of gathering specific information or performing image retrieval. However, automatically generated image-based questions tend to be simplistic and template-based, which hinders the real deployment of question answering or visual dialogue systems. To enrich and diversify the questions, we propose a knowledge-aware remote sensing visual question generation model, KRSVQG, that incorporates external knowledge related to the image content to improve the quality and contextual understanding of the generated questions. The model takes an image and a related knowledge triplet from external knowledge sources as inputs and leverages image captioning as an intermediary representation to enhance the image grounding of the generated questions. To assess the performance of KRSVQG, we utilized two datasets that we manually annotated: NWPU-300 and TextRS-300. Results on these two datasets demonstrate that KRSVQG outperforms existing methods and leads to knowledge-enriched questions, grounded in both image and domain knowledge.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.19224">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.19224.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.19224.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Questions beyond Pixels: Integrating Commonsense Knowledge in Visual Question Generation for Remote Sensing</span>
        <span class="paper-authors">Siran Li, Li Mi, Javiera Castillo-Navarro, Devis Tuia</span>
        <span class="paper-meta">Updated 2026-02-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">With the rapid development of remote sensing image archives, asking questions about images has become an effective way of gathering specific information or performing semantic image retrieval. However, current automatically generated questions tend to be simplistic and template-based, which hinders the deployment of question answering or visual dialogue systems for real-world applications. To enrich and diversify the questions with both image content and commonsense knowledge, we propose a Knowledge-aware Remote Sensing Visual Question Generation model (KRSVQG). The proposed model incorporates related knowledge triplets from external knowledge sources to broaden the question content, while employing image captioning as an intermediary representation to ground questions to the corresponding images. Moreover, KRSVQG utilizes a vision-language pre-training and fine-tuning strategy, enabling the model&#x27;s adaptation to low data regimes. To evaluate the proposed KRSVQG model, we construct two knowledge-aware remote sensing visual question generation datasets: the NWPU-300 dataset and the TextRS-300 dataset. Evaluations, including metrics and human assessment, demonstrate that KRSVQG outperforms existing methods and leads to rich questions, grounded in both image and domain knowledge. As a key practice in vision-language research, knowledge-aware visual question generation advances the understanding of image content beyond pixels, facilitating the development of knowledge-enriched vision-language systems with vision-grounded human commonsense.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.19217">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.19217.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.19217.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">IRIS-SLAM: Unified Geo-Instance Representations for Robust Semantic Localization and Mapping</span>
        <span class="paper-authors">Tingyang Xiao, Liu Liu, Wei Feng, Zhengyu Zou, Xiaolin Zhou, Wei Sui, Hao Li, Dingwen Zhang, Zhizhong Su</span>
        <span class="paper-meta">Updated 2026-02-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Geometry foundation models have significantly advanced dense geometric SLAM, yet existing systems often lack deep semantic understanding and robust loop closure capabilities. Meanwhile, contemporary semantic mapping approaches are frequently hindered by decoupled architectures and fragile data association. We propose IRIS-SLAM, a novel RGB semantic SLAM system that leverages unified geometric-instance representations derived from an instance-extended foundation model. By extending a geometry foundation model to concurrently predict dense geometry and cross-view consistent instance embeddings, we enable a semantic-synergized association mechanism and instance-guided loop closure detection. Our approach effectively utilizes viewpoint-agnostic semantic anchors to bridge the gap between geometric reconstruction and open-vocabulary mapping. Experimental results demonstrate that IRIS-SLAM significantly outperforms state-of-the-art methods, particularly in map consistency and wide-baseline loop closure reliability.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.18709">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.18709.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.18709.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">VQPP: Video Query Performance Prediction Benchmark</span>
        <span class="paper-authors">Adrian Catalin Lutu, Eduard Poesina, Radu Tudor Ionescu</span>
        <span class="paper-meta">Updated 2026-02-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Query performance prediction (QPP) is an important and actively studied information retrieval task, having various applications, such as query reformulation, query expansion, and retrieval system selection, among many others. The task has been primarily studied in the context of text and image retrieval, whereas QPP for content-based video retrieval (CBVR) remains largely underexplored. To this end, we propose the first benchmark for video query performance prediction (VQPP), comprising two text-to-video retrieval datasets and two CBVR systems, respectively. VQPP contains a total of 56K text queries and 51K videos, and comes with official training, validation and test splits, fostering direct comparisons and reproducible results. We explore multiple pre-retrieval and post-retrieval performance predictors, creating a representative benchmark for future exploration of QPP in the video domain. Our results show that pre-retrieval predictors obtain competitive performance, enabling applications before performing the retrieval step. We also demonstrate the applicability of VQPP by employing the best performing pre-retrieval predictor as reward model for training a large language model (LLM) on the query reformulation task via direct preference optimization (DPO). We release our benchmark and code at https://github.com/AdrianLutu/VQPP.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.17814">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.17814.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.17814.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DiffPlace: Street View Generation via Place-Controllable Diffusion Model Enhancing Place Recognition</span>
        <span class="paper-authors">Ji Li, Zhiwei Li, Shihao Li, Zhenjiang Yu, Boyang Wang, Haiou Liu</span>
        <span class="paper-meta">Updated 2026-02-12</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Generative models have advanced significantly in realistic image synthesis, with diffusion models excelling in quality and stability. Recent multi-view diffusion models improve 3D-aware street view generation, but they struggle to produce place-aware and background-consistent urban scenes from text, BEV maps, and object bounding boxes. This limits their effectiveness in generating realistic samples for place recognition tasks. To address these challenges, we propose DiffPlace, a novel framework that introduces a place-ID controller to enable place-controllable multi-view image generation. The place-ID controller employs linear projection, perceiver transformer, and contrastive learning to map place-ID embeddings into a fixed CLIP space, allowing the model to synthesize images with consistent background buildings while flexibly modifying foreground objects and weather conditions. Extensive experiments, including quantitative comparisons and augmented training evaluations, demonstrate that DiffPlace outperforms existing methods in both generation quality and training support for visual place recognition. Our results highlight the potential of generative models in enhancing scene-level and place-aware synthesis, providing a valuable approach for improving place recognition in autonomous driving</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.11875">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.11875.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.11875.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Arbitrary Ratio Feature Compression via Next Token Prediction</span>
        <span class="paper-authors">Yufan Liu, Daoyuan Ren, Zhipeng Zhang, Wenyang Luo, Bing Li, Weiming Hu, Stephen Maybank</span>
        <span class="paper-meta">Updated 2026-02-12</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Feature compression is increasingly important for improving the efficiency of downstream tasks, especially in applications involving large-scale or multi-modal data. While existing methods typically rely on dedicated models for achieving specific compression ratios, they are often limited in flexibility and generalization. In particular, retraining is necessary when adapting to a new compression ratio. To address this limitation, we propose a novel and flexible Arbitrary Ratio Feature Compression (ARFC) framework, which supports any compression ratio with a single model, eliminating the need for multiple specialized models. At its core, the Arbitrary Ratio Compressor (ARC) is an auto-regressive model that performs compression via next-token prediction. This allows the compression ratio to be controlled at inference simply by adjusting the number of generated tokens. To enhance the quality of the compressed features, two key modules are introduced. The Mixture of Solutions (MoS) module refines the compressed tokens by utilizing multiple compression results (solutions), reducing uncertainty and improving robustness. The Entity Relation Graph Constraint (ERGC) is integrated into the training process to preserve semantic and structural relationships during compression. Extensive experiments on cross-modal retrieval, image classification, and image retrieval tasks across multiple datasets demonstrate that our method consistently outperforms existing approaches at various compression ratios. Notably, in some cases, it even surpasses the performance of the original, uncompressed features. These results validate the effectiveness and versatility of ARFC for practical, resource-constrained scenarios.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.11494">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.11494.pdf">PDF</a>
          <a class="chip" href="https://github.com/muhammetdurmaz54/tst-tc2602-ufcpivj-114940">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.11494.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DeepImageSearch: Benchmarking Multimodal Agents for Context-Aware Image Retrieval in Visual Histories</span>
        <span class="paper-authors">Chenlong Deng, Mengjie Deng, Junjie Wu, Dun Zeng, Teng Wang, Qingsong Xie, Jiadeng Huang, Shengjie Ma, Changwang Zhang, Zhaoxiang Wang, Jun Wang, Yutao Zhu, Zhicheng Dou</span>
        <span class="paper-meta">Updated 2026-02-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Existing multimodal retrieval systems excel at semantic matching but implicitly assume that query-image relevance can be measured in isolation. This paradigm overlooks the rich dependencies inherent in realistic visual streams, where information is distributed across temporal sequences rather than confined to single snapshots. To bridge this gap, we introduce DeepImageSearch, a novel agentic paradigm that reformulates image retrieval as an autonomous exploration task. Models must plan and perform multi-step reasoning over raw visual histories to locate targets based on implicit contextual cues. We construct DISBench, a challenging benchmark built on interconnected visual data. To address the scalability challenge of creating context-dependent queries, we propose a human-model collaborative pipeline that employs vision-language models to mine latent spatiotemporal associations, effectively offloading intensive context discovery before human verification. Furthermore, we build a robust baseline using a modular agent framework equipped with fine-grained tools and a dual-memory system for long-horizon navigation. Extensive experiments demonstrate that DISBench poses significant challenges to state-of-the-art models, highlighting the necessity of incorporating agentic reasoning into next-generation retrieval systems.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.10809">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.10809.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.10809.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">WristMIR: Coarse-to-Fine Region-Aware Retrieval of Pediatric Wrist Radiographs with Radiology Report-Driven Learning</span>
        <span class="paper-authors">Mert Sonmezer, Serge Vasylechko, Duygu Atasoy, Seyda Ertekin, Sila Kurugol</span>
        <span class="paper-meta">Updated 2026-02-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Retrieving wrist radiographs with analogous fracture patterns is challenging because clinically important cues are subtle, highly localized and often obscured by overlapping anatomy or variable imaging views. Progress is further limited by the scarcity of large, well-annotated datasets for case-based medical image retrieval. We introduce WristMIR, a region-aware pediatric wrist radiograph retrieval framework that leverages dense radiology reports and bone-specific localization to learn fine-grained, clinically meaningful image representations without any manual image-level annotations. Using MedGemma-based structured report mining to generate both global and region-level captions, together with pre-processed wrist images and bone-specific crops of the distal radius, distal ulna, and ulnar styloid, WristMIR jointly trains global and local contrastive encoders and performs a two-stage retrieval process: (1) coarse global matching to identify candidate exams, followed by (2) region-conditioned reranking aligned to a predefined anatomical bone region. WristMIR improves retrieval performance over strong vision-language baselines, raising image-to-text Recall@5 from 0.82% to 9.35%. Its embeddings also yield stronger fracture classification (AUROC 0.949, AUPRC 0.953). In region-aware evaluation, the two-stage design markedly improves retrieval-based fracture diagnosis, increasing mean $F_1$ from 0.568 to 0.753, and radiologists rate its retrieved cases as more clinically relevant, with mean scores rising from 3.36 to 4.35. These findings highlight the potential of anatomically guided retrieval to enhance diagnostic reasoning and support clinical decision-making in pediatric musculoskeletal imaging. The source code is publicly available at https://github.com/quin-med-harvard-edu/WristMIR.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.07872">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.07872.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.07872.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">OSCAR: Optimization-Steered Agentic Planning for Composed Image Retrieval</span>
        <span class="paper-authors">Teng Wang, Rong Shan, Jianghao Lin, Junjie Wu, Tianyi Xu, Jianping Zhang, Wenteng Chen, Changwang Zhang, Zhaoxiang Wang, Weinan Zhang, Jun Wang</span>
        <span class="paper-meta">Updated 2026-02-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Composed image retrieval (CIR) requires complex reasoning over heterogeneous visual and textual constraints. Existing approaches largely fall into two paradigms: unified embedding retrieval, which suffers from single-model myopia, and heuristic agentic retrieval, which is limited by suboptimal, trial-and-error orchestration. To this end, we propose OSCAR, an optimization-steered agentic planning framework for composed image retrieval. We are the first to reformulate agentic CIR from a heuristic search process into a principled trajectory optimization problem. Instead of relying on heuristic trial-and-error exploration, OSCAR employs a novel offline-online paradigm. In the offline phase, we model CIR via atomic retrieval selection and composition as a two-stage mixed-integer programming problem, mathematically deriving optimal trajectories that maximize ground-truth coverage for training samples via rigorous boolean set operations. These trajectories are then stored in a golden library to serve as in-context demonstrations for online steering of VLM planner at online inference time. Extensive experiments on three public benchmarks and a private industrial benchmark show that OSCAR consistently outperforms SOTA baselines. Notably, it achieves superior performance using only 10% of training data, demonstrating strong generalization of planning logic rather than dataset-specific memorization.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.08603">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.08603.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.08603.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A Sketch+Text Composed Image Retrieval Dataset for Thangka</span>
        <span class="paper-authors">Jinyu Xu, Yi Sun, Jiangling Zhang, Qing Xie, Daomin Ji, Zhifeng Bao, Jiachen Li, Yanchun Ma, Yongjian Liu</span>
        <span class="paper-meta">Updated 2026-02-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Composed Image Retrieval (CIR) enables image retrieval by combining multiple query modalities, but existing benchmarks predominantly focus on general-domain imagery and rely on reference images with short textual modifications. As a result, they provide limited support for retrieval scenarios that require fine-grained semantic reasoning, structured visual understanding, and domain-specific knowledge. In this work, we introduce CIRThan, a sketch+text Composed Image Retrieval dataset for Thangka imagery, a culturally grounded and knowledge-specific visual domain characterized by complex structures, dense symbolic elements, and domain-dependent semantic conventions. CIRThan contains 2,287 high-quality Thangka images, each paired with a human-drawn sketch and hierarchical textual descriptions at three semantic levels, enabling composed queries that jointly express structural intent and multi-level semantic specification. We provide standardized data splits, comprehensive dataset analysis, and benchmark evaluations of representative supervised and zero-shot CIR methods. Experimental results reveal that existing CIR approaches, largely developed for general-domain imagery, struggle to effectively align sketch-based abstractions and hierarchical textual semantics with fine-grained Thangka images, particularly without in-domain supervision. We believe CIRThan offers a valuable benchmark for advancing sketch+text CIR, hierarchical semantic modeling, and multimodal retrieval in cultural heritage and other knowledge-specific visual domains. The dataset is publicly available at https://github.com/jinyuxu-whut/CIRThan.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.08411">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.08411.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.08411.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">UrbanGraphEmbeddings: Learning and Evaluating Spatially Grounded Multimodal Embeddings for Urban Science</span>
        <span class="paper-authors">Jie Zhang, Xingtong Yu, Yuan Fang, Rudi Stouffs, Zdravko Trivic</span>
        <span class="paper-meta">Updated 2026-02-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Learning transferable multimodal embeddings for urban environments is challenging because urban understanding is inherently spatial, yet existing datasets and benchmarks lack explicit alignment between street-view images and urban structure. We introduce UGData, a spatially grounded dataset that anchors street-view images to structured spatial graphs and provides graph-aligned supervision via spatial reasoning paths and spatial context captions, exposing distance, directionality, connectivity, and neighborhood context beyond image content. Building on UGData, we propose UGE, a two-stage training strategy that progressively and stably aligns images, text, and spatial structures by combining instruction-guided contrastive learning with graph-based spatial encoding. We finally introduce UGBench, a comprehensive benchmark to evaluate how spatially grounded embeddings support diverse urban understanding tasks -- including geolocation ranking, image retrieval, urban perception, and spatial grounding. We develop UGE on multiple state-of-the-art VLM backbones, including Qwen2-VL, Qwen2.5-VL, Phi-3-Vision, and LLaVA1.6-Mistral, and train fixed-dimensional spatial embeddings with LoRA tuning. UGE built upon Qwen2.5-VL-7B backbone achieves up to 44% improvement in image retrieval and 30% in geolocation ranking on training cities, and over 30% and 22% gains respectively on held-out cities, demonstrating the effectiveness of explicit spatial grounding for spatially intensive urban tasks.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.08342">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.08342.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.08342.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SDR-CIR: Semantic Debias Retrieval Framework for Training-Free Zero-Shot Composed Image Retrieval</span>
        <span class="paper-authors">Yi Sun, Jinyu Xu, Qing Xie, Jiachen Li, Yanchun Ma, Yongjian Liu</span>
        <span class="paper-meta">Updated 2026-02-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Composed Image Retrieval (CIR) aims to retrieve a target image from a query composed of a reference image and modification text. Recent training-free zero-shot methods often employ Multimodal Large Language Models (MLLMs) with Chain-of-Thought (CoT) to compose a target image description for retrieval. However, due to the fuzzy matching nature of ZS-CIR, the generated description is prone to semantic bias relative to the target image. We propose SDR-CIR, a training-free Semantic Debias Ranking method based on CoT reasoning. First, Selective CoT guides the MLLM to extract visual content relevant to the modification text during image understanding, thereby reducing visual noise at the source. We then introduce a Semantic Debias Ranking with two steps, Anchor and Debias, to mitigate semantic bias. In the Anchor step, we fuse reference image features with target description features to reinforce useful semantics and supplement omitted cues. In the Debias step, we explicitly model the visual semantic contribution of the reference image to the description and incorporate it into the similarity score as a penalty term. By supplementing omitted cues while suppressing redundancy, SDR-CIR mitigates semantic bias and improves retrieval performance. Experiments on three standard CIR benchmarks show that SDR-CIR achieves state-of-the-art results among one-stage methods while maintaining high efficiency. The code is publicly available at https://github.com/suny105/SDR-CIR.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.04451">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.04451.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.04451.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SAR-RAG: ATR Visual Question Answering by Semantic Search, Retrieval, and MLLM Generation</span>
        <span class="paper-authors">David F. Ramirez, Tim Overman, Kristen Jaskie, Joe Marvin, Andreas Spanias</span>
        <span class="paper-meta">Updated 2026-02-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We present a visual-context image retrieval-augmented generation (ImageRAG) assisted AI agent for automatic target recognition (ATR) of synthetic aperture radar (SAR). SAR is a remote sensing method used in defense and security applications to detect and monitor the positions of military vehicles, which may appear indistinguishable in images. Researchers have extensively studied SAR ATR to improve the differentiation and identification of vehicle types, characteristics, and measurements. Test examples can be compared with known vehicle target types to improve recognition tasks. New methods enhance the capabilities of neural networks, transformer attention, and multimodal large language models. An agentic AI method may be developed to utilize a defined set of tools, such as searching through a library of similar examples. Our proposed method, SAR Retrieval-Augmented Generation (SAR-RAG), combines a multimodal large language model (MLLM) with a vector database of semantic embeddings to support contextual search for image exemplars with known qualities. By recovering past image examples with known true target types, our SAR-RAG system can compare similar vehicle categories, achieving improved ATR prediction accuracy. We evaluate this through search and retrieval metrics, categorical classification accuracy, and numeric regression of vehicle dimensions. These metrics all show improvements when SAR-RAG is added to an MLLM baseline method as an attached ATR memory bank.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.04712">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.04712.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.04712.pdf">
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
        <span class="paper-title">Beyond Static Cropping: Layer-Adaptive Visual Localization and Decoding Enhancement</span>
        <span class="paper-authors">Zipeng Zhu, Zhanghao Hu, Qinglin Zhu, Yuxi Hong, Yijun Liu, Jingyong Su, Yulan He, Lin Gui</span>
        <span class="paper-meta">Updated 2026-02-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Large Vision-Language Models (LVLMs) have advanced rapidly by aligning visual patches with the text embedding space, but a fixed visual-token budget forces images to be resized to a uniform pretraining resolution, often erasing fine-grained details and causing hallucinations via over-reliance on language priors. Recent attention-guided enhancement (e.g., cropping or region-focused attention allocation) alleviates this, yet it commonly hinges on a static &quot;magic layer&quot; empirically chosen on simple recognition benchmarks and thus may not transfer to complex reasoning tasks. In contrast to this static assumption, we propose a dynamic perspective on visual grounding. Through a layer-wise sensitivity analysis, we demonstrate that visual grounding is a dynamic process: while simple object recognition tasks rely on middle layers, complex visual search and reasoning tasks require visual information to be reactivated at deeper layers. Based on this observation, we introduce Visual Activation by Query (VAQ), a metric that identifies the layer whose attention map is most relevant to query-specific visual grounding by measuring attention sensitivity to the input query. Building on VAQ, we further propose LASER (Layer-adaptive Attention-guided Selective visual and decoding Enhancement for Reasoning), a training-free inference procedure that adaptively selects task-appropriate layers for visual localization and question answering. Experiments across diverse VQA benchmarks show that LASER significantly improves VQA accuracy across tasks with varying levels of complexity.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.04304">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.04304.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.04304.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Invariance on Manifolds: Understanding Robust Visual Representations for Place Recognition</span>
        <span class="paper-authors">Jintao Cheng, Weibin Li, Zhijian He, Jin Wu, Chi Man Vong, Wei Zhang</span>
        <span class="paper-meta">Updated 2026-02-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Visual Place Recognition (VPR) demands representations robust to drastic environmental and viewpoint shifts. Current aggregation paradigms, however, either rely on data-hungry supervision or simplistic first-order statistics, often neglecting intrinsic structural correlations. In this work, we propose a Second-Order Geometric Statistics framework that inherently captures geometric stability without training. We conceptualize scenes as covariance descriptors on the Symmetric Positive Definite (SPD) manifold, where perturbations manifest as tractable congruence transformations. By leveraging geometry-aware Riemannian mappings, we project these descriptors into a linearized Euclidean embedding, effectively decoupling signal structure from noise. Our approach introduces a training-free framework built upon fixed, pre-trained backbones, achieving strong zero-shot generalization without parameter updates. Extensive experiments confirm that our method achieves highly competitive performance against state-of-the-art baselines, particularly excelling in challenging zero-shot scenarios.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.00841">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.00841.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.00841.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LaVPR: Benchmarking Language and Vision for Place Recognition</span>
        <span class="paper-authors">Ofer Idan, Dan Badur, Yosi Keller, Yoli Shavit</span>
        <span class="paper-meta">Updated 2026-02-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Visual Place Recognition (VPR) often fails under extreme environmental changes and perceptual aliasing. Furthermore, standard systems cannot perform &quot;blind&quot; localization from verbal descriptions alone, a capability needed for applications such as emergency response. To address these challenges, we introduce LaVPR, a large-scale benchmark that extends existing VPR datasets with over 650,000 rich natural-language descriptions. Using LaVPR, we investigate two paradigms: Multi-Modal Fusion for enhanced robustness and Cross-Modal Retrieval for language-based localization. Our results show that language descriptions yield consistent gains in visually degraded conditions, with the most significant impact on smaller backbones. Notably, adding language allows compact models to rival the performance of much larger vision-only architectures. For cross-modal retrieval, we establish a baseline using Low-Rank Adaptation (LoRA) and Multi-Similarity loss, which substantially outperforms standard contrastive methods across vision-language models. Ultimately, LaVPR enables a new class of localization systems that are both resilient to real-world stochasticity and practical for resource-constrained deployment. Our dataset and code are available at https://github.com/oferidan1/LaVPR.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.03253">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.03253.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.03253.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ObjEmbed: Towards Universal Multimodal Object Embeddings</span>
        <span class="paper-authors">Shenghao Fu, Yukun Su, Fengyun Rao, Jing Lyu, Xiaohua Xie, Wei-Shi Zheng</span>
        <span class="paper-meta">Updated 2026-02-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Aligning objects with corresponding textual descriptions is a fundamental challenge and a realistic requirement in vision-language understanding. While recent multimodal embedding models excel at global image-text alignment, they often struggle with fine-grained alignment between image regions and specific phrases. In this work, we present ObjEmbed, a novel MLLM embedding model that decomposes the input image into multiple regional embeddings, each corresponding to an individual object, along with global embeddings. It supports a wide range of visual understanding tasks like visual grounding, local image retrieval, and global image retrieval. ObjEmbed enjoys three key properties: (1) Object-Oriented Representation: It captures both semantic and spatial aspects of objects by generating two complementary embeddings for each region: an object embedding for semantic matching and an IoU embedding that predicts localization quality. The final object matching score combines semantic similarity with the predicted IoU, enabling more accurate retrieval. (2) Versatility: It seamlessly handles both region-level and image-level tasks. (3) Efficient Encoding: All objects in an image, along with the full image, are encoded in a single forward pass for high efficiency. Superior performance on 18 diverse benchmarks demonstrates its strong semantic discrimination.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.01753">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.01753.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.01753.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Real-Time Loop Closure Detection in Visual SLAM via NetVLAD and Faiss</span>
        <span class="paper-authors">Enguang Fan</span>
        <span class="paper-meta">Updated 2026-02-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Loop closure detection (LCD) is a core component of simultaneous localization and mapping (SLAM): it identifies revisited places and enables pose-graph constraints that correct accumulated drift. Classic bag-of-words approaches such as DBoW are efficient but often degrade under appearance change and perceptual aliasing. In parallel, deep learning-based visual place recognition (VPR) descriptors (e.g., NetVLAD and Transformer-based models) offer stronger robustness, but their computational cost is often viewed as a barrier to real-time SLAM. In this paper, we empirically evaluate NetVLAD as an LCD module and compare it against DBoW on the KITTI dataset. We introduce a Fine-Grained Top-K precision-recall curve that better reflects LCD settings where a query may have zero or multiple valid matches. With Faiss-accelerated nearestneighbor search, NetVLAD achieves real-time query speed while improving accuracy and robustness over DBoW, making it a practical drop-in alternative for LCD in SLAM.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.01673">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.01673.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.01673.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ReCALL: Recalibrating Capability Degradation for MLLM-based Composed Image Retrieval</span>
        <span class="paper-authors">Tianyu Yang, ChenWei He, Xiangzhao Hao, Tianyue Wang, Jiarui Guo, Haiyun Guo, Leigang Qu, Jinqiao Wang, Tat-Seng Chua</span>
        <span class="paper-meta">Updated 2026-02-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Composed Image Retrieval (CIR) aims to retrieve target images based on a hybrid query comprising a reference image and a modification text. Early dual-tower Vision-Language Models (VLMs) struggle with cross-modality compositional reasoning required for this task. Recently, adapting generative Multimodal Large Language Models (MLLMs) for retrieval offers a promising direction. However, we identify that this adaptation strategy overlooks a fundamental issue: adapting a generative MLLM into a single-embedding discriminative retriever triggers a paradigm conflict, which leads to Capability Degradation - the deterioration of native fine-grained reasoning after retrieval adaptation. To address this challenge, we propose ReCALL (Recalibrating Capability Degradation), a model-agnostic framework that follows a diagnose-generate-refine pipeline: Firstly, we diagnose cognitive blind spots of the retriever via self-guided informative instance mining. Next, we generate corrective instructions and triplets by CoT prompting the foundation MLLM and conduct quality control with VQA-based consistency filtering. Finally, we refine the retriever through continual training on these triplets with a grouped contrastive scheme, thereby internalizing fine-grained visual-semantic distinctions and realigning the discriminative embedding space of retriever with intrinsic compositional reasoning within the MLLM. Extensive experiments on CIRR and FashionIQ show that ReCALL consistently recalibrates degraded capabilities and achieves state-of-the-art performance. Code will be released soon.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.01639">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.01639.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.01639.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Interacted Planes Reveal 3D Line Mapping</span>
        <span class="paper-authors">Zeran Ke, Bin Tan, Gui-Song Xia, Yujun Shen, Nan Xue</span>
        <span class="paper-meta">Updated 2026-02-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">3D line mapping from multi-view RGB images provides a compact and structured visual representation of scenes. We study the problem from a physical and topological perspective: a 3D line most naturally emerges as the edge of a finite 3D planar patch. We present LiP-Map, a line-plane joint optimization framework that explicitly models learnable line and planar primitives. This coupling enables accurate and detailed 3D line mapping while maintaining strong efficiency (typically completing a reconstruction in 3 to 5 minutes per scene). LiP-Map pioneers the integration of planar topology into 3D line mapping, not by imposing pairwise coplanarity constraints but by explicitly constructing interactions between plane and line primitives, thus offering a principled route toward structured reconstruction in man-made environments. On more than 100 scenes from ScanNetV2, ScanNet++, Hypersim, 7Scenes, and Tanks\&amp;Temple, LiP-Map improves both accuracy and completeness over state-of-the-art methods. Beyond line mapping quality, LiP-Map significantly advances line-assisted visual localization, establishing strong performance on 7Scenes. Our code is released at https://github.com/calmke/LiPMAP for reproducible research.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.01296">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.01296.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.01296.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Variance &amp; Greediness: A comparative study of metric-learning losses</span>
        <span class="paper-authors">Donghuo Zeng, Hao Niu, Zhi Li, Masato Taya</span>
        <span class="paper-meta">Updated 2026-01-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Metric learning is central to retrieval, yet its effects on embedding geometry and optimization dynamics are not well understood. We introduce a diagnostic framework, VARIANCE (intra-/inter-class variance) and GREEDINESS (active ratio and gradient norms), to compare seven representative losses, i.e., Contrastive, Triplet, N-pair, InfoNCE, ArcFace, SCL, and CCL, across five image-retrieval datasets. Our analysis reveals that Triplet and SCL preserve higher within-class variance and clearer inter-class margins, leading to stronger top-1 retrieval in fine-grained settings. In contrast, Contrastive and InfoNCE compact embeddings are achieved quickly through many small updates, accelerating convergence but potentially oversimplifying class structures. N-pair achieves a large mean separation but with uneven spacing. These insights reveal a form of efficiency-granularity trade-off and provide practical guidance: prefer Triplet/SCL when diversity preservation and hard-sample discrimination are critical, and Contrastive/InfoNCE when faster embedding compaction is desired.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.21450">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.21450.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.21450.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">When Vision Meets Texts in Listwise Reranking</span>
        <span class="paper-authors">Hongyi Cai</span>
        <span class="paper-meta">Updated 2026-01-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Recent advancements in information retrieval have highlighted the potential of integrating visual and textual information, yet effective reranking for image-text documents remains challenging due to the modality gap and scarcity of aligned datasets. Meanwhile, existing approaches often rely on large models (7B to 32B parameters) with reasoning-based distillation, incurring unnecessary computational overhead while primarily focusing on textual modalities. In this paper, we propose Rank-Nexus, a multimodal image-text document reranker that performs listwise qualitative reranking on retrieved lists incorporating both images and texts. To bridge the modality gap, we introduce a progressive cross-modal training strategy. We first train modalities separately: leveraging abundant text reranking data, we distill knowledge into the text branch. For images, where data is scarce, we construct distilled pairs from multimodal large language model (MLLM) captions on image retrieval benchmarks. Subsequently, we distill a joint image-text reranking dataset. Rank-Nexus achieves outstanding performance on text reranking benchmarks (TREC, BEIR) and the challenging image reranking benchmark (INQUIRE, MMDocIR), using only a lightweight 2B pretrained visual-language model. This efficient design ensures strong generalization across diverse multimodal scenarios without excessive parameters or reasoning overhead.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.20623">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.20623.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.20623.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Eliminating Hallucination in Diffusion-Augmented Interactive Text-to-Image Retrieval</span>
        <span class="paper-authors">Zhuocheng Zhang, Kangheng Liang, Guanxuan Li, Paul Henderson, Richard Mccreadie, Zijun Long</span>
        <span class="paper-meta">Updated 2026-01-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Diffusion-Augmented Interactive Text-to-Image Retrieval (DAI-TIR) is a promising paradigm that improves retrieval performance by generating query images via diffusion models and using them as additional ``views&#x27;&#x27; of the user&#x27;s intent. However, these generative views can be incorrect because diffusion generation may introduce hallucinated visual cues that conflict with the original query text. Indeed, we empirically demonstrate that these hallucinated cues can substantially degrade DAI-TIR performance. To address this, we propose Diffusion-aware Multi-view Contrastive Learning (DMCL), a hallucination-robust training framework that casts DAI-TIR as joint optimization over representations of query intent and the target image. DMCL introduces semantic-consistency and diffusion-aware contrastive objectives to align textual and diffusion-generated query views while suppressing hallucinated query signals. This yields an encoder that acts as a semantic filter, effectively mapping hallucinated cues into a null space, improving robustness to spurious cues and better representing the user&#x27;s intent. Attention visualization and geometric embedding-space analyses corroborate this filtering behavior. Across five standard benchmarks, DMCL delivers consistent improvements in multi-round Hits@10, reaching as high as 7.37\% over prior fine-tuned and zero-shot baselines, which indicates it is a general and robust training framework for DAI-TIR.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.20391">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.20391.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.20391.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">VGGT-SLAM 2.0: Real time Dense Feed-forward Scene Reconstruction</span>
        <span class="paper-authors">Dominic Maggio, Luca Carlone</span>
        <span class="paper-meta">Updated 2026-01-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We present VGGT-SLAM 2.0, a real time RGB feed-forward SLAM system which substantially improves upon VGGT-SLAM for incrementally aligning submaps created from VGGT. Firstly, we remove high-dimensional 15-degree-of-freedom drift and planar degeneracy from VGGT-SLAM by creating a new factor graph design while still addressing the reconstruction ambiguity of VGGT given unknown camera intrinsics. Secondly, by studying the attention layers of VGGT, we show that one of the layers is well suited to assist in image retrieval verification for free without additional training, which enables both rejecting false positive matches and allows for completing more loop closures. Finally, we conduct a suite of experiments which includes showing VGGT-SLAM 2.0 can easily be adapted for open-set object detection and demonstrating real time performance while running online onboard a ground robot using a Jetson Thor. We also test in environments ranging from cluttered indoor apartments and office scenes to a 4,200 square foot barn, and we also demonstrate VGGT-SLAM 2.0 achieves the highest accuracy on the TUM dataset with about 23 percent less pose error than VGGT-SLAM. Code will be released upon publication.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.19887">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.19887.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.19887.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Pixel-Grounded Retrieval for Knowledgeable Large Multimodal Models</span>
        <span class="paper-authors">Jeonghwan Kim, Renjie Tao, Sanat Sharma, Jiaqi Wang, Kai Sun, Zhaojiang Lin, Seungwhan Moon, Lambert Mathias, Anuj Kumar, Heng Ji, Xin Luna Dong</span>
        <span class="paper-meta">Updated 2026-01-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Visual Question Answering (VQA) often requires coupling fine-grained perception with factual knowledge beyond the input image. Prior multimodal Retrieval-Augmented Generation (MM-RAG) systems improve factual grounding but lack an internal policy for when and how to retrieve. We propose PixSearch, the first end-to-end Segmenting Large Multimodal Model (LMM) that unifies region-level perception and retrieval-augmented reasoning. During encoding, PixSearch emits &lt;search&gt; tokens to trigger retrieval, selects query modalities (text, image, or region), and generates pixel-level masks that directly serve as visual queries, eliminating the reliance on modular pipelines (detectors, segmenters, captioners, etc.). A two-stage supervised fine-tuning regimen with search-interleaved supervision teaches retrieval timing and query selection while preserving segmentation ability. On egocentric and entity-centric VQA benchmarks, PixSearch substantially improves factual consistency and generalization, yielding a 19.7% relative gain in accuracy on CRAG-MM compared to whole image retrieval, while retaining competitive reasoning performance on various VQA and text-only QA tasks.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.19060">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.19060.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.19060.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">X-Aligner: Composed Visual Retrieval without the Bells and Whistles</span>
        <span class="paper-authors">Yuqian Zheng, Mariana-Iuliana Georgescu</span>
        <span class="paper-meta">Updated 2026-01-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Composed Video Retrieval (CoVR) facilitates video retrieval by combining visual and textual queries. However, existing CoVR frameworks typically fuse multimodal inputs in a single stage, achieving only marginal gains over initial baseline. To address this, we propose a novel CoVR framework that leverages the representational power of Vision Language Models (VLMs). Our framework incorporates a novel cross-attention module X-Aligner, composed of cross-attention layers that progressively fuse visual and textual inputs and align their multimodal representation with that of the target video. To further enhance the representation of the multimodal query, we incorporate the caption of the visual query as an additional input. The framework is trained in two stages to preserve the pretrained VLM representation. In the first stage, only the newly introduced module is trained, while in the second stage, the textual query encoder is also fine-tuned. We implement our framework on top of BLIP-family architecture, namely BLIP and BLIP-2, and train it on the Webvid-CoVR data set. In addition to in-domain evaluation on Webvid-CoVR-Test, we perform zero-shot evaluations on the Composed Image Retrieval (CIR) data sets CIRCO and Fashion-IQ. Our framework achieves state-of-the-art performance on CoVR obtaining a Recall@1 of 63.93% on Webvid-CoVR-Test, and demonstrates strong zero-shot generalization on CIR tasks.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.16582">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.16582.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.16582.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Rethinking Composed Image Retrieval Evaluation: A Fine-Grained Benchmark from Image Editing</span>
        <span class="paper-authors">Tingyu Song, Yanzhao Zhang, Mingxin Li, Zhuoning Guo, Dingkun Long, Pengjun Xie, Siyue Zhang, Yilun Zhao, Shu Wu</span>
        <span class="paper-meta">Updated 2026-01-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Composed Image Retrieval (CIR) is a pivotal and complex task in multimodal understanding. Current CIR benchmarks typically feature limited query categories and fail to capture the diverse requirements of real-world scenarios. To bridge this evaluation gap, we leverage image editing to achieve precise control over modification types and content, enabling a pipeline for synthesizing queries across a broad spectrum of categories. Using this pipeline, we construct EDIR, a novel fine-grained CIR benchmark. EDIR encompasses 5,000 high-quality queries structured across five main categories and fifteen subcategories. Our comprehensive evaluation of 13 multimodal embedding models reveals a significant capability gap; even state-of-the-art models (e.g., RzenEmbed and GME) struggle to perform consistently across all subcategories, highlighting the rigorous nature of our benchmark. Through comparative analysis, we further uncover inherent limitations in existing benchmarks, such as modality biases and insufficient categorical coverage. Furthermore, an in-domain training experiment demonstrates the feasibility of our benchmark. This experiment clarifies the task challenges by distinguishing between categories that are solvable with targeted data and those that expose intrinsic limitations of current model architectures.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.16125">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.16125.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.16125.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Heterogeneous Uncertainty-Guided Composed Image Retrieval with Fine-Grained Probabilistic Learning</span>
        <span class="paper-authors">Haomiao Tang, Jinpeng Wang, Minyi Zhao, Guanghao Meng, Ruisheng Luo, Long Chen, Shu-Tao Xia</span>
        <span class="paper-meta">Updated 2026-01-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Composed Image Retrieval (CIR) enables image search by combining a reference image with modification text. Intrinsic noise in CIR triplets incurs intrinsic uncertainty and threatens the model&#x27;s robustness. Probabilistic learning approaches have shown promise in addressing such issues; however, they fall short for CIR due to their instance-level holistic modeling and homogeneous treatment of queries and targets. This paper introduces a Heterogeneous Uncertainty-Guided (HUG) paradigm to overcome these limitations. HUG utilizes a fine-grained probabilistic learning framework, where queries and targets are represented by Gaussian embeddings that capture detailed concepts and uncertainties. We customize heterogeneous uncertainty estimations for multi-modal queries and uni-modal targets. Given a query, we capture uncertainties not only regarding uni-modal content quality but also multi-modal coordination, followed by a provable dynamic weighting mechanism to derive comprehensive query uncertainty. We further design uncertainty-guided objectives, including query-target holistic contrast and fine-grained contrasts with comprehensive negative sampling strategies, which effectively enhance discriminative learning. Experiments on benchmarks demonstrate HUG&#x27;s effectiveness beyond state-of-the-art baselines, with faithful analysis justifying the technical contributions.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.11393">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.11393.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.11393.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Unified Multimodal and Multilingual Retrieval via Multi-Task Learning with NLU Integration</span>
        <span class="paper-authors">Xinyuan Zhang, Lina Zhang, Lisung Chen, Guangyao Liu, Shuai Nie, Jiaming Xu, Runyu Shi, Ying Huang, Guoquan Zhang</span>
        <span class="paper-meta">Updated 2026-01-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Multimodal retrieval systems typically employ Vision Language Models (VLMs) that encode images and text independently into vectors within a shared embedding space. Despite incorporating text encoders, VLMs consistently underperform specialized text models on text-only retrieval tasks. Moreover, introducing additional text encoders increases storage, inference overhead, and exacerbates retrieval inefficiencies, especially in multilingual settings. To address these limitations, we propose a multi-task learning framework that unifies the feature representation across images, long and short texts, and intent-rich queries. To our knowledge, this is the first work to jointly optimize multilingual image retrieval, text retrieval, and natural language understanding (NLU) tasks within a single framework. Our approach integrates image and text retrieval with a shared text encoder that is enhanced by NLU features for intent understanding and retrieval accuracy.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.14714">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.14714.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.14714.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LookBench: A Live and Holistic Open Benchmark for Fashion Image Retrieval</span>
        <span class="paper-authors">Chao Gao, Siqiao Xue, Yimin Peng, Jiwen Fu, Tingyi Gu, Shanshan Li, Fan Zhou</span>
        <span class="paper-meta">Updated 2026-01-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">In this paper, we present LookBench (We use the term &quot;look&quot; to reflect retrieval that mirrors how people shop -- finding the exact item, a close substitute, or a visually consistent alternative.), a live, holistic and challenging benchmark for fashion image retrieval in real e-commerce settings. LookBench includes both recent product images sourced from live websites and AI-generated fashion images, reflecting contemporary trends and use cases. Each test sample is time-stamped and we intend to update the benchmark periodically, enabling contamination-aware evaluation aligned with declared training cutoffs. Grounded in our fine-grained attribute taxonomy, LookBench covers single-item and outfit-level retrieval across. Our experiments reveal that LookBench poses a significant challenge on strong baselines, with many models achieving below $60\%$ Recall@1. Our proprietary model achieves the best performance on LookBench, and we release an open-source counterpart that ranks second, with both models attaining state-of-the-art results on legacy Fashion200K evaluations. LookBench is designed to be updated semi-annually with new test samples and progressively harder task variants, providing a durable measure of progress. We publicly release our leaderboard, dataset, evaluation code, and trained models.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.14706">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.14706.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.14706.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">XR: Cross-Modal Agents for Composed Image Retrieval</span>
        <span class="paper-authors">Zhongyu Yang, Wei Pang, Yingfang Yuan</span>
        <span class="paper-meta">Updated 2026-01-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Retrieval is being redefined by agentic AI, demanding multimodal reasoning beyond conventional similarity-based paradigms. Composed Image Retrieval (CIR) exemplifies this shift as each query combines a reference image with textual modifications, requiring compositional understanding across modalities. While embedding-based CIR methods have achieved progress, they remain narrow in perspective, capturing limited cross-modal cues and lacking semantic reasoning. To address these limitations, we introduce XR, a training-free multi-agent framework that reframes retrieval as a progressively coordinated reasoning process. It orchestrates three specialized types of agents: imagination agents synthesize target representations through cross-modal generation, similarity agents perform coarse filtering via hybrid matching, and question agents verify factual consistency through targeted reasoning for fine filtering. Through progressive multi-agent coordination, XR iteratively refines retrieval to meet both semantic and visual query constraints, achieving up to a 38% gain over strong training-free and training-based baselines on FashionIQ, CIRR, and CIRCO, while ablations show each agent is essential. Code is available: https://01yzzyu.github.io/xr.github.io/.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.14245">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.14245.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.14245.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Fine-Grained Zero-Shot Composed Image Retrieval with Complementary Visual-Semantic Integration</span>
        <span class="paper-authors">Yongcong Ye, Kai Zhang, Yanghai Zhang, Enhong Chen, Longfei Li, Jun Zhou</span>
        <span class="paper-meta">Updated 2026-01-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Zero-shot composed image retrieval (ZS-CIR) is a rapidly growing area with significant practical applications, allowing users to retrieve a target image by providing a reference image and a relative caption describing the desired modifications. Existing ZS-CIR methods often struggle to capture fine-grained changes and integrate visual and semantic information effectively. They primarily rely on either transforming the multimodal query into a single text using image-to-text models or employing large language models for target image description generation, approaches that often fail to capture complementary visual information and complete semantic context. To address these limitations, we propose a novel Fine-Grained Zero-Shot Composed Image Retrieval method with Complementary Visual-Semantic Integration (CVSI). Specifically, CVSI leverages three key components: (1) Visual Information Extraction, which not only extracts global image features but also uses a pre-trained mapping network to convert the image into a pseudo token, combining it with the modification text and the objects most likely to be added. (2) Semantic Information Extraction, which involves using a pre-trained captioning model to generate multiple captions for the reference image, followed by leveraging an LLM to generate the modified captions and the objects most likely to be added. (3) Complementary Information Retrieval, which integrates information extracted from both the query and database images to retrieve the target image, enabling the system to efficiently handle retrieval queries in a variety of situations. Extensive experiments on three public datasets (e.g., CIRR, CIRCO, and FashionIQ) demonstrate that CVSI significantly outperforms existing state-of-the-art methods. Our code is available at https://github.com/yyc6631/CVSI.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.14060">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.14060.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.14060.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Glance-or-Gaze: Incentivizing LMMs to Adaptively Focus Search via Reinforcement Learning</span>
        <span class="paper-authors">Hongbo Bai, Yujin Zhou, Yile Wu, Chi-Min Chan, Pengcheng Wen, Kunhao Pan, Sirui Han, Yike Guo</span>
        <span class="paper-meta">Updated 2026-01-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Large Multimodal Models (LMMs) have achieved remarkable success in visual understanding, yet they struggle with knowledge-intensive queries involving long-tail entities or evolving information due to static parametric knowledge. Recent search-augmented approaches attempt to address this limitation, but existing methods rely on indiscriminate whole-image retrieval that introduces substantial visual redundancy and noise, and lack deep iterative reflection, limiting their effectiveness on complex visual queries. To overcome these challenges, we propose Glance-or-Gaze (GoG), a fully autonomous framework that shifts from passive perception to active visual planning. GoG introduces a Selective Gaze mechanism that dynamically chooses whether to glance at global context or gaze into high-value regions, filtering irrelevant information before retrieval. We design a dual-stage training strategy: Reflective GoG Behavior Alignment via supervised fine-tuning instills the fundamental GoG paradigm, while Complexity-Adaptive Reinforcement Learning further enhances the model&#x27;s capability to handle complex queries through iterative reasoning. Experiments across six benchmarks demonstrate state-of-the-art performance. Ablation studies confirm that both Selective Gaze and complexity-adaptive RL are essential for effective visual search. We will release our data and models for further exploration soon.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.13942">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.13942.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.13942.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DC-VLAQ: Query-Residual Aggregation for Robust Visual Place Recognition</span>
        <span class="paper-authors">Hanyu Zhu, Zhihao Zhan, Yuhang Ming, Liang Li, Dibo Hou, Javier Civera, Wanzeng Kong</span>
        <span class="paper-meta">Updated 2026-01-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">One of the central challenges in visual place recognition (VPR) is learning a robust global representation that remains discriminative under large viewpoint changes, illumination variations, and severe domain shifts. While visual foundation models (VFMs) provide strong local features, most existing methods rely on a single model, overlooking the complementary cues offered by different VFMs. However, exploiting such complementary information inevitably alters token distributions, which challenges the stability of existing query-based global aggregation schemes. To address these challenges, we propose DC-VLAQ, a representation-centric framework that integrates the fusion of complementary VFMs and robust global aggregation. Specifically, we first introduce a lightweight residual-guided complementary fusion that anchors representations in the DINOv2 feature space while injecting complementary semantics from CLIP through a learned residual correction. In addition, we propose the Vector of Local Aggregated Queries (VLAQ), a query--residual global aggregation scheme that encodes local tokens by their residual responses to learnable queries, resulting in improved stability and the preservation of fine-grained discriminative cues. Extensive experiments on standard VPR benchmarks, including Pitts30k, Tokyo24/7, MSLS, Nordland, SPED, and AmsterTime, demonstrate that DC-VLAQ consistently outperforms strong baselines and achieves state-of-the-art performance, particularly under challenging domain shifts and long-term appearance changes.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.12729">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.12729.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.12729.pdf">
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
        <span class="paper-title">Simple Models, Rich Representations: Visual Decoding from Primate Intracortical Neural Signals</span>
        <span class="paper-authors">Matteo Ciferri, Matteo Ferrante, Nicola Toschi</span>
        <span class="paper-meta">Updated 2026-01-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Understanding how neural activity gives rise to perception is a central challenge in neuroscience. We address the problem of decoding visual information from high-density intracortical recordings in primates, using the THINGS Ventral Stream Spiking Dataset. We systematically evaluate the effects of model architecture, training objectives, and data scaling on decoding performance. Results show that decoding accuracy is mainly driven by modeling temporal dynamics in neural signals, rather than architectural complexity. A simple model combining temporal attention with a shallow MLP achieves up to 70% top-1 image retrieval accuracy, outperforming linear baselines as well as recurrent and convolutional approaches. Scaling analyses reveal predictable diminishing returns with increasing input dimensionality and dataset size. Building on these findings, we design a modular generative decoding pipeline that combines low-resolution latent reconstruction with semantically conditioned diffusion, generating plausible images from 200 ms of brain activity. This framework provides principles for brain-computer interfaces and semantic neural decoding.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.11108">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.11108.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.11108.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Multilingual-To-Multimodal (M2M): Unlocking New Languages with Monolingual Text</span>
        <span class="paper-authors">Piyush Singh Pasi</span>
        <span class="paper-meta">Updated 2026-01-15</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Multimodal models excel in English, supported by abundant image-text and audio-text data, but performance drops sharply for other languages due to limited multilingual multimodal resources. Existing solutions rely heavily on machine translation, while advances in multilingual text modeling remain underutilized. We introduce METAL, a lightweight alignment method that learns only a few linear layers using English text alone to map multilingual text embeddings into a multimodal space. Despite its simplicity, METAL matches baseline performance in English (94.9 percent Recall at 10) and achieves strong zero-shot transfer (89.5 percent Recall at 10 averaged across 11 languages, 10 unseen) on XTD text-to-image retrieval. Qualitative t-SNE visualizations show that multilingual embeddings align tightly with multimodal representations, while weight analysis reveals that the transformation reshapes embedding geometry rather than performing trivial rotations. Beyond image-text retrieval, METAL generalizes to audio-text retrieval and cross-lingual text-to-image generation. We release code and checkpoints at https://github.com/m2m-codebase/M2M , as well as multilingual evaluation datasets including MSCOCO Multilingual 30K (https://huggingface.co/datasets/piyushsinghpasi/mscoco-multilingual-30k ), AudioCaps Multilingual (https://huggingface.co/datasets/piyushsinghpasi/audiocaps-multilingual ), and Clotho Multilingual (https://huggingface.co/datasets/piyushsinghpasi/clotho-multilingual ), to facilitate further research.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.10096">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.10096.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.10096.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">UniHash: Unifying Pointwise and Pairwise Hashing Paradigms for Seen and Unseen Category Retrieval</span>
        <span class="paper-authors">Xiaoxu Ma, Runhao Li, Hanwen Liu, Xiangbo Zhang, Zhenyu Weng</span>
        <span class="paper-meta">Updated 2026-01-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Effective retrieval across both seen and unseen categories is crucial for modern image retrieval systems. Retrieval on seen categories ensures precise recognition of known classes, while retrieval on unseen categories promotes generalization to novel classes with limited supervision. However, most existing deep hashing methods are confined to a single training paradigm, either pointwise or pairwise, where the former excels on seen categories and the latter generalizes better to unseen ones. To overcome this limitation, we propose Unified Hashing (UniHash), a dual-branch framework that unifies the strengths of both paradigms to achieve balanced retrieval performance across seen and unseen categories. UniHash consists of two complementary branches: a center-based branch following the pointwise paradigm and a pairwise branch following the pairwise paradigm. A novel hash code learning method is introduced to enable bidirectional knowledge transfer between branches, improving hash code discriminability and generalization. It employs a mutual learning loss to align hash representations and introduces a Split-Merge Mixture of Hash Experts (SM-MoH) module to enhance cross-branch exchange of hash representations. Theoretical analysis substantiates the effectiveness of UniHash, and extensive experiments on CIFAR-10, MSCOCO, and ImageNet demonstrate that UniHash consistently achieves state-of-the-art performance in both seen and unseen image retrieval scenarios.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.09828">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.09828.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.09828.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Hybrid guided variational autoencoder for visual place recognition</span>
        <span class="paper-authors">Ni Wang, Zihan You, Emre Neftci, Thorben Schoepe</span>
        <span class="paper-meta">Updated 2026-01-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Autonomous agents such as cars, robots and drones need to precisely localize themselves in diverse environments, including in GPS-denied indoor environments. One approach for precise localization is visual place recognition (VPR), which estimates the place of an image based on previously seen places. State-of-the-art VPR models require high amounts of memory, making them unwieldy for mobile deployment, while more compact models lack robustness and generalization capabilities. This work overcomes these limitations for robotics using a combination of event-based vision sensors and an event-based novel guided variational autoencoder (VAE). The encoder part of our model is based on a spiking neural network model which is compatible with power-efficient low latency neuromorphic hardware. The VAE successfully disentangles the visual features of 16 distinct places in our new indoor VPR dataset with a classification performance comparable to other state-of-the-art approaches while, showing robust performance also under various illumination conditions. When tested with novel visual inputs from unknown scenes, our model can distinguish between these places, which demonstrates a high generalization capability by learning the essential features of location. Our compact and robust guided VAE with generalization capabilities poses a promising model for visual place recognition that can significantly enhance mobile robot navigation in known and unknown indoor environments.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.09248">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.09248.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.09248.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Keyframe-based Dense Mapping with the Graph of View-Dependent Local Maps</span>
        <span class="paper-authors">Krzysztof Zielinski, Dominik Belter</span>
        <span class="paper-meta">Updated 2026-01-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">In this article, we propose a new keyframe-based mapping system. The proposed method updates local Normal Distribution Transform maps (NDT) using data from an RGB-D sensor. The cells of the NDT are stored in 2D view-dependent structures to better utilize the properties and uncertainty model of RGB-D cameras. This method naturally represents an object closer to the camera origin with higher precision. The local maps are stored in the pose graph which allows correcting global map after loop closure detection. We also propose a procedure that allows merging and filtering local maps to obtain a global map of the environment. Finally, we compare our method with Octomap and NDT-OM and provide example applications of the proposed mapping method.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.08520">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.08520.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.08520.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Enhancing Image Quality Assessment Ability of LMMs via Retrieval-Augmented Generation</span>
        <span class="paper-authors">Kang Fu, Huiyu Duan, Zicheng Zhang, Yucheng Zhu, Jun Zhao, Xiongkuo Min, Jia Wang, Guangtao Zhai</span>
        <span class="paper-meta">Updated 2026-01-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Large Multimodal Models (LMMs) have recently shown remarkable promise in low-level visual perception tasks, particularly in Image Quality Assessment (IQA), demonstrating strong zero-shot capability. However, achieving state-of-the-art performance often requires computationally expensive fine-tuning methods, which aim to align the distribution of quality-related token in output with image quality levels. Inspired by recent training-free works for LMM, we introduce IQARAG, a novel, training-free framework that enhances LMMs&#x27; IQA ability. IQARAG leverages Retrieval-Augmented Generation (RAG) to retrieve some semantically similar but quality-variant reference images with corresponding Mean Opinion Scores (MOSs) for input image. These retrieved images and input image are integrated into a specific prompt. Retrieved images provide the LMM with a visual perception anchor for IQA task. IQARAG contains three key phases: Retrieval Feature Extraction, Image Retrieval, and Integration &amp; Quality Score Generation. Extensive experiments across multiple diverse IQA datasets, including KADID, KonIQ, LIVE Challenge, and SPAQ, demonstrate that the proposed IQARAG effectively boosts the IQA performance of LMMs, offering a resource-efficient alternative to fine-tuning for quality assessment.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.08311">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.08311.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.08311.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Ground What You See: Hallucination-Resistant MLLMs via Caption Feedback, Diversity-Aware Sampling, and Conflict Regularization</span>
        <span class="paper-authors">Miao Pan, Wangjie Gan, Jintao Chen, Wenqi Zhang, Bing Sun, Jianwei Yin, Xuhong Zhang</span>
        <span class="paper-meta">Updated 2026-01-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">While Multimodal Large Language Models (MLLMs) have achieved remarkable success across diverse tasks, their practical deployment is severely hindered by hallucination issues, which become particularly acute during Reinforcement Learning (RL) optimization. This paper systematically analyzes the root causes of hallucinations in MLLMs under RL training, identifying three critical factors: (1) an over-reliance on chained visual reasoning, where inaccurate initial descriptions or redundant information anchor subsequent inferences to incorrect premises; (2) insufficient exploration diversity during policy optimization, leading the model to generate overly confident but erroneous outputs; and (3) destructive conflicts between training samples, where Neural Tangent Kernel (NTK) similarity causes false associations and unstable parameter updates. To address these challenges, we propose a comprehensive framework comprising three core modules. First, we enhance visual localization by introducing dedicated planning and captioning stages before the reasoning phase, employing a quality-based caption reward to ensure accurate initial anchoring. Second, to improve exploration, we categorize samples based on the mean and variance of their reward distributions, prioritizing samples with high variance to focus the model on diverse and informative data. Finally, to mitigate sample interference, we regulate NTK similarity by grouping sample pairs and applying an InfoNCE loss to push overly similar pairs apart and pull dissimilar ones closer, thereby guiding gradient interactions toward a balanced range. Experimental results demonstrate that our proposed method significantly reduces hallucination rates and effectively enhances the inference accuracy of MLLMs.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.06224">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.06224.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.06224.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Multi-task Cross-modal Learning for Chest X-ray Image Retrieval</span>
        <span class="paper-authors">Zhaohui Liang, Sivaramakrishnan Rajaraman, Niccolo Marini, Zhiyun Xue, Sameer Antani</span>
        <span class="paper-meta">Updated 2026-01-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">CLIP and BiomedCLIP are examples of vision-language foundation models and offer strong cross-modal embeddings; however, they are not optimized for fine-grained medical retrieval tasks, such as retrieving clinically relevant radiology reports using chest X-ray (CXR) image queries. To address this shortcoming, we propose a multi-task learning framework to fine-tune BiomedCLIP and evaluate improvements to CXR image-text retrieval. Using BiomedCLIP as the backbone, we incorporate a lightweight MLP projector head trained with a multi-task composite loss function that includes: (1) a binary cross-entropy loss to distinguish normal from abnormal CXR studies, (2) a supervised contrastive loss to reinforce intra-class consistency, and (3) a CLIP loss to maintain cross-modal alignment. Experimental results demonstrate that the fine-tuned model achieves more balanced and clinically meaningful performance across both image-to-text and text-to-image retrieval tasks compared to the pretrained BiomedCLIP and general-purpose CLIP models. Furthermore, t-SNE visualizations reveal clearer semantic clustering of normal and abnormal cases, demonstrating the model&#x27;s enhanced diagnostic sensitivity. These findings highlight the value of domain-adaptive, multi-task learning for advancing cross-modal retrieval in biomedical applications.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.05399">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.05399.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.05399.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ImLoc: Revisiting Visual Localization with Image-based Representation</span>
        <span class="paper-authors">Xudong Jiang, Fangjinhua Wang, Silvano Galliani, Christoph Vogel, Marc Pollefeys</span>
        <span class="paper-meta">Updated 2026-01-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Existing visual localization methods are typically either 2D image-based, which are easy to build and maintain but limited in effective geometric reasoning, or 3D structure-based, which achieve high accuracy but require a centralized reconstruction and are difficult to update. In this work, we revisit visual localization with a 2D image-based representation and propose to augment each image with estimated depth maps to capture the geometric structure. Supported by the effective use of dense matchers, this representation is not only easy to build and maintain, but achieves highest accuracy in challenging conditions. With compact compression and a GPU-accelerated LO-RANSAC implementation, the whole pipeline is efficient in both storage and computation and allows for a flexible trade-off between accuracy and highest memory efficiency. Our method achieves a new state-of-the-art accuracy on various standard benchmarks and outperforms existing memory-efficient methods at comparable map sizes. Code will be available at https://github.com/cvg/Hierarchical-Localization.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.04185">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.04185.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.04185.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">CSMCIR: CoT-Enhanced Symmetric Alignment with Memory Bank for Composed Image Retrieval</span>
        <span class="paper-authors">Zhipeng Qian, Zihan Liang, Yufei Ma, Ben Chen, Huangyu Dai, Yiwei Ma, Jiayi Ji, Chenyi Lei, Han Li, Xiaoshuai Sun</span>
        <span class="paper-meta">Updated 2026-01-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Composed Image Retrieval (CIR) enables users to search for target images using both a reference image and manipulation text, offering substantial advantages over single-modality retrieval systems. However, existing CIR methods suffer from representation space fragmentation: queries and targets comprise heterogeneous modalities and are processed by distinct encoders, forcing models to bridge misaligned representation spaces only through post-hoc alignment, which fundamentally limits retrieval performance. This architectural asymmetry manifests as three distinct, well-separated clusters in the feature space, directly demonstrating how heterogeneous modalities create fundamentally misaligned representation spaces from initialization. In this work, we propose CSMCIR, a unified representation framework that achieves efficient query-target alignment through three synergistic components. First, we introduce a Multi-level Chain-of-Thought (MCoT) prompting strategy that guides Multimodal Large Language Models to generate discriminative, semantically compatible captions for target images, establishing modal symmetry. Building upon this, we design a symmetric dual-tower architecture where both query and target sides utilize the identical shared-parameter Q-Former for cross-modal encoding, ensuring consistent feature representations and further reducing the alignment gap. Finally, this architectural symmetry enables an entropy-based, temporally dynamic Memory Bank strategy that provides high-quality negative samples while maintaining consistency with the evolving model state. Extensive experiments on four benchmark datasets demonstrate that our CSMCIR achieves state-of-the-art performance with superior training efficiency. Comprehensive ablation studies further validate the effectiveness of each proposed component.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.03728">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.03728.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.03728.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">BREATH-VL: Vision-Language-Guided 6-DoF Bronchoscopy Localization via Semantic-Geometric Fusion</span>
        <span class="paper-authors">Qingyao Tian, Bingyu Yang, Huai Liao, Xinyan Huang, Junyong Li, Dong Yi, Hongbin Liu</span>
        <span class="paper-meta">Updated 2026-01-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Vision-language models (VLMs) have recently shown remarkable performance in navigation and localization tasks by leveraging large-scale pretraining for semantic understanding. However, applying VLMs to 6-DoF endoscopic camera localization presents several challenges: 1) the lack of large-scale, high-quality, densely annotated, and localization-oriented vision-language datasets in real-world medical settings; 2) limited capability for fine-grained pose regression; and 3) high computational latency when extracting temporal features from past frames. To address these issues, we first construct BREATH dataset, the largest in-vivo endoscopic localization dataset to date, collected in the complex human airway. Building on this dataset, we propose BREATH-VL, a hybrid framework that integrates semantic cues from VLMs with geometric information from vision-based registration methods for accurate 6-DoF pose estimation. Our motivation lies in the complementary strengths of both approaches: VLMs offer generalizable semantic understanding, while registration methods provide precise geometric alignment. To further enhance the VLM&#x27;s ability to capture temporal context, we introduce a lightweight context-learning mechanism that encodes motion history as linguistic prompts, enabling efficient temporal reasoning without expensive video-level computation. Extensive experiments demonstrate that the vision-language module delivers robust semantic localization in challenging surgical scenes. Building on this, our BREATH-VL outperforms state-of-the-art vision-only localization methods in both accuracy and generalization, reducing translational error by 25.5% compared with the best-performing baseline, while achieving competitive computational latency.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.03713">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.03713.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.03713.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">HOLO: Homography-Guided Pose Estimator Network for Fine-Grained Visual Localization on SD Maps</span>
        <span class="paper-authors">Xuchang Zhong, Xu Cao, Jinke Feng, Hao Fang</span>
        <span class="paper-meta">Updated 2026-01-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Visual localization on standard-definition (SD) maps has emerged as a promising low-cost and scalable solution for autonomous driving. However, existing regression-based approaches often overlook inherent geometric priors, resulting in suboptimal training efficiency and limited localization accuracy. In this paper, we propose a novel homography-guided pose estimator network for fine-grained visual localization between multi-view images and standard-definition (SD) maps. We construct input pairs that satisfy a homography constraint by projecting ground-view features into the BEV domain and enforcing semantic alignment with map features. Then we leverage homography relationships to guide feature fusion and restrict the pose outputs to a valid feasible region, which significantly improves training efficiency and localization accuracy compared to prior methods relying on attention-based fusion and direct 3-DoF pose regression. To the best of our knowledge, this is the first work to unify BEV semantic reasoning with homography learning for image-to-map localization. Furthermore, by explicitly modeling homography transformations, the proposed framework naturally supports cross-resolution inputs, enhancing model flexibility. Extensive experiments on the nuScenes dataset demonstrate that our approach significantly outperforms existing state-of-the-art visual localization methods. Code and pretrained models will be publicly released to foster future research.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.02730">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.02730.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.02730.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Comparative Analysis of Binarization Methods For Medical Image Hashing On Odir Dataset</span>
        <span class="paper-authors">Nedim Muzoglu</span>
        <span class="paper-meta">Updated 2026-01-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">In this study, we evaluated four binarization methods. Locality-Sensitive Hashing (LSH), Iterative Quantization (ITQ), Kernel-based Supervised Hashing (KSH), and Supervised Discrete Hashing (SDH) on the ODIR dataset using deep feature embeddings. Experimental results show that SDH achieved the best performance, with an mAP@100 of 0.9184 using only 32-bit codes, outperforming LSH, ITQ, and KSH. Compared with prior studies, our method proved highly competitive: Fang et al. reported 0.7528 (Fundus-iSee, 48 bits) and 0.8856 (ASOCT-Cataract, 48 bits), while Wijesinghe et al. achieved 94.01 (KVASIR, 256 bits). Despite using significantly fewer bits, our SDH-based framework reached retrieval accuracy close to the state-of-the-art. These findings demonstrate that SDH is the most effective approach among those tested, offering a practical balance of accuracy, storage, and efficiency for medical image retrieval and device inventory management.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.02564">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.02564.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.02564.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Loop Closure using AnyLoc Visual Place Recognition in DPV-SLAM</span>
        <span class="paper-authors">Wenzheng Zhang, Kazuki Adachi, Yoshitaka Hara, Sousuke Nakamura</span>
        <span class="paper-meta">Updated 2026-01-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Loop closure is crucial for maintaining the accuracy and consistency of visual SLAM. We propose a method to improve loop closure performance in DPV-SLAM. Our approach integrates AnyLoc, a learning-based visual place recognition technique, as a replacement for the classical Bag of Visual Words (BoVW) loop detection method. In contrast to BoVW, which relies on handcrafted features, AnyLoc utilizes deep feature representations, enabling more robust image retrieval across diverse viewpoints and lighting conditions. Furthermore, we propose an adaptive mechanism that dynamically adjusts similarity threshold based on environmental conditions, removing the need for manual tuning. Experiments on both indoor and outdoor datasets demonstrate that our method significantly outperforms the original DPV-SLAM in terms of loop closure accuracy and robustness. The proposed method offers a practical and scalable solution for enhancing loop closure performance in modern SLAM systems.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.02723">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.02723.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.02723.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Vision-Language Reasoning for Geolocalization: A Reinforcement Learning Approach</span>
        <span class="paper-authors">Biao Wu, Meng Fang, Ling Chen, Ke Xu, Tao Cheng, Jun Wang</span>
        <span class="paper-meta">Updated 2026-01-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Recent advances in vision-language models have opened up new possibilities for reasoning-driven image geolocalization. However, existing approaches often rely on synthetic reasoning annotations or external image retrieval, which can limit interpretability and generalizability. In this paper, we present Geo-R, a retrieval-free framework that uncovers structured reasoning paths from existing ground-truth coordinates and optimizes geolocation accuracy via reinforcement learning. We propose the Chain of Region, a rule-based hierarchical reasoning paradigm that generates precise, interpretable supervision by mapping GPS coordinates to geographic entities (e.g., country, province, city) without relying on model-generated or synthetic labels. Building on this, we introduce a lightweight reinforcement learning strategy with coordinate-aligned rewards based on Haversine distance, enabling the model to refine predictions through spatially meaningful feedback. Our approach bridges structured geographic reasoning with direct spatial supervision, yielding improved localization accuracy, stronger generalization, and more transparent inference. Experimental results across multiple benchmarks confirm the effectiveness of Geo-R, establishing a new retrieval-free paradigm for scalable and interpretable image geolocalization. To facilitate further research and ensure reproducibility, both the model and code will be made publicly available.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.00388">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.00388.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.00388.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">OCP-LS: An Efficient Algorithm for Visual Localization</span>
        <span class="paper-authors">Jindi Zhong, Hongxia Wang, Huanshui Zhang</span>
        <span class="paper-meta">Updated 2025-12-31</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">This paper proposes a novel second-order optimization algorithm. It aims to address large-scale optimization problems in deep learning because it incorporates the OCP method and appropriately approximating the diagonal elements of the Hessian matrix. Extensive experiments on multiple standard visual localization benchmarks demonstrate the significant superiority of the proposed method. Compared with conventional optimiza tion algorithms, our framework achieves competitive localization accuracy while exhibiting faster convergence, enhanced training stability, and improved robustness to noise interference.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.24552">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.24552.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.24552.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Geometric Multi-Session Map Merging with Learned Local Descriptors</span>
        <span class="paper-authors">Yanlong Ma, Nakul S. Joshi, Christa S. Robison, Philip R. Osteen, Brett T. Lopez</span>
        <span class="paper-meta">Updated 2025-12-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Multi-session map merging is crucial for extended autonomous operations in large-scale environments. In this paper, we present GMLD, a learning-based local descriptor framework for large-scale multi-session point cloud map merging that systematically aligns maps collected across different sessions with overlapping regions. The proposed framework employs a keypoint-aware encoder and a plane-based geometric transformer to extract discriminative features for loop closure detection and relative pose estimation. To further improve global consistency, we include inter-session scan matching cost factors in the factor-graph optimization stage. We evaluate our framework on the public datasets, as well as self-collected data from diverse environments. The results show accurate and robust map merging with low error, and the learned features deliver strong performance in both loop closure detection and relative pose estimation.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.24384">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.24384.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.24384.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Learning to Feel the Future: DreamTacVLA for Contact-Rich Manipulation</span>
        <span class="paper-authors">Guo Ye, Zexi Zhang, Xu Zhao, Shang Wu, Haoran Lu, Shihan Lu, Han Liu</span>
        <span class="paper-meta">Updated 2025-12-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Vision-Language-Action (VLA) models have shown remarkable generalization by mapping web-scale knowledge to robotic control, yet they remain blind to physical contact. Consequently, they struggle with contact-rich manipulation tasks that require reasoning about force, texture, and slip. While some approaches incorporate low-dimensional tactile signals, they fail to capture the high-resolution dynamics essential for such interactions. To address this limitation, we introduce DreamTacVLA, a framework that grounds VLA models in contact physics by learning to feel the future. Our model adopts a hierarchical perception scheme in which high-resolution tactile images serve as micro-vision inputs coupled with wrist-camera local vision and third-person macro vision. To reconcile these multi-scale sensory streams, we first train a unified policy with a Hierarchical Spatial Alignment (HSA) loss that aligns tactile tokens with their spatial counterparts in the wrist and third-person views. To further deepen the model&#x27;s understanding of fine-grained contact dynamics, we finetune the system with a tactile world model that predicts future tactile signals. To mitigate tactile data scarcity and the wear-prone nature of tactile sensors, we construct a hybrid large-scale dataset sourced from both high-fidelity digital twin and real-world experiments. By anticipating upcoming tactile states, DreamTacVLA acquires a rich model of contact physics and conditions its actions on both real observations and imagined consequences. Across contact-rich manipulation tasks, it outperforms state-of-the-art VLA baselines, achieving up to 95% success, highlighting the importance of understanding physical contact for robust, touch-aware robotic agents.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.23864">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.23864.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.23864.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MindWatcher: Toward Smarter Multimodal Tool-Integrated Reasoning</span>
        <span class="paper-authors">Jiawei Chen, Xintian Shen, Lihao Zheng, Zhenwei Shao, Hongyuan Zhang, Pengfei Yu, Xudong Rao, Ning Mao, Xiaobo Liu, Lian Wen, Chaoqun Du, Feng Gu, Wei He, Qizhen Li, Shanshan Li, Zide Liu, Jing Luo, Lifu Mu, Xuhao Pan, Chang Ren, Haoyi Sun, Qian Wang, Wei Wang, Hongfu Yang, Jiqing Zhan, Chunpeng Zhou, Zheng Zhou, Hao Ma, Tao Wei, Pan Zhou, Wei Chen</span>
        <span class="paper-meta">Updated 2025-12-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Traditional workflow-based agents exhibit limited intelligence when addressing real-world problems requiring tool invocation. Tool-integrated reasoning (TIR) agents capable of autonomous reasoning and tool invocation are rapidly emerging as a powerful approach for complex decision-making tasks involving multi-step interactions with external environments. In this work, we introduce MindWatcher, a TIR agent integrating interleaved thinking and multimodal chain-of-thought (CoT) reasoning. MindWatcher can autonomously decide whether and how to invoke diverse tools and coordinate their use, without relying on human prompts or workflows. The interleaved thinking paradigm enables the model to switch between thinking and tool calling at any intermediate stage, while its multimodal CoT capability allows manipulation of images during reasoning to yield more precise search results. We implement automated data auditing and evaluation pipelines, complemented by manually curated high-quality datasets for training, and we construct a benchmark, called MindWatcher-Evaluate Bench (MWE-Bench), to evaluate its performance. MindWatcher is equipped with a comprehensive suite of auxiliary reasoning tools, enabling it to address broad-domain multimodal problems. A large-scale, high-quality local image retrieval database, covering eight categories including cars, animals, and plants, endows model with robust object recognition despite its small size. Finally, we design a more efficient training infrastructure for MindWatcher, enhancing training speed and hardware utilization. Experiments not only demonstrate that MindWatcher matches or exceeds the performance of larger or more recent models through superior tool invocation, but also uncover critical insights for agent training, such as the genetic inheritance phenomenon in agentic RL.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.23412">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.23412.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.23412.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Anomaly Detection by Effectively Leveraging Synthetic Images</span>
        <span class="paper-authors">Sungho Kang, Hyunkyu Park, Yeonho Lee, Hanbyul Lee, Mijoo Jeong, YeongHyeon Park, Injae Lee, Juneho Yi</span>
        <span class="paper-meta">Updated 2025-12-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Anomaly detection plays a vital role in industrial manufacturing. Due to the scarcity of real defect images, unsupervised approaches that rely solely on normal images have been extensively studied. Recently, diffusion-based generative models brought attention to training data synthesis as an alternative solution. In this work, we focus on a strategy to effectively leverage synthetic images to maximize the anomaly detection performance. Previous synthesis strategies are broadly categorized into two groups, presenting a clear trade-off. Rule-based synthesis, such as injecting noise or pasting patches, is cost-effective but often fails to produce realistic defect images. On the other hand, generative model-based synthesis can create high-quality defect images but requires substantial cost. To address this problem, we propose a novel framework that leverages a pre-trained text-guided image-to-image translation model and image retrieval model to efficiently generate synthetic defect images. Specifically, the image retrieval model assesses the similarity of the generated images to real normal images and filters out irrelevant outputs, thereby enhancing the quality and relevance of the generated defect images. To effectively leverage synthetic images, we also introduce a two stage training strategy. In this strategy, the model is first pre-trained on a large volume of images from rule-based synthesis and then fine-tuned on a smaller set of high-quality images. This method significantly reduces the cost for data collection while improving the anomaly detection performance. Experiments on the MVTec AD dataset demonstrate the effectiveness of our approach.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.23227">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.23227.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.23227.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">UniPR-3D: Towards Universal Visual Place Recognition with Visual Geometry Grounded Transformer</span>
        <span class="paper-authors">Tianchen Deng, Xun Chen, Ziming Li, Hongming Shen, Danwei Wang, Javier Civera, Hesheng Wang</span>
        <span class="paper-meta">Updated 2025-12-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Visual Place Recognition (VPR) has been traditionally formulated as a single-image retrieval task. Using multiple views offers clear advantages, yet this setting remains relatively underexplored and existing methods often struggle to generalize across diverse environments. In this work we introduce UniPR-3D, the first VPR architecture that effectively integrates information from multiple views. UniPR-3D builds on a VGGT backbone capable of encoding multi-view 3D representations, which we adapt by designing feature aggregators and fine-tune for the place recognition task. To construct our descriptor, we jointly leverage the 3D tokens and intermediate 2D tokens produced by VGGT. Based on their distinct characteristics, we design dedicated aggregation modules for 2D and 3D features, allowing our descriptor to capture fine-grained texture cues while also reasoning across viewpoints. To further enhance generalization, we incorporate both single- and multi-frame aggregation schemes, along with a variable-length sequence retrieval strategy. Our experiments show that UniPR-3D sets a new state of the art, outperforming both single- and multi-view baselines and highlighting the effectiveness of geometry-grounded tokens for VPR. Our code and models will be made publicly available on Github https://github.com/dtc111111/UniPR-3D.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.21078">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.21078.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.21078.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Reloc-VGGT: Visual Re-localization with Geometry Grounded Transformer</span>
        <span class="paper-authors">Tianchen Deng, Wenhua Wu, Kunzhen Wu, Guangming Wang, Siting Zhu, Shenghai Yuan, Xun Chen, Guole Shen, Zhe Liu, Hesheng Wang</span>
        <span class="paper-meta">Updated 2025-12-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Visual localization has traditionally been formulated as a pair-wise pose regression problem. Existing approaches mainly estimate relative poses between two images and employ a late-fusion strategy to obtain absolute pose estimates. However, the late motion average is often insufficient for effectively integrating spatial information, and its accuracy degrades in complex environments. In this paper, we present the first visual localization framework that performs multi-view spatial integration through an early-fusion mechanism, enabling robust operation in both structured and unstructured environments. Our framework is built upon the VGGT backbone, which encodes multi-view 3D geometry, and we introduce a pose tokenizer and projection module to more effectively exploit spatial relationships from multiple database views. Furthermore, we propose a novel sparse mask attention strategy that reduces computational cost by avoiding the quadratic complexity of global attention, thereby enabling real-time performance at scale. Trained on approximately eight million posed image pairs, Reloc-VGGT demonstrates strong accuracy and remarkable generalization ability. Extensive experiments across diverse public datasets consistently validate the effectiveness and efficiency of our approach, delivering high-quality camera pose estimates in real time while maintaining robustness to unseen environments. Our code and models will be publicly released upon acceptance.https://github.com/dtc111111/Reloc-VGGT.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.21883">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.21883.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.21883.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Leveraging Lightweight Entity Extraction for Scalable Event-Based Image Retrieval</span>
        <span class="paper-authors">Dao Sy Duy Minh, Huynh Trung Kiet, Nguyen Lam Phu Quy, Phu-Hoa Pham, Tran Chi Nguyen</span>
        <span class="paper-meta">Updated 2025-12-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Retrieving images from natural language descriptions is a core task at the intersection of computer vision and natural language processing, with wide-ranging applications in search engines, media archiving, and digital content management. However, real-world image-text retrieval remains challenging due to vague or context-dependent queries, linguistic variability, and the need for scalable solutions. In this work, we propose a lightweight two-stage retrieval pipeline that leverages event-centric entity extraction to incorporate temporal and contextual signals from real-world captions. The first stage performs efficient candidate filtering using BM25 based on salient entities, while the second stage applies BEiT-3 models to capture deep multimodal semantics and rerank the results. Evaluated on the OpenEvents v1 benchmark, our method achieves a mean average precision of 0.559, substantially outperforming prior baselines. These results highlight the effectiveness of combining event-guided filtering with long-text vision-language modeling for accurate and efficient retrieval in complex, real-world scenarios. Our code is available at https://github.com/PhamPhuHoa-23/Event-Based-Image-Retrieval</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.21221">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.21221.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.21221.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Soft Filtering: Guiding Zero-shot Composed Image Retrieval with Prescriptive and Proscriptive Constraints</span>
        <span class="paper-authors">Youjin Jung, Seongwoo Cho, Hyun-seok Min, Sungchul Choi</span>
        <span class="paper-meta">Updated 2025-12-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Composed Image Retrieval (CIR) aims to find a target image that aligns with user intent, expressed through a reference image and a modification text. While Zero-shot CIR (ZS-CIR) methods sidestep the need for labeled training data by leveraging pretrained vision-language models, they often rely on a single fused query that merges all descriptive cues of what the user wants, tending to dilute key information and failing to account for what they wish to avoid. Moreover, current CIR benchmarks assume a single correct target per query, overlooking the ambiguity in modification texts. To address these challenges, we propose Soft Filtering with Textual constraints (SoFT), a training-free, plug-and-play filtering module for ZS-CIR. SoFT leverages multimodal large language models (LLMs) to extract two complementary constraints from the reference-modification pair: prescriptive (must-have) and proscriptive (must-avoid) constraints. These serve as semantic filters that reward or penalize candidate images to re-rank results, without modifying the base retrieval model or adding supervision. In addition, we construct a two-stage dataset pipeline that refines CIR benchmarks. We first identify multiple plausible targets per query to construct multi-target triplets, capturing the open-ended nature of user intent. Then guide multimodal LLMs to rewrite the modification text to focus on one target, while referencing contrastive distractors to ensure precision. This enables more comprehensive and reliable evaluation under varying ambiguity levels. Applied on top of CIReVL, a ZS-CIR retriever, SoFT raises R@5 to 65.25 on CIRR (+12.94), mAP@50 to 27.93 on CIRCO (+6.13), and R@50 to 58.44 on FashionIQ (+4.59), demonstrating broad effectiveness.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.20781">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.20781.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.20781.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Towards Natural Language-Based Document Image Retrieval: New Dataset and Benchmark</span>
        <span class="paper-authors">Hao Guo et.al.</span>
        <span class="paper-meta">Updated 2025-12-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.20174">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.20174.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.20174.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Beyond CLIP: Knowledge-Enhanced Multimodal Transformers for Cross-Modal Alignment in Diabetic Retinopathy Diagnosis</span>
        <span class="paper-authors">Argha Kamal Samanta et.al.</span>
        <span class="paper-meta">Updated 2025-12-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.19663">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.19663.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.19663.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Finer-Personalization Rank: Fine-Grained Retrieval Examines Identity Preservation for Personalized Generation</span>
        <span class="paper-authors">Connor Kilrain et.al.</span>
        <span class="paper-meta">Updated 2025-12-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.19026">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.19026.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.19026.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Text2Graph VPR: A Text-to-Graph Expert System for Explainable Place Recognition in Changing Environments</span>
        <span class="paper-authors">Saeideh Yousefzadeh et.al.</span>
        <span class="paper-meta">Updated 2025-12-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.18613">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.18613.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.18613.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Through the PRISm: Importance-Aware Scene Graphs for Image Retrieval</span>
        <span class="paper-authors">Dimitrios Georgoulopoulos et.al.</span>
        <span class="paper-meta">Updated 2025-12-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.18407">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.18407.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.18407.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Robust Scene Coordinate Regression via Geometrically-Consistent Global Descriptors</span>
        <span class="paper-authors">Son Tung Nguyen et.al.</span>
        <span class="paper-meta">Updated 2025-12-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.17226">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.17226.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.17226.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">The Effect of Negation on CLIP in Medical Imaging: Limitations of Contrastive Language-Image Pretraining</span>
        <span class="paper-authors">Jasmine Vu et.al.</span>
        <span class="paper-meta">Updated 2025-12-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.17121">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.17121.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.17121.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MACL: Multi-Label Adaptive Contrastive Learning Loss for Remote Sensing Image Retrieval</span>
        <span class="paper-authors">Amna Amir et.al.</span>
        <span class="paper-meta">Updated 2025-12-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.16294">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.16294.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.16294.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">CLNet: Cross-View Correspondence Makes a Stronger Geo-Localizationer</span>
        <span class="paper-authors">Xianwei Cao et.al.</span>
        <span class="paper-meta">Updated 2025-12-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.14560">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.14560.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.14560.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Neurosymbolic Inference On Foundation Models For Remote Sensing Text-to-image Retrieval With Complex Queries</span>
        <span class="paper-authors">Emanuele Mezzi et.al.</span>
        <span class="paper-meta">Updated 2025-12-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.14102">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.14102.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.14102.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Towards Test-time Efficient Visual Place Recognition via Asymmetric Query Processing</span>
        <span class="paper-authors">Jaeyoon Kim et.al.</span>
        <span class="paper-meta">Updated 2025-12-15</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.13055">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.13055.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.13055.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Patch-wise Retrieval: A Bag of Practical Techniques for Instance-level Matching</span>
        <span class="paper-authors">Wonseok Choi et.al.</span>
        <span class="paper-meta">Updated 2025-12-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.12610">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.12610.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.12610.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Beyond Pixels: A Training-Free, Text-to-Text Framework for Remote Sensing Image Retrieval</span>
        <span class="paper-authors">J. Xiao et.al.</span>
        <span class="paper-meta">Updated 2025-12-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.10596">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.10596.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.10596.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">YOPO-Nav: Visual Navigation using 3DGS Graphs from One-Pass Videos</span>
        <span class="paper-authors">Ryan Meegan et.al.</span>
        <span class="paper-meta">Updated 2025-12-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.09903">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.09903.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.09903.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Adaptive Thresholding for Visual Place Recognition using Negative Gaussian Mixture Statistics</span>
        <span class="paper-authors">Nick Trinh et.al.</span>
        <span class="paper-meta">Updated 2025-12-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.09071">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.09071.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.09071.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Generalized Referring Expression Segmentation on Aerial Photos</span>
        <span class="paper-authors">Luís Marnoto et.al.</span>
        <span class="paper-meta">Updated 2025-12-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.07338">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.07338.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.07338.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Spatial Retrieval Augmented Autonomous Driving</span>
        <span class="paper-authors">Xiaosong Jia et.al.</span>
        <span class="paper-meta">Updated 2025-12-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.06865">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.06865.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.06865.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Language-driven Fine-grained Retrieval</span>
        <span class="paper-authors">Shijie Wang et.al.</span>
        <span class="paper-meta">Updated 2025-12-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.06255">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.06255.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.06255.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GuideNav: User-Informed Development of a Vision-Only Robotic Navigation Assistant For Blind Travelers</span>
        <span class="paper-authors">Hochul Hwang et.al.</span>
        <span class="paper-meta">Updated 2025-12-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.06147">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.06147.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.06147.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ARM-Thinker: Reinforcing Multimodal Generative Reward Models with Agentic Tool Use and Visual Reasoning</span>
        <span class="paper-authors">Shengyuan Ding et.al.</span>
        <span class="paper-meta">Updated 2025-12-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.05111">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.05111.pdf">PDF</a>
          <a class="chip" href="https://github.com/InternLM/ARM-Thinker">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.05111.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Visual Reasoning Tracer: Object-Level Grounded Reasoning Benchmark</span>
        <span class="paper-authors">Haobo Yuan et.al.</span>
        <span class="paper-meta">Updated 2025-12-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.05091">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.05091.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.05091.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Semantic-Guided Two-Stage GAN for Face Inpainting with Hybrid Perceptual Encoding</span>
        <span class="paper-authors">Abhigyan Bhattacharya et.al.</span>
        <span class="paper-meta">Updated 2025-12-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.05039">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.05039.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.05039.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Revealing stimulus-dependent dynamics through statistical complexity</span>
        <span class="paper-authors">Edson V. de Paula et.al.</span>
        <span class="paper-meta">Updated 2025-12-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.05007">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.05007.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.05007.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Influence of Object Affordance on Action Language Understanding: Evidence from Dynamic Causal Modeling Analysis</span>
        <span class="paper-authors">Supriya Bordoloi et.al.</span>
        <span class="paper-meta">Updated 2025-12-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.04989">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.04989.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.04989.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LiteVGGT: Boosting Vanilla VGGT via Geometry-aware Cached Token Merging</span>
        <span class="paper-authors">Zhijian Shu et.al.</span>
        <span class="paper-meta">Updated 2025-12-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.04939">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.04939.pdf">PDF</a>
          <a class="chip" href="https://github.com/GarlicBa/LiteVGGT-repo">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.04939.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Terahertz Fourier Ptychographic Imaging</span>
        <span class="paper-authors">Pitambar Mukherjee et.al.</span>
        <span class="paper-meta">Updated 2025-12-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.04783">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.04783.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.04783.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">TEMPO-VINE: A Multi-Temporal Sensor Fusion Dataset for Localization and Mapping in Vineyards</span>
        <span class="paper-authors">Mauro Martini et.al.</span>
        <span class="paper-meta">Updated 2025-12-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.04772">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.04772.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.04772.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MemLoRA: Distilling Expert Adapters for On-Device Memory Systems</span>
        <span class="paper-authors">Massimo Bini et.al.</span>
        <span class="paper-meta">Updated 2025-12-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.04763">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.04763.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.04763.pdf">
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
        <span class="paper-title">HUD: Hierarchical Uncertainty-Aware Disambiguation Network for Composed Video Retrieval</span>
        <span class="paper-authors">Zhiwei Chen et.al.</span>
        <span class="paper-meta">Updated 2025-12-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.02792">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.02792.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.02792.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GeoBridge: A Semantic-Anchored Multi-View Foundation Model Bridging Images and Text for Geo-Localization</span>
        <span class="paper-authors">Zixuan Song et.al.</span>
        <span class="paper-meta">Updated 2025-12-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.02697">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.02697.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.02697.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Generative Editing in the Joint Vision-Language Space for Zero-Shot Composed Image Retrieval</span>
        <span class="paper-authors">Xin Wang et.al.</span>
        <span class="paper-meta">Updated 2025-12-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.01636">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.01636.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.01636.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Winning Solutions for the Rayan AI Contest: Compositional Retrieval, Zero-Shot Anomaly Detection, and Backdoor Detection</span>
        <span class="paper-authors">Ali Nafisi et.al.</span>
        <span class="paper-meta">Updated 2025-12-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.01498">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.01498.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.01498.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MARVO: Marine-Adaptive Radiance-aware Visual Odometry</span>
        <span class="paper-authors">Sacchin Sundar et.al.</span>
        <span class="paper-meta">Updated 2025-11-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.22860">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.22860.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.22860.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">UNION: A Lightweight Target Representation for Efficient Zero-Shot Image-Guided Retrieval with Optional Textual Queries</span>
        <span class="paper-authors">Hoang-Bao Le et.al.</span>
        <span class="paper-meta">Updated 2025-11-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.22253">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.22253.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.22253.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Attention-Guided Patch-Wise Sparse Adversarial Attacks on Vision-Language-Action Models</span>
        <span class="paper-authors">Naifu Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-11-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.21663">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.21663.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.21663.pdf">
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
        <span class="paper-title">Qwen3-VL Technical Report</span>
        <span class="paper-authors">Shuai Bai et.al.</span>
        <span class="paper-meta">Updated 2025-11-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.21631">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.21631.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.21631.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Harmony: Harmonizing Audio and Video Generation through Cross-Task Synergy</span>
        <span class="paper-authors">Teng Hu et.al.</span>
        <span class="paper-meta">Updated 2025-11-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.21579">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.21579.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.21579.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FITRep: Attention-Guided Item Representation via MLLMs</span>
        <span class="paper-authors">Guoxiao Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-11-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.21389">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.21389.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.21389.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Thinking With Bounding Boxes: Enhancing Spatio-Temporal Video Grounding via Reinforcement Fine-Tuning</span>
        <span class="paper-authors">Xin Gu et.al.</span>
        <span class="paper-meta">Updated 2025-11-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.21375">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.21375.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.21375.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">HTTM: Head-wise Temporal Token Merging for Faster VGGT</span>
        <span class="paper-authors">Weitian Wang et.al.</span>
        <span class="paper-meta">Updated 2025-11-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.21317">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.21317.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.21317.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Low-dose Chemically Specific Bioimaging via Deep-UV Lensless Holographic Microscopy on a Standard Camera</span>
        <span class="paper-authors">Piotr Arcab et.al.</span>
        <span class="paper-meta">Updated 2025-11-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.21311">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.21311.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.21311.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Adaptive Lighting Control in Visible Light Systems: An Integrated Sensing, Communication, and Illumination Framework</span>
        <span class="paper-authors">Xinyan Xie et.al.</span>
        <span class="paper-meta">Updated 2025-11-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.21271">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.21271.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.21271.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Towards an Effective Action-Region Tracking Framework for Fine-grained Video Action Recognition</span>
        <span class="paper-authors">Baoli Sun et.al.</span>
        <span class="paper-meta">Updated 2025-11-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.21202">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.21202.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.21202.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Wigner and Gabor phase-space analysis of propagators for evolution equations</span>
        <span class="paper-authors">Elena Cordero et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.19400">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.19400.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.19400.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Real-Time Object Tracking with On-Device Deep Learning for Adaptive Beamforming in Dynamic Acoustic Environments</span>
        <span class="paper-authors">Jorge Ortigoso-Narro et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.19396">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.19396.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.19396.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">In-vivo imaging with a low-cost MRI scanner and cloud data processing in low-resource settings</span>
        <span class="paper-authors">Teresa Guallart-Naval et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.19226">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.19226.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.19226.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Can Modern Vision Models Understand the Difference Between an Object and a Look-alike?</span>
        <span class="paper-authors">Itay Cohen et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.19200">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.19200.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.19200.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">From Pixels to Posts: Retrieval-Augmented Fashion Captioning and Hashtag Generation</span>
        <span class="paper-authors">Moazzam Umer Gondal et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.19149">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.19149.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.19149.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Graph-based 3D Human Pose Estimation using WiFi Signals</span>
        <span class="paper-authors">Jichao Chen et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.19105">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.19105.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.19105.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Towards Generalizable Deepfake Detection via Forgery-aware Audio-Visual Adaptation: A Variational Bayesian Approach</span>
        <span class="paper-authors">Fan Nie et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.19080">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.19080.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.19080.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LAA3D: A Benchmark of Detecting and Tracking Low-Altitude Aircraft in 3D Space</span>
        <span class="paper-authors">Hai Wu et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.19057">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.19057.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.19057.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Multi-Agent Monocular Dense SLAM With 3D Reconstruction Priors</span>
        <span class="paper-authors">Haihang Wu et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.19031">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.19031.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.19031.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Dynamic Granularity Matters: Rethinking Vision Transformers Beyond Fixed Patch Splitting</span>
        <span class="paper-authors">Qiyang Yu et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.19021">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.19021.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.19021.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GeoVista: Web-Augmented Agentic Visual Reasoning for Geolocalization</span>
        <span class="paper-authors">Yikun Wang et.al.</span>
        <span class="paper-meta">Updated 2025-11-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.15705">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.15705.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.15705.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">First Frame Is the Place to Go for Video Content Customization</span>
        <span class="paper-authors">Jingxi Chen et.al.</span>
        <span class="paper-meta">Updated 2025-11-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.15700">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.15700.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.15700.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Hierarchical Semantic Tree Anchoring for CLIP-Based Class-Incremental Learning</span>
        <span class="paper-authors">Tao Hu et.al.</span>
        <span class="paper-meta">Updated 2025-11-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.15633">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.15633.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.15633.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Multi-Text Guided Few-Shot Semantic Segmentation</span>
        <span class="paper-authors">Qiang Jiao et.al.</span>
        <span class="paper-meta">Updated 2025-11-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.15515">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.15515.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.15515.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SIGMMA: Hierarchical Graph-Based Multi-Scale Multi-modal Contrastive Alignment of Histopathology Image and Spatial Transcriptome</span>
        <span class="paper-authors">Dabin Jeong et.al.</span>
        <span class="paper-meta">Updated 2025-11-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.15464">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.15464.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.15464.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">HV-Attack: Hierarchical Visual Attack for Multimodal Retrieval Augmented Generation</span>
        <span class="paper-authors">Linyin Luo et.al.</span>
        <span class="paper-meta">Updated 2025-11-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.15435">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.15435.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.15435.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">The Empowerment of Science of Science by Large Language Models: New Tools and Methods</span>
        <span class="paper-authors">Guoqiang Liang et.al.</span>
        <span class="paper-meta">Updated 2025-11-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.15370">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.15370.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.15370.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">C2F-Space: Coarse-to-Fine Space Grounding for Spatial Instructions using Vision-Language Models</span>
        <span class="paper-authors">Nayoung Oh et.al.</span>
        <span class="paper-meta">Updated 2025-11-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.15333">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.15333.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.15333.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Towards Unbiased Cross-Modal Representation Learning for Food Image-to-Recipe Retrieval</span>
        <span class="paper-authors">Qing Wang et.al.</span>
        <span class="paper-meta">Updated 2025-11-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.15201">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.15201.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.15201.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Unbiased Semantic Decoding with Vision Foundation Models for Few-shot Segmentation</span>
        <span class="paper-authors">Jin Wang et.al.</span>
        <span class="paper-meta">Updated 2025-11-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.15118">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.15118.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.15118.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Multi-modal Loop Closure Detection with Foundation Models in Severely Unstructured Environments</span>
        <span class="paper-authors">Laura Alejandra Encinar Gonzalez et.al.</span>
        <span class="paper-meta">Updated 2025-11-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.05404">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.05404.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.05404.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DAFM: Dynamic Adaptive Fusion for Multi-Model Collaboration in Composed Image Retrieval</span>
        <span class="paper-authors">Yawei Cai et.al.</span>
        <span class="paper-meta">Updated 2025-11-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.05020">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.05020.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.05020.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Multi-Task Learning for Visually Grounded Reasoning in Gastrointestinal VQA</span>
        <span class="paper-authors">Itbaan Safwan et.al.</span>
        <span class="paper-meta">Updated 2025-11-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.04384">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.04384.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.04384.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">An Efficient Algorithm for Learning-Based Visual Localization</span>
        <span class="paper-authors">Jindi Zhong et.al.</span>
        <span class="paper-meta">Updated 2025-11-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.04232">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.04232.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.04232.pdf">
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
        <span class="paper-title">LUMA-RAG: Lifelong Multimodal Agents with Provably Stable Streaming Alignment</span>
        <span class="paper-authors">Rohan Wandre et.al.</span>
        <span class="paper-meta">Updated 2025-11-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.02371">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.02371.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.02371.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SEPS: Semantic-enhanced Patch Slimming Framework for fine-grained cross-modal alignment</span>
        <span class="paper-authors">Xinyu Mao et.al.</span>
        <span class="paper-meta">Updated 2025-11-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.01390">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.01390.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.01390.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Evaluating Perspectival Biases in Cross-Modal Retrieval</span>
        <span class="paper-authors">Teerapol Saengsukhiran et.al.</span>
        <span class="paper-meta">Updated 2025-11-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.26861">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.26861.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.26861.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Dynamic Multi-level Weighted Alignment Network for Zero-shot Sketch-based Image Retrieval</span>
        <span class="paper-authors">Hanwen Su et.al.</span>
        <span class="paper-meta">Updated 2025-11-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.00925">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.00925.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.00925.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Multi-Mapcher: Loop Closure Detection-Free Heterogeneous LiDAR Multi-Session SLAM Leveraging Outlier-Robust Registration for Autonomous Vehicles</span>
        <span class="paper-authors">Hyungtae Lim et.al.</span>
        <span class="paper-meta">Updated 2025-11-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.00635">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.00635.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.00635.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Approximate Diverse $k$-nearest Neighbor Search in Vector Database</span>
        <span class="paper-authors">Jiachen Zhao et.al.</span>
        <span class="paper-meta">Updated 2025-10-31</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.27243">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.27243.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.27243.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Scaling Image Geo-Localization to Continent Level</span>
        <span class="paper-authors">Philipp Lindenberger et.al.</span>
        <span class="paper-meta">Updated 2025-10-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.26795">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.26795.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.26795.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Instance-Level Composed Image Retrieval</span>
        <span class="paper-authors">Bill Psomas et.al.</span>
        <span class="paper-meta">Updated 2025-10-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.25387">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.25387.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.25387.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DualCap: Enhancing Lightweight Image Captioning via Dual Retrieval with Similar Scenes Visual Prompts</span>
        <span class="paper-authors">Binbin Li et.al.</span>
        <span class="paper-meta">Updated 2025-10-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.24813">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.24813.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.24813.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Accurate and Scalable Multimodal Pathology Retrieval via Attentive Vision-Language Alignment</span>
        <span class="paper-authors">Hongyi Wang et.al.</span>
        <span class="paper-meta">Updated 2025-10-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.23224">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.23224.pdf">PDF</a>
          <a class="chip" href="https://github.com/Dootmaan/PathSearch">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.23224.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Seeing the Unseen: Towards Zero-Shot Inspection for Wind Turbine Blades using Knowledge-Augmented Vision Language Models</span>
        <span class="paper-authors">Yang Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-10-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.22868">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.22868.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.22868.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">TWC-SLAM: Multi-Agent Cooperative SLAM with Text Semantics and WiFi Features Integration for Similar Indoor Environments</span>
        <span class="paper-authors">Chunyu Li et.al.</span>
        <span class="paper-meta">Updated 2025-10-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.22754">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.22754.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.22754.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Cross-view Localization and Synthesis -- Datasets, Challenges and Opportunities</span>
        <span class="paper-authors">Ningli Xu et.al.</span>
        <span class="paper-meta">Updated 2025-10-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.22736">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.22736.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.22736.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">STATUS Bench: A Rigorous Benchmark for Evaluating Object State Understanding in Vision-Language Models</span>
        <span class="paper-authors">Mahiro Ukai et.al.</span>
        <span class="paper-meta">Updated 2025-10-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.22571">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.22571.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.22571.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Bag-of-Word-Groups (BoWG): A Robust and Efficient Loop Closure Detection Method Under Perceptual Aliasing</span>
        <span class="paper-authors">Xiang Fei et.al.</span>
        <span class="paper-meta">Updated 2025-10-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.22529">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.22529.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.22529.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">BioCAP: Exploiting Synthetic Captions Beyond Labels in Biological Foundation Models</span>
        <span class="paper-authors">Ziheng Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-10-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.20095">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.20095.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.20095.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Beyond Single Images: Retrieval Self-Augmented Unsupervised Camouflaged Object Detection</span>
        <span class="paper-authors">Ji Du et.al.</span>
        <span class="paper-meta">Updated 2025-10-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.18437">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.18437.pdf">PDF</a>
          <a class="chip" href="https://github.com/xiaohainku/RISE">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.18437.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ImageGem: In-the-wild Generative Image Interaction Dataset for Generative Model Personalization</span>
        <span class="paper-authors">Yuanhe Guo et.al.</span>
        <span class="paper-meta">Updated 2025-10-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.18433">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.18433.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.18433.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DualHash: A Stochastic Primal-Dual Algorithm with Theoretical Guarantee for Deep Hashing</span>
        <span class="paper-authors">Luxuan Li et.al.</span>
        <span class="paper-meta">Updated 2025-10-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.18218">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.18218.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.18218.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Joint Multi-Condition Representation Modelling via Matrix Factorisation for Visual Place Recognition</span>
        <span class="paper-authors">Timur Ismagilov et.al.</span>
        <span class="paper-meta">Updated 2025-10-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.17739">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.17739.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.17739.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Small Language Models Offer Significant Potential for Science Community</span>
        <span class="paper-authors">Jian Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-10-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.18890">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.18890.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.18890.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Acquisition of interpretable domain information during brain MR image harmonization for content-based image retrieval</span>
        <span class="paper-authors">Keima Abe et.al.</span>
        <span class="paper-meta">Updated 2025-10-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.14535">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.14535.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.14535.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Through the Lens of Doubt: Robust and Efficient Uncertainty Estimation for Visual Place Recognition</span>
        <span class="paper-authors">Emily Miller et.al.</span>
        <span class="paper-meta">Updated 2025-10-15</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.13464">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.13464.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.13464.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Embedding the Teacher: Distilling vLLM Preferences for Scalable Image Retrieval</span>
        <span class="paper-authors">Eric He et.al.</span>
        <span class="paper-meta">Updated 2025-10-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.12014">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.12014.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.12014.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Hierarchical Scheduling for Multi-Vector Image Retrieval</span>
        <span class="paper-authors">Maoliang Li et.al.</span>
        <span class="paper-meta">Updated 2025-10-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.08976">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.08976.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.08976.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DarkHash: A Data-Free Backdoor Attack Against Deep Hashing</span>
        <span class="paper-authors">Ziqi Zhou et.al.</span>
        <span class="paper-meta">Updated 2025-10-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.08094">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.08094.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.08094.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">CIR-CoT: Towards Interpretable Composed Image Retrieval via End-to-End Chain-of-Thought Reasoning</span>
        <span class="paper-authors">Weihuang Lin et.al.</span>
        <span class="paper-meta">Updated 2025-10-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.08003">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.08003.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.08003.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Mutual Learning for Hashing: Unlocking Strong Hash Functions from Weak Supervision</span>
        <span class="paper-authors">Xiaoxu Ma et.al.</span>
        <span class="paper-meta">Updated 2025-10-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.07703">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.07703.pdf">PDF</a>
          <a class="chip" href="https://github.com/mxx0723/MLH">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.07703.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Multi-hop Deep Joint Source-Channel Coding with Deep Hash Distillation for Semantically Aligned Image Retrieval</span>
        <span class="paper-authors">Didrik Bergström et.al.</span>
        <span class="paper-meta">Updated 2025-10-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.06868">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.06868.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.06868.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">CalibCLIP: Contextual Calibration of Dominant Semantics for Text-Driven Image Retrieval</span>
        <span class="paper-authors">Bin Kang et.al.</span>
        <span class="paper-meta">Updated 2025-10-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.05586">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.05586.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.05586.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Personalizing Retrieval using Joint Embeddings or &quot;the Return of Fluffy&quot;</span>
        <span class="paper-authors">Bruno Korbar et.al.</span>
        <span class="paper-meta">Updated 2025-10-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.05411">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.05411.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.05411.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Flexible and Efficient Spatio-Temporal Transformer for Sequential Visual Place Recognition</span>
        <span class="paper-authors">Yu Kiu et.al.</span>
        <span class="paper-meta">Updated 2025-10-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.04282">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.04282.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.04282.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">The Overlooked Value of Test-time Reference Sets in Visual Place Recognition</span>
        <span class="paper-authors">Mubariz Zaffar et.al.</span>
        <span class="paper-meta">Updated 2025-10-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.03751">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.03751.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.03751.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Novel UWB Synthetic Aperture Radar Imaging for Mobile Robot Mapping</span>
        <span class="paper-authors">Charith Premachandra et.al.</span>
        <span class="paper-meta">Updated 2025-10-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.02874">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.02874.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.02874.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Team Xiaomi EV-AD VLA: Caption-Guided Retrieval System for Cross-Modal Drone Navigation -- Technical Report for IROS 2025 RoboSense Challenge Track 4</span>
        <span class="paper-authors">Lingfeng Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-10-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.02728">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.02728.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.02728.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">EvoWorld: Evolving Panoramic World Generation with Explicit 3D Memory</span>
        <span class="paper-authors">Jiahao Wang et.al.</span>
        <span class="paper-meta">Updated 2025-10-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.01183">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.01183.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.01183.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A Scene is Worth a Thousand Features: Feed-Forward Camera Localization from a Collection of Image Features</span>
        <span class="paper-authors">Axel Barroso-Laguna et.al.</span>
        <span class="paper-meta">Updated 2025-10-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.00978">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.00978.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.00978.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Semantic Visual Simultaneous Localization and Mapping: A Survey on State of the Art, Challenges, and Future Directions</span>
        <span class="paper-authors">Thanh Nguyen Canh et.al.</span>
        <span class="paper-meta">Updated 2025-10-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.00783">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.00783.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.00783.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Video Object Segmentation-Aware Audio Generation</span>
        <span class="paper-authors">Ilpo Viertola et.al.</span>
        <span class="paper-meta">Updated 2025-09-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.26604">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.26604.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.26604.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SQUARE: Semantic Query-Augmented Fusion and Efficient Batch Reranking for Training-free Zero-Shot Composed Image Retrieval</span>
        <span class="paper-authors">Ren-Di Wu et.al.</span>
        <span class="paper-meta">Updated 2025-09-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.26330">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.26330.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.26330.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SETR: A Two-Stage Semantic-Enhanced Framework for Zero-Shot Composed Image Retrieval</span>
        <span class="paper-authors">Yuqi Xiao et.al.</span>
        <span class="paper-meta">Updated 2025-09-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.26012">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.26012.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.26012.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SAGE: Spatial-visual Adaptive Graph Exploration for Visual Place Recognition</span>
        <span class="paper-authors">Shunpeng Chen et.al.</span>
        <span class="paper-meta">Updated 2025-09-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.25723">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.25723.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.25723.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Robust Visual Localization in Compute-Constrained Environments by Salient Edge Rendering and Weighted Hamming Similarity</span>
        <span class="paper-authors">Tu-Hoa Pham et.al.</span>
        <span class="paper-meta">Updated 2025-09-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.25520">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.25520.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.25520.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Performance-Efficiency Trade-off for Fashion Image Retrieval</span>
        <span class="paper-authors">Julio Hurtado et.al.</span>
        <span class="paper-meta">Updated 2025-09-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.24477">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.24477.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.24477.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Prepare for Warp Speed: Sub-millisecond Visual Place Recognition Using Event Cameras</span>
        <span class="paper-authors">Vignesh Ramanathan et.al.</span>
        <span class="paper-meta">Updated 2025-09-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.24094">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.24094.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.24094.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Johnson-Lindenstrauss Lemma Guided Network for Efficient 3D Medical Segmentation</span>
        <span class="paper-authors">Jinpeng Lu et.al.</span>
        <span class="paper-meta">Updated 2025-09-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.22307">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.22307.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.22307.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Efficient Multimodal Dataset Distillation via Generative Models</span>
        <span class="paper-authors">Zhenghao Zhao et.al.</span>
        <span class="paper-meta">Updated 2025-09-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.15472">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.15472.pdf">PDF</a>
          <a class="chip" href="https://github.com/ichbill/EDGE">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.15472.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A Versatile Foundation Model for AI-enabled Mammogram Interpretation</span>
        <span class="paper-authors">Fuxiang Huang et.al.</span>
        <span class="paper-meta">Updated 2025-09-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.20271">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.20271.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.20271.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SGAligner++: Cross-Modal Language-Aided 3D Scene Graph Alignment</span>
        <span class="paper-authors">Binod Singh et.al.</span>
        <span class="paper-meta">Updated 2025-09-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.20401">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.20401.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.20401.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Vision-Free Retrieval: Rethinking Multimodal Search with Textual Scene Descriptions</span>
        <span class="paper-authors">Ioanna Ntinou et.al.</span>
        <span class="paper-meta">Updated 2025-09-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.19203">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.19203.pdf">PDF</a>
          <a class="chip" href="https://github.com/IoannaNti/LexiCLIP">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.19203.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">OrthoLoC: UAV 6-DoF Localization and Calibration Using Orthographic Geodata</span>
        <span class="paper-authors">Oussema Dhaouadi et.al.</span>
        <span class="paper-meta">Updated 2025-09-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.18350">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.18350.pdf">PDF</a>
          <a class="chip" href="https://github.com/deepscenario/OrthoLoC">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.18350.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Learning Attribute-Aware Hash Codes for Fine-Grained Image Retrieval via Query Optimization</span>
        <span class="paper-authors">Peng Wang et.al.</span>
        <span class="paper-meta">Updated 2025-09-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.17049">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.17049.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.17049.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SERVAL: Surprisingly Effective Zero-Shot Visual Document Retrieval Powered by Large Vision and Language Models</span>
        <span class="paper-authors">Thong Nguyen et.al.</span>
        <span class="paper-meta">Updated 2025-09-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.15432">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.15432.pdf">PDF</a>
          <a class="chip" href="https://github.com/thongnt99/serval">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.15432.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">PRISM: Product Retrieval In Shopping Carts using Hybrid Matching</span>
        <span class="paper-authors">Arda Kabadayi et.al.</span>
        <span class="paper-meta">Updated 2025-09-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.14985">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.14985.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.14985.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Chain-of-Thought Re-ranking for Image Retrieval Tasks</span>
        <span class="paper-authors">Shangrong Wu et.al.</span>
        <span class="paper-meta">Updated 2025-09-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.14746">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.14746.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.14746.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DiffVL: Diffusion-Based Visual Localization on 2D Maps via BEV-Conditioned GPS Denoising</span>
        <span class="paper-authors">Li Gao et.al.</span>
        <span class="paper-meta">Updated 2025-09-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.14565">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.14565.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.14565.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Event-LAB: Towards Standardized Evaluation of Neuromorphic Localization Methods</span>
        <span class="paper-authors">Adam D. Hines et.al.</span>
        <span class="paper-meta">Updated 2025-09-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.14516">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.14516.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.14516.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Hashing-Baseline: Rethinking Hashing in the Age of Pretrained Models</span>
        <span class="paper-authors">Ilyass Moummad et.al.</span>
        <span class="paper-meta">Updated 2025-09-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.14427">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.14427.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.14427.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">CSMoE: An Efficient Remote Sensing Foundation Model with Soft Mixture-of-Experts</span>
        <span class="paper-authors">Leonard Hackel et.al.</span>
        <span class="paper-meta">Updated 2025-09-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.14104">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.14104.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.14104.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DiffHash: Text-Guided Targeted Attack via Diffusion Models against Deep Hashing Image Retrieval</span>
        <span class="paper-authors">Zechao Liu et.al.</span>
        <span class="paper-meta">Updated 2025-09-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.12824">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.12824.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.12824.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Semantic-Enhanced Cross-Modal Place Recognition for Robust Robot Localization</span>
        <span class="paper-authors">Yujia Lin et.al.</span>
        <span class="paper-meta">Updated 2025-09-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.13474">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.13474.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.13474.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MapAnything: Universal Feed-Forward Metric 3D Reconstruction</span>
        <span class="paper-authors">Nikhil Keetha et.al.</span>
        <span class="paper-meta">Updated 2025-09-16</span>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Bridging Vision Language Models and Symbolic Grounding for Video Question Answering</span>
        <span class="paper-authors">Haodi Ma et.al.</span>
        <span class="paper-meta">Updated 2025-09-15</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.11862">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.11862.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.11862.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Listening for &quot;You&quot;: Enhancing Speech Image Retrieval via Target Speaker Extraction</span>
        <span class="paper-authors">Wenhao Yang et.al.</span>
        <span class="paper-meta">Updated 2025-09-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.09306">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.09306.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.09306.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Aerial-ground Cross-modal Localization: Dataset, Ground-truth, and Benchmark</span>
        <span class="paper-authors">Yandi Yang et.al.</span>
        <span class="paper-meta">Updated 2025-09-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.07362">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.07362.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.07362.pdf">
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
        <span class="paper-title">Towards an Accurate and Effective Robot Vision (The Problem of Topological Localization for Mobile Robots)</span>
        <span class="paper-authors">Emanuela Boros et.al.</span>
        <span class="paper-meta">Updated 2025-09-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.04948">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.04948.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.04948.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FloodVision: Urban Flood Depth Estimation Using Foundation Vision-Language Models and Domain Knowledge Graph</span>
        <span class="paper-authors">Zhangding Liu et.al.</span>
        <span class="paper-meta">Updated 2025-09-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.04772">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.04772.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.04772.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Global-to-Local or Local-to-Global? Enhancing Image Retrieval with Efficient Local Search and Effective Global Re-ranking</span>
        <span class="paper-authors">Dror Aiger et.al.</span>
        <span class="paper-meta">Updated 2025-09-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.04351">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.04351.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.04351.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DUDE: Diffusion-Based Unsupervised Cross-Domain Image Retrieval</span>
        <span class="paper-authors">Ruohong Yang et.al.</span>
        <span class="paper-meta">Updated 2025-09-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.04193">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.04193.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.04193.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Scale, Don&#x27;t Fine-tune: Guiding Multimodal LLMs for Efficient Visual Place Recognition at Test-Time</span>
        <span class="paper-authors">Jintao Cheng et.al.</span>
        <span class="paper-meta">Updated 2025-09-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.02129">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.02129.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.02129.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Ensemble-Based Event Camera Place Recognition Under Varying Illumination</span>
        <span class="paper-authors">Therese Joseph et.al.</span>
        <span class="paper-meta">Updated 2025-09-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.01968">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.01968.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.01968.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">M3Ret: Unleashing Zero-shot Multimodal Medical Image Retrieval via Self-Supervision</span>
        <span class="paper-authors">Che Liu et.al.</span>
        <span class="paper-meta">Updated 2025-09-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.01360">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.01360.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.01360.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ReCap: Event-Aware Image Captioning with Article Retrieval and Semantic Gaussian Normalization</span>
        <span class="paper-authors">Thinh-Phuc Nguyen et.al.</span>
        <span class="paper-meta">Updated 2025-09-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.01259">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.01259.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.01259.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FAR-Net: Multi-Stage Fusion Network with Enhanced Semantic Alignment and Adaptive Reconciliation for Composed Image Retrieval</span>
        <span class="paper-authors">Jeong-Woo Park et.al.</span>
        <span class="paper-meta">Updated 2025-07-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.12823">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.12823.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.12823.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MCoT-RE: Multi-Faceted Chain-of-Thought and Re-Ranking for Training-Free Zero-Shot Composed Image Retrieval</span>
        <span class="paper-authors">Jeong-Woo Park et.al.</span>
        <span class="paper-meta">Updated 2025-07-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.12819">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.12819.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.12819.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">QuRe: Query-Relevant Retrieval through Hard Negative Sampling in Composed Image Retrieval</span>
        <span class="paper-authors">Jaehyun Kwak et.al.</span>
        <span class="paper-meta">Updated 2025-07-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.12416">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.12416.pdf">PDF</a>
          <a class="chip" href="https://github.com/jackwaky/QuRe">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.12416.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">CorrMoE: Mixture of Experts with De-stylization Learning for Cross-Scene and Cross-Domain Correspondence Pruning</span>
        <span class="paper-authors">Peiwen Xia et.al.</span>
        <span class="paper-meta">Updated 2025-07-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.11834">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.11834.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.11834.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GT-Loc: Unifying When and Where in Images Through a Joint Embedding Space</span>
        <span class="paper-authors">David G. Shatwell et.al.</span>
        <span class="paper-meta">Updated 2025-07-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.10473">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.10473.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.10473.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Text-to-Remote-Sensing-Image Retrieval beyond RGB Sources</span>
        <span class="paper-authors">Daniele Rege Cambrin et.al.</span>
        <span class="paper-meta">Updated 2025-07-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.10403">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.10403.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.10403.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Kaleidoscopic Background Attack: Disrupting Pose Estimation with Multi-Fold Radial Symmetry Textures</span>
        <span class="paper-authors">Xinlong Ding et.al.</span>
        <span class="paper-meta">Updated 2025-07-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.10265">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.10265.pdf">PDF</a>
          <a class="chip" href="https://github.com/wakuwu/KBA">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.10265.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">RadiomicsRetrieval: A Customizable Framework for Medical Image Retrieval Using Radiomics Features</span>
        <span class="paper-authors">Inye Na et.al.</span>
        <span class="paper-meta">Updated 2025-07-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.08546">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.08546.pdf">PDF</a>
          <a class="chip" href="https://github.com/nainye/RadiomicsRetrieval">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.08546.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LiDAR, GNSS and IMU Sensor Alignment through Dynamic Time Warping to Construct 3D City Maps</span>
        <span class="paper-authors">Haitian Wang et.al.</span>
        <span class="paper-meta">Updated 2025-07-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.08420">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.08420.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.08420.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Deep Hashing with Semantic Hash Centers for Image Retrieval</span>
        <span class="paper-authors">Li Chen et.al.</span>
        <span class="paper-meta">Updated 2025-07-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.08404">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.08404.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.08404.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SCREP: Scene Coordinate Regression and Evidential Learning-based Perception-Aware Trajectory Generation</span>
        <span class="paper-authors">Juyeop Han et.al.</span>
        <span class="paper-meta">Updated 2025-07-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.07467">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.07467.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.07467.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">VP-SelDoA: Visual-prompted Selective DoA Estimation of Target Sound via Semantic-Spatial Matching</span>
        <span class="paper-authors">Yu Chen et.al.</span>
        <span class="paper-meta">Updated 2025-07-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.07384">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.07384.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.07384.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Evaluating Attribute Confusion in Fashion Text-to-Image Generation</span>
        <span class="paper-authors">Ziyue Liu et.al.</span>
        <span class="paper-meta">Updated 2025-07-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.07079">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.07079.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.07079.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MS-DPPs: Multi-Source Determinantal Point Processes for Contextual Diversity Refinement of Composite Attributes in Text to Image Retrieval</span>
        <span class="paper-authors">Naoya Sogi et.al.</span>
        <span class="paper-meta">Updated 2025-07-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.06654">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.06654.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.06654.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Automatic Synthesis of High-Quality Triplet Data for Composed Image Retrieval</span>
        <span class="paper-authors">Haiwen Li et.al.</span>
        <span class="paper-meta">Updated 2025-07-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.05970">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.05970.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.05970.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">OFFSET: Segmentation-based Focus Shift Revision for Composed Image Retrieval</span>
        <span class="paper-authors">Zhiwei Chen et.al.</span>
        <span class="paper-meta">Updated 2025-07-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.05631">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.05631.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.05631.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">What&#x27;s Making That Sound Right Now? Video-centric Audio-Visual Localization</span>
        <span class="paper-authors">Hahyeon Choi et.al.</span>
        <span class="paper-meta">Updated 2025-07-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.04667">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.04667.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.04667.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Llama Nemoretriever Colembed: Top-Performing Text-Image Retrieval Model</span>
        <span class="paper-authors">Mengyao Xu et.al.</span>
        <span class="paper-meta">Updated 2025-07-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.05513">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.05513.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.05513.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">An analysis of vision-language models for fabric retrieval</span>
        <span class="paper-authors">Francesco Giuliari et.al.</span>
        <span class="paper-meta">Updated 2025-07-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.04735">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.04735.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.04735.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Simultaneous Localization and Mapping Using Active mmWave Sensing in 5G NR</span>
        <span class="paper-authors">Tao Du et.al.</span>
        <span class="paper-meta">Updated 2025-07-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.04662">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.04662.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.04662.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">U-ViLAR: Uncertainty-Aware Visual Localization for Autonomous Driving via Differentiable Association and Registration</span>
        <span class="paper-authors">Xiaofan Li et.al.</span>
        <span class="paper-meta">Updated 2025-07-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.04503">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.04503.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.04503.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Query-Based Adaptive Aggregation for Multi-Dataset Joint Training Toward Universal Visual Place Recognition</span>
        <span class="paper-authors">Jiuhong Xiao et.al.</span>
        <span class="paper-meta">Updated 2025-07-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.03831">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.03831.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.03831.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LoD-Loc v2: Aerial Visual Localization over Low Level-of-Detail City Models using Explicit Silhouette Alignment</span>
        <span class="paper-authors">Juelin Zhu et.al.</span>
        <span class="paper-meta">Updated 2025-07-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.00659">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.00659.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.00659.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Utilizing a Novel Deep Learning Method for Scene Categorization in Remote Sensing Data</span>
        <span class="paper-authors">Ghufran A. Omran et.al.</span>
        <span class="paper-meta">Updated 2025-06-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.22939">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.22939.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.22939.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Mask-aware Text-to-Image Retrieval: Referring Expression Segmentation Meets Cross-modal Retrieval</span>
        <span class="paper-authors">Li-Cheng Shen et.al.</span>
        <span class="paper-meta">Updated 2025-06-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.22864">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.22864.pdf">PDF</a>
          <a class="chip" href="https://github.com/AI-Application-and-Integration-Lab/MaTIR">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.22864.pdf">
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
        <span class="paper-title">OracleFusion: Assisting the Decipherment of Oracle Bone Script with Structurally Constrained Semantic Typography</span>
        <span class="paper-authors">Caoshuo Li et.al.</span>
        <span class="paper-meta">Updated 2025-06-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.21101">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.21101.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.21101.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Referring Expression Instance Retrieval and A Strong End-to-End Baseline</span>
        <span class="paper-authors">Xiangzhao Hao et.al.</span>
        <span class="paper-meta">Updated 2025-06-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.18246">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.18246.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.18246.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Visualizing intercalation effects in 2D materials using AFM based techniques</span>
        <span class="paper-authors">Karmen Kapustić et.al.</span>
        <span class="paper-meta">Updated 2025-06-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.20467">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.20467.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.20467.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">On the Burstiness of Faces in Set</span>
        <span class="paper-authors">Jiong Wang et.al.</span>
        <span class="paper-meta">Updated 2025-06-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.20312">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.20312.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.20312.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">jina-embeddings-v4: Universal Embeddings for Multimodal Multilingual Retrieval</span>
        <span class="paper-authors">Michael Günther et.al.</span>
        <span class="paper-meta">Updated 2025-06-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.18902">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.18902.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.18902.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Class Agnostic Instance-level Descriptor for Visual Instance Search</span>
        <span class="paper-authors">Qi-Ying Sun et.al.</span>
        <span class="paper-meta">Updated 2025-06-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.16745">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.16745.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.16745.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MambaHash: Visual State Space Deep Hashing Model for Large-Scale Image Retrieval</span>
        <span class="paper-authors">Chao He et.al.</span>
        <span class="paper-meta">Updated 2025-06-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.16353">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.16353.pdf">PDF</a>
          <a class="chip" href="https://github.com/shuaichaochao/mambahash">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.16353.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Fine-grained Image Retrieval via Dual-Vision Adaptation</span>
        <span class="paper-authors">Xin Jiang et.al.</span>
        <span class="paper-meta">Updated 2025-06-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.16273">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.16273.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.16273.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Adversarial Attacks and Detection in Visual Place Recognition for Safer Robot Navigation</span>
        <span class="paper-authors">Connor Malone et.al.</span>
        <span class="paper-meta">Updated 2025-06-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.15988">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.15988.pdf">PDF</a>
          <a class="chip" href="https://github.com/QVPR/aarapsiproject">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.15988.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Semantic and Feature Guided Uncertainty Quantification of Visual Localization for Autonomous Vehicles</span>
        <span class="paper-authors">Qiyuan Wu et.al.</span>
        <span class="paper-meta">Updated 2025-06-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.15851">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.15851.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.15851.pdf">
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
        <span class="paper-title">HARMONY: A Scalable Distributed Vector Database for High-Throughput Approximate Nearest Neighbor Search</span>
        <span class="paper-authors">Qian Xu et.al.</span>
        <span class="paper-meta">Updated 2025-06-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.14707">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.14707.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.14707.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">TACS-Graphs: Traversability-Aware Consistent Scene Graphs for Ground Robot Indoor Localization and Mapping</span>
        <span class="paper-authors">Jeewon Kim et.al.</span>
        <span class="paper-meta">Updated 2025-06-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.14178">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.14178.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.14178.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Hierarchical Multi-Positive Contrastive Learning for Patent Image Retrieval</span>
        <span class="paper-authors">Kshitij Kavimandan et.al.</span>
        <span class="paper-meta">Updated 2025-06-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.13496">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.13496.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.13496.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A Semantically-Aware Relevance Measure for Content-Based Medical Image Retrieval Evaluation</span>
        <span class="paper-authors">Xiaoyang Wei et.al.</span>
        <span class="paper-meta">Updated 2025-06-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.13509">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.13509.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.13509.pdf">
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
        <span class="paper-title">SuperPlace: The Renaissance of Classical Feature Aggregation for Visual Place Recognition in the Era of Foundation Models</span>
        <span class="paper-authors">Bingxi Liu et.al.</span>
        <span class="paper-meta">Updated 2025-06-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.13073">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.13073.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.13073.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Feature Complementation Architecture for Visual Place Recognition</span>
        <span class="paper-authors">Weiwei Wang et.al.</span>
        <span class="paper-meta">Updated 2025-06-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.12401">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.12401.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.12401.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Towards a general-purpose foundation model for fMRI analysis</span>
        <span class="paper-authors">Cheng Wang et.al.</span>
        <span class="paper-meta">Updated 2025-06-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.11167">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.11167.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.11167.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Improving Personalized Search with Regularized Low-Rank Parameter Updates</span>
        <span class="paper-authors">Fiona Ryan et.al.</span>
        <span class="paper-meta">Updated 2025-06-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.10182">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.10182.pdf">PDF</a>
          <a class="chip" href="https://github.com/adobe-research/polar-vl">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.10182.pdf">
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
        <span class="paper-title">Safeguarding Multimodal Knowledge Copyright in the RAG-as-a-Service Environment</span>
        <span class="paper-authors">Tianyu Chen et.al.</span>
        <span class="paper-meta">Updated 2025-06-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.10030">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.10030.pdf">PDF</a>
          <a class="chip" href="https://github.com/tychenn/aqua">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.10030.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Robust Visual Localization via Semantic-Guided Multi-Scale Transformer</span>
        <span class="paper-authors">Zhongtao Tian et.al.</span>
        <span class="paper-meta">Updated 2025-06-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.08526">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.08526.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.08526.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Interpretable and Reliable Detection of AI-Generated Images via Grounded Reasoning in MLLMs</span>
        <span class="paper-authors">Yikun Ji et.al.</span>
        <span class="paper-meta">Updated 2025-06-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.07045">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.07045.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.07045.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Zero Shot Composed Image Retrieval</span>
        <span class="paper-authors">Santhosh Kakarla et.al.</span>
        <span class="paper-meta">Updated 2025-06-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.06602">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.06602.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.06602.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GenIR: Generative Visual Feedback for Mental Image Retrieval</span>
        <span class="paper-authors">Diji Yang et.al.</span>
        <span class="paper-meta">Updated 2025-06-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.06220">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.06220.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.06220.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Astra: Toward General-Purpose Mobile Robots via Hierarchical Multimodal Learning</span>
        <span class="paper-authors">Sheng Chen et.al.</span>
        <span class="paper-meta">Updated 2025-06-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.06205">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.06205.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.06205.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">HypeVPR: Exploring Hyperbolic Space for Perspective to Equirectangular Visual Place Recognition</span>
        <span class="paper-authors">Suhan Woo et.al.</span>
        <span class="paper-meta">Updated 2025-06-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.04764">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.04764.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.04764.pdf">
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
        <span class="paper-title">Entity Image and Mixed-Modal Image Retrieval Datasets</span>
        <span class="paper-authors">Cristian-Ioan Blaga et.al.</span>
        <span class="paper-meta">Updated 2025-06-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.02291">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.02291.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.02291.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Quantization-based Bounds on the Wasserstein Metric</span>
        <span class="paper-authors">Jonathan Bobrutsky et.al.</span>
        <span class="paper-meta">Updated 2025-06-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.00976">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.00976.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.00976.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SORCE: Small Object Retrieval in Complex Environments</span>
        <span class="paper-authors">Chunxu Liu et.al.</span>
        <span class="paper-meta">Updated 2025-05-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.24441">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.24441.pdf">PDF</a>
          <a class="chip" href="https://github.com/mcg-nju/sorce">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.24441.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Sketch Down the FLOPs: Towards Efficient Networks for Human Sketch</span>
        <span class="paper-authors">Aneeshan Sain et.al.</span>
        <span class="paper-meta">Updated 2025-05-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.23763">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.23763.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.23763.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">4DTAM: Non-Rigid Tracking and Mapping via Dynamic Surface Gaussians</span>
        <span class="paper-authors">Hidenobu Matsuki et.al.</span>
        <span class="paper-meta">Updated 2025-05-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.22859">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.22859.pdf">PDF</a>
          <a class="chip" href="https://github.com/muskie82/4dtam">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.22859.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Visual Loop Closure Detection Through Deep Graph Consensus</span>
        <span class="paper-authors">Martin Büchner et.al.</span>
        <span class="paper-meta">Updated 2025-05-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.21754">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.21754.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.21754.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">QuARI: Query Adaptive Retrieval Improvement</span>
        <span class="paper-authors">Eric Xing et.al.</span>
        <span class="paper-meta">Updated 2025-05-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.21647">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.21647.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.21647.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ConText-CIR: Learning from Concepts in Text for Composed Image Retrieval</span>
        <span class="paper-authors">Eric Xing et.al.</span>
        <span class="paper-meta">Updated 2025-05-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.20764">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.20764.pdf">PDF</a>
          <a class="chip" href="https://github.com/mvrl/context-cir">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.20764.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Visualized Text-to-Image Retrieval</span>
        <span class="paper-authors">Di Wu et.al.</span>
        <span class="paper-meta">Updated 2025-05-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.20291">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.20291.pdf">PDF</a>
          <a class="chip" href="https://github.com/xiaowu0162/visualize-then-retrieve">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.20291.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Multimodal Reasoning Agent for Zero-Shot Composed Image Retrieval</span>
        <span class="paper-authors">Rong-Cheng Tu et.al.</span>
        <span class="paper-meta">Updated 2025-05-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.19952">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.19952.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.19952.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Can Visual Encoder Learn to See Arrows?</span>
        <span class="paper-authors">Naoyuki Terashita et.al.</span>
        <span class="paper-meta">Updated 2025-05-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.19944">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.19944.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.19944.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">TAT-VPR: Ternary Adaptive Transformer for Dynamic and Efficient Visual Place Recognition</span>
        <span class="paper-authors">Oliver Grainge et.al.</span>
        <span class="paper-meta">Updated 2025-05-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.16447">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.16447.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.16447.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Highlighting What Matters: Promptable Embeddings for Attribute-Focused Image Retrieval</span>
        <span class="paper-authors">Siting Li et.al.</span>
        <span class="paper-meta">Updated 2025-05-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.15877">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.15877.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.15877.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SCENIR: Visual Semantic Clarity through Unsupervised Scene Graph Retrieval</span>
        <span class="paper-authors">Nikolaos Chaidos et.al.</span>
        <span class="paper-meta">Updated 2025-05-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.15867">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.15867.pdf">PDF</a>
          <a class="chip" href="https://github.com/nickhaidos/scenir-icml2025">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.15867.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Multimodal RAG-driven Anomaly Detection and Classification in Laser Powder Bed Fusion using Large Language Models</span>
        <span class="paper-authors">Kiarash Naghavi Khanghah et.al.</span>
        <span class="paper-meta">Updated 2025-05-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.13828">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.13828.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.13828.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MMS-VPR: Multimodal Street-Level Visual Place Recognition Dataset and Benchmark</span>
        <span class="paper-authors">Yiwei Ou et.al.</span>
        <span class="paper-meta">Updated 2025-05-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.12254">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.12254.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.12254.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Improved Bag-of-Words Image Retrieval with Geometric Constraints for Ground Texture Localization</span>
        <span class="paper-authors">Aaron Wilhelm et.al.</span>
        <span class="paper-meta">Updated 2025-05-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.11620">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.11620.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.11620.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Redundancy-Aware Pretraining of Vision-Language Foundation Models in Remote Sensing</span>
        <span class="paper-authors">Mathis Jürgen Adler et.al.</span>
        <span class="paper-meta">Updated 2025-05-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.11121">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.11121.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.11121.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SafeNav: Safe Path Navigation using Landmark Based Localization in a GPS-denied Environment</span>
        <span class="paper-authors">Ganesh Sapkota et.al.</span>
        <span class="paper-meta">Updated 2025-05-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.01956">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.01956.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.01956.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Thermal-LiDAR Fusion for Robust Tunnel Localization in GNSS-Denied and Low-Visibility Conditions</span>
        <span class="paper-authors">Lukas Schichler et.al.</span>
        <span class="paper-meta">Updated 2025-05-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.03565">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.03565.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.03565.pdf">
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
        <span class="paper-title">Seeing the Abstract: Translating the Abstract Language for Vision Language Models</span>
        <span class="paper-authors">Davide Talon et.al.</span>
        <span class="paper-meta">Updated 2025-05-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.03242">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.03242.pdf">PDF</a>
          <a class="chip" href="https://github.com/davidetalon/fashionact">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.03242.pdf">
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
        <span class="paper-title">NeuroLoc: Encoding Navigation Cells for 6-DOF Camera Localization</span>
        <span class="paper-authors">Xun Li et.al.</span>
        <span class="paper-meta">Updated 2025-05-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.01113">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.01113.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.01113.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GSFeatLoc: Visual Localization Using Feature Correspondence on 3D Gaussian Splatting</span>
        <span class="paper-authors">Jongwon Lee et.al.</span>
        <span class="paper-meta">Updated 2025-05-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.20379">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.20379.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.20379.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">From Mapping to Composing: A Two-Stage Framework for Zero-shot Composed Image Retrieval</span>
        <span class="paper-authors">Yabing Wang et.al.</span>
        <span class="paper-meta">Updated 2025-04-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.17990">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.17990.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.17990.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A Guide to Structureless Visual Localization</span>
        <span class="paper-authors">Vojtech Panek et.al.</span>
        <span class="paper-meta">Updated 2025-04-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.17636">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.17636.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.17636.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Rethinking Vision Transformer for Large-Scale Fine-Grained Image Retrieval</span>
        <span class="paper-authors">Xin Jiang et.al.</span>
        <span class="paper-meta">Updated 2025-04-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.16691">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.16691.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.16691.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Media Content Atlas: A Pipeline to Explore and Investigate Multidimensional Media Space using Multimodal LLMs</span>
        <span class="paper-authors">Merve Cerit et.al.</span>
        <span class="paper-meta">Updated 2025-04-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.16323">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.16323.pdf">PDF</a>
          <a class="chip" href="https://github.com/mediacontentatlas/mediacontentatlas">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.16323.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A Multimodal Recaptioning Framework to Account for Perceptual Diversity in Multilingual Vision-Language Modeling</span>
        <span class="paper-authors">Kyle Buettner et.al.</span>
        <span class="paper-meta">Updated 2025-04-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.14359">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.14359.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.14359.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SemCORE: A Semantic-Enhanced Generative Cross-Modal Retrieval Framework with MLLMs</span>
        <span class="paper-authors">Haoxuan Li et.al.</span>
        <span class="paper-meta">Updated 2025-04-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.13172">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.13172.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.13172.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Generalized Visual Relation Detection with Diffusion Models</span>
        <span class="paper-authors">Kaifeng Gao et.al.</span>
        <span class="paper-meta">Updated 2025-04-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.12100">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.12100.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.12100.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Visual Re-Ranking with Non-Visual Side Information</span>
        <span class="paper-authors">Gustav Hanning et.al.</span>
        <span class="paper-meta">Updated 2025-04-15</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.11134">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.11134.pdf">PDF</a>
          <a class="chip" href="https://github.com/ghanning/gcsa">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.11134.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">TMCIR: Token Merge Benefits Composed Image Retrieval</span>
        <span class="paper-authors">Chaoyang Wang et.al.</span>
        <span class="paper-meta">Updated 2025-04-15</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.10995">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.10995.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.10995.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Focus on Local: Finding Reliable Discriminative Regions for Visual Place Recognition</span>
        <span class="paper-authors">Changwei Wang et.al.</span>
        <span class="paper-meta">Updated 2025-04-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.09881">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.09881.pdf">PDF</a>
          <a class="chip" href="https://github.com/chenshunpeng/FoL">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.09881.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Evolved Hierarchical Masking for Self-Supervised Learning</span>
        <span class="paper-authors">Zhanzhou Feng et.al.</span>
        <span class="paper-meta">Updated 2025-04-12</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.09155">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.09155.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.09155.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">HAL-NeRF: High Accuracy Localization Leveraging Neural Radiance Fields</span>
        <span class="paper-authors">Asterios Reppas et.al.</span>
        <span class="paper-meta">Updated 2025-04-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.08901">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.08901.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.08901.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Hypergraph Vision Transformers: Images are More than Nodes, More than Edges</span>
        <span class="paper-authors">Joshua Fixelle et.al.</span>
        <span class="paper-meta">Updated 2025-04-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.08710">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.08710.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.08710.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FocalLens: Instruction Tuning Enables Zero-Shot Conditional Image Representations</span>
        <span class="paper-authors">Cheng-Yu Hsieh et.al.</span>
        <span class="paper-meta">Updated 2025-04-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.08368">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.08368.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.08368.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">PNE-SGAN: Probabilistic NDT-Enhanced Semantic Graph Attention Network for LiDAR Loop Closure Detection</span>
        <span class="paper-authors">Xiong Li et.al.</span>
        <span class="paper-meta">Updated 2025-04-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.08280">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.08280.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.08280.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Multi-modal Reference Learning for Fine-grained Text-to-Image Retrieval</span>
        <span class="paper-authors">Zehong Ma et.al.</span>
        <span class="paper-meta">Updated 2025-04-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.07718">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.07718.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.07718.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A Pointcloud Registration Framework for Relocalization in Subterranean Environments</span>
        <span class="paper-authors">David Akhihiero et.al.</span>
        <span class="paper-meta">Updated 2025-04-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.07231">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.07231.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.07231.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Patch Matters: Training-free Fine-grained Image Caption Enhancement via Local Perception</span>
        <span class="paper-authors">Ruotian Peng et.al.</span>
        <span class="paper-meta">Updated 2025-04-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.06666">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.06666.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.06666.pdf">
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
        <span class="paper-meta">Updated 2025-04-08</span>
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
        <span class="paper-title">NCL-CIR: Noise-aware Contrastive Learning for Composed Image Retrieval</span>
        <span class="paper-authors">Peng Gao et.al.</span>
        <span class="paper-meta">Updated 2025-04-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.04339">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.04339.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.04339.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Re-thinking Temporal Search for Long-Form Video Understanding</span>
        <span class="paper-authors">Jinhui Ye et.al.</span>
        <span class="paper-meta">Updated 2025-04-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.02259">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.02259.pdf">PDF</a>
          <a class="chip" href="https://github.com/longvideohaystack/tstar">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.02259.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">REJEPA: A Novel Joint-Embedding Predictive Architecture for Efficient Remote Sensing Image Retrieval</span>
        <span class="paper-authors">Shabnam Choudhury et.al.</span>
        <span class="paper-meta">Updated 2025-04-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.03169">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.03169.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.03169.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A Chefs KISS -- Utilizing semantic information in both ICP and SLAM framework</span>
        <span class="paper-authors">Sven Ochs et.al.</span>
        <span class="paper-meta">Updated 2025-04-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.02086">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.02086.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.02086.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Prompt-Guided Attention Head Selection for Focus-Oriented Image Retrieval</span>
        <span class="paper-authors">Yuji Nozawa et.al.</span>
        <span class="paper-meta">Updated 2025-04-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.01348">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.01348.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.01348.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">IDMR: Towards Instance-Driven Precise Visual Correspondence in Multimodal Retrieval</span>
        <span class="paper-authors">Bangwei Liu et.al.</span>
        <span class="paper-meta">Updated 2025-04-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.00954">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.00954.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.00954.pdf">
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
        <span class="paper-title">CIBR: Cross-modal Information Bottleneck Regularization for Robust CLIP Generalization</span>
        <span class="paper-authors">Yingrui Ji et.al.</span>
        <span class="paper-meta">Updated 2025-03-31</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.24182">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.24182.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.24182.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LiM-Loc: Visual Localization with Dense and Accurate 3D Reference Maps Directly Corresponding 2D Keypoints to 3D LiDAR Point Clouds</span>
        <span class="paper-authors">Masahiko Tsuji et.al.</span>
        <span class="paper-meta">Updated 2025-03-31</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.23664">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.23664.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.23664.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Multiview Image-Based Localization</span>
        <span class="paper-authors">Cameron Fiore et.al.</span>
        <span class="paper-meta">Updated 2025-03-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.23577">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.23577.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.23577.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LOCORE: Image Re-ranking with Long-Context Sequence Modeling</span>
        <span class="paper-authors">Zilin Xiao et.al.</span>
        <span class="paper-meta">Updated 2025-03-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.21772">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.21772.pdf">PDF</a>
          <a class="chip" href="https://github.com/MrZilinXiao/LongContextReranker">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.21772.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Fwd2Bot: LVLM Visual Token Compression with Double Forward Bottleneck</span>
        <span class="paper-authors">Adrian Bulat et.al.</span>
        <span class="paper-meta">Updated 2025-03-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.21757">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.21757.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.21757.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">UGNA-VPR: A Novel Training Paradigm for Visual Place Recognition Based on Uncertainty-Guided NeRF Augmentation</span>
        <span class="paper-authors">Yehui Shen et.al.</span>
        <span class="paper-meta">Updated 2025-03-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.21338">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.21338.pdf">PDF</a>
          <a class="chip" href="https://github.com/nubot-nudt/ugna-vpr">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.21338.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FineCIR: Explicit Parsing of Fine-Grained Modification Semantics for Composed Image Retrieval</span>
        <span class="paper-authors">Zixu Li et.al.</span>
        <span class="paper-meta">Updated 2025-03-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.21309">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.21309.pdf">PDF</a>
          <a class="chip" href="https://github.com/sdu-l/finecir">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.21309.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Clean Image May be Dangerous: Data Poisoning Attacks Against Deep Hashing</span>
        <span class="paper-authors">Shuai Li et.al.</span>
        <span class="paper-meta">Updated 2025-03-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.21236">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.21236.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.21236.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">CoLLM: A Large Language Model for Composed Image Retrieval</span>
        <span class="paper-authors">Chuong Huynh et.al.</span>
        <span class="paper-meta">Updated 2025-03-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.19910">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.19910.pdf">PDF</a>
          <a class="chip" href="https://github.com/hmchuong/CoLLM">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.19910.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Scene-agnostic Pose Regression for Visual Localization</span>
        <span class="paper-authors">Junwei Zheng et.al.</span>
        <span class="paper-meta">Updated 2025-03-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.19543">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.19543.pdf">PDF</a>
          <a class="chip" href="https://github.com/JunweiZheng93/SPR">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.19543.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">From Sparse to Dense: Camera Relocalization with Scene-Specific Detector from Feature Gaussian Splatting</span>
        <span class="paper-authors">Zhiwei Huang et.al.</span>
        <span class="paper-meta">Updated 2025-03-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.19358">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.19358.pdf">PDF</a>
          <a class="chip" href="https://github.com/zju3dv/STDLoc">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.19358.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Fine-grained Textual Inversion Network for Zero-Shot Composed Image Retrieval</span>
        <span class="paper-authors">Haoqiang Lin et.al.</span>
        <span class="paper-meta">Updated 2025-03-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.19296">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.19296.pdf">PDF</a>
          <a class="chip" href="https://github.com/ZiChao111/FTI4CIR">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.19296.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LocDiffusion: Identifying Locations on Earth by Diffusing in the Hilbert Space</span>
        <span class="paper-authors">Zhangyu Wang et.al.</span>
        <span class="paper-meta">Updated 2025-03-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.18142">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.18142.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.18142.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Selecting and Pruning: A Differentiable Causal Sequentialized State-Space Model for Two-View Correspondence Learning</span>
        <span class="paper-authors">Xiang Fang et.al.</span>
        <span class="paper-meta">Updated 2025-03-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.17938">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.17938.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.17938.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">What Time Tells Us? An Explorative Study of Time Awareness Learned from Static Images</span>
        <span class="paper-authors">Dongheng Lin et.al.</span>
        <span class="paper-meta">Updated 2025-03-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.17899">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.17899.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.17899.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">good4cir: Generating Detailed Synthetic Captions for Composed Image Retrieval</span>
        <span class="paper-authors">Pranavi Kolouju et.al.</span>
        <span class="paper-meta">Updated 2025-03-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.17871">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.17871.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.17871.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Missing Target-Relevant Information Prediction with World Model for Accurate Zero-Shot Composed Image Retrieval</span>
        <span class="paper-authors">Yuanmin Tang et.al.</span>
        <span class="paper-meta">Updated 2025-03-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.17109">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.17109.pdf">PDF</a>
          <a class="chip" href="https://github.com/pter61/predicir">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.17109.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Autonomous Exploration-Based Precise Mapping for Mobile Robots through Stepwise and Consistent Motions</span>
        <span class="paper-authors">Muhua Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-03-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.17005">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.17005.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.17005.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">PromptHash: Affinity-Prompted Collaborative Cross-Modal Learning for Adaptive Hashing Retrieval</span>
        <span class="paper-authors">Qiang Zou et.al.</span>
        <span class="paper-meta">Updated 2025-03-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.16064">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.16064.pdf">PDF</a>
          <a class="chip" href="https://github.com/ShiShuMo/PromptHash">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.16064.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Automating 3D Dataset Generation with Neural Radiance Fields</span>
        <span class="paper-authors">P. Schulz et.al.</span>
        <span class="paper-meta">Updated 2025-03-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.15997">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.15997.pdf">PDF</a>
          <a class="chip" href="https://github.com/PaulSK98/Nerf2Dataset">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.15997.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">3D Densification for Multi-Map Monocular VSLAM in Endoscopy</span>
        <span class="paper-authors">X. Anadón et.al.</span>
        <span class="paper-meta">Updated 2025-03-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.14346">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.14346.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.14346.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Scale Efficient Training for Large Datasets</span>
        <span class="paper-authors">Qing Zhou et.al.</span>
        <span class="paper-meta">Updated 2025-03-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.13385">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.13385.pdf">PDF</a>
          <a class="chip" href="https://github.com/mrazhou/seta">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.13385.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Multi-Platform Teach-and-Repeat Navigation by Visual Place Recognition Based on Deep-Learned Local Features</span>
        <span class="paper-authors">Václav Truhlařík et.al.</span>
        <span class="paper-meta">Updated 2025-03-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.13090">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.13090.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.13090.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">All You Need to Know About Training Image Retrieval Models</span>
        <span class="paper-authors">Gabriele Berton et.al.</span>
        <span class="paper-meta">Updated 2025-03-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.13045">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.13045.pdf">PDF</a>
          <a class="chip" href="https://github.com/gmberton/image-retrieval">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.13045.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ImageScope: Unifying Language-Guided Image Retrieval via Large Multimodal Model Collective Reasoning</span>
        <span class="paper-authors">Pengfei Luo et.al.</span>
        <span class="paper-meta">Updated 2025-03-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.10166">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.10166.pdf">PDF</a>
          <a class="chip" href="https://github.com/pengfei-luo/ImageScope">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.10166.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Exploring the best way for UAV visual localization under Low-altitude Multi-view Observation Condition: a Benchmark</span>
        <span class="paper-authors">Yibin Ye et.al.</span>
        <span class="paper-meta">Updated 2025-03-12</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.10692">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.10692.pdf">PDF</a>
          <a class="chip" href="https://github.com/uav-avl/benchmark">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.10692.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Revisiting Medical Image Retrieval via Knowledge Consolidation</span>
        <span class="paper-authors">Yang Nan et.al.</span>
        <span class="paper-meta">Updated 2025-03-12</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.09370">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.09370.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.09370.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">CQVPR: Landmark-aware Contextual Queries for Visual Place Recognition</span>
        <span class="paper-authors">Dongyue Li et.al.</span>
        <span class="paper-meta">Updated 2025-03-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.08170">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.08170.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.08170.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Find your Needle: Small Object Image Retrieval via Multi-Object Attention Optimization</span>
        <span class="paper-authors">Michael Green et.al.</span>
        <span class="paper-meta">Updated 2025-03-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.07038">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.07038.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.07038.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Zero-Shot Hashing Based on Reconstruction With Part Alignment</span>
        <span class="paper-authors">Yan Jiang et.al.</span>
        <span class="paper-meta">Updated 2025-03-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.07037">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.07037.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.07037.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Improving Visual Place Recognition with Sequence-Matching Receptiveness Prediction</span>
        <span class="paper-authors">Somayeh Hussaini et.al.</span>
        <span class="paper-meta">Updated 2025-03-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.06840">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.06840.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.06840.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">RoboDesign1M: A Large-scale Dataset for Robot Design Understanding</span>
        <span class="paper-authors">Tri Le et.al.</span>
        <span class="paper-meta">Updated 2025-03-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.06796">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.06796.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.06796.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">StructVPR++: Distill Structural and Semantic Knowledge with Weighting Samples for Visual Place Recognition</span>
        <span class="paper-authors">Yanqing Shen et.al.</span>
        <span class="paper-meta">Updated 2025-03-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.06601">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.06601.pdf">PDF</a>
          <a class="chip" href="https://github.com/syqlyx/StructVPR">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.06601.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">TextInPlace: Indoor Visual Place Recognition in Repetitive Structures with Scene Text Spotting and Verification</span>
        <span class="paper-authors">Huaqi Tao et.al.</span>
        <span class="paper-meta">Updated 2025-03-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.06501">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.06501.pdf">PDF</a>
          <a class="chip" href="https://github.com/hqitao/textinplace">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.06501.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">NeuraLoc: Visual Localization in Neural Implicit Map with Dual Complementary Features</span>
        <span class="paper-authors">Hongjia Zhai et.al.</span>
        <span class="paper-meta">Updated 2025-03-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.06117">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.06117.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.06117.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
</section>
