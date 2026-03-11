---
layout: default
title: Point Cloud Registration
---

<section class="topic-hero" style="--accent: #28d8ff;">
  <div>
    <p class="eyebrow">Topic</p>
    <h1>Point Cloud Registration</h1>
    <p class="topic-lede">Updated 2026.03.11 · 123 papers</p>
  </div>
  <a class="btn ghost" href="../index.html#topics">← Back to topics</a>
</section>

<section class="paper-grid">
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SPIRIT: Perceptive Shared Autonomy for Robust Robotic Manipulation under Deep Learning Uncertainty</span>
        <span class="paper-authors">Jongseok Lee, Ribin Balachandran, Harsimran Singh, Jianxiang Feng, Hrishik Mishra, Marco De Stefano, Rudolph Triebel, Alin Albu-Schaeffer, Konstantin Kondak</span>
        <span class="paper-meta">Updated 2026-03-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Deep learning (DL) has enabled impressive advances in robotic perception, yet its limited robustness and lack of interpretability hinder reliable deployment in safety critical applications. We propose a concept termed perceptive shared autonomy, in which uncertainty estimates from DL based perception are used to regulate the level of autonomy. Specifically, when the robot&#x27;s perception is confident, semi-autonomous manipulation is enabled to improve performance; when uncertainty increases, control transitions to haptic teleoperation for maintaining robustness. In this way, high-performing but uninterpretable DL methods can be integrated safely into robotic systems. A key technical enabler is an uncertainty aware DL based point cloud registration approach based on the so called Neural Tangent Kernels (NTK). We evaluate perceptive shared autonomy on challenging aerial manipulation tasks through a user study of 15 participants and realization of mock-up industrial scenarios, demonstrating reliable robotic manipulation despite failures in DL based perception. The resulting system, named SPIRIT, improves both manipulation performance and system reliability. SPIRIT was selected as a finalist of a major industrial innovation award.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.05111">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.05111.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.05111.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Geometry-to-Image Synthesis-Driven Generative Point Cloud Registration</span>
        <span class="paper-authors">Haobo Jiang, Jin Xie, Jian Yang, Liang Yu, Jianmin Zheng</span>
        <span class="paper-meta">Updated 2026-02-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">In this paper, we propose a novel 3D registration paradigm, Generative Point Cloud Registration, which bridges advanced 2D generative models with 3D matching tasks to enhance registration performance. Our key idea is to generate cross-view consistent image pairs that are well-aligned with the source and target point clouds, enabling geometry-color feature fusion to facilitate robust matching. To ensure high-quality matching, the generated image pair should feature both 2D-3D geometric consistency and cross-view texture consistency. To this end, we introduce DepthMatch-ControlNet and LiDARMatch-ControlNet, two matching-specific, controllable 2D generative models. Specifically, for depth camera-based 3D registration with point clouds derived from the depth maps, DepthMatch-ControlNet leverages the depth-conditioned generation capabilities of ControlNet to synthesize perspective-view RGB images that are geometrically consistent with depth maps, ensuring accurate 2D-3D alignment. Additionally, by incorporating a coupled conditional denoising scheme and coupled prompt guidance, it further promotes cross-view feature interaction, guiding texture consistency generation. To address LiDAR-based 3D registration with point clouds captured by LiDAR sensors, LiDARMatch-ControlNet extends this framework by conditioning on paired equirectangular range maps projected from 360-degree LiDAR point clouds, generating corresponding panoramic RGB images. Our generative 3D registration paradigm is general and can be seamlessly integrated into a wide range of existing registration methods to improve their performance. Extensive experiments on the 3DMatch and ScanNet datasets (for depth-camera settings), as well as the Dur360BEV dataset (for LiDAR settings), demonstrate the effectiveness of our approach.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.09407">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.09407.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.09407.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">End-to-End LiDAR optimization for 3D point cloud registration</span>
        <span class="paper-authors">Siddhant Katyan, Marc-André Gardner, Jean-François Lalonde</span>
        <span class="paper-meta">Updated 2026-02-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">LiDAR sensors are a key modality for 3D perception, yet they are typically designed independently of downstream tasks such as point cloud registration. Conventional registration operates on pre-acquired datasets with fixed LiDAR configurations, leading to suboptimal data collection and significant computational overhead for sampling, noise filtering, and parameter tuning. In this work, we propose an adaptive LiDAR sensing framework that dynamically adjusts sensor parameters, jointly optimizing LiDAR acquisition and registration hyperparameters. By integrating registration feedback into the sensing loop, our approach optimally balances point density, noise, and sparsity, improving registration accuracy and efficiency. Evaluations in the CARLA simulation demonstrate that our method outperforms fixed-parameter baselines while retaining generalization abilities, highlighting the potential of adaptive LiDAR for autonomous perception and robotic applications.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.10492">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.10492.pdf">PDF</a>
          <a class="chip" href="https://github.com/siddhantkatyan/e2e-lidar-registration">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.10492.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Beyond the Vehicle: Cooperative Localization by Fusing Point Clouds for GPS-Challenged Urban Scenarios</span>
        <span class="paper-authors">Kuo-Yi Chao, Ralph Rasshofer, Alois Christian Knoll</span>
        <span class="paper-meta">Updated 2026-02-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Accurate vehicle localization is a critical challenge in urban environments where GPS signals are often unreliable. This paper presents a cooperative multi-sensor and multi-modal localization approach to address this issue by fusing data from vehicle-to-vehicle (V2V) and vehicle-to-infrastructure (V2I) systems. Our approach integrates cooperative data with a point cloud registration-based simultaneous localization and mapping (SLAM) algorithm. The system processes point clouds generated from diverse sensor modalities, including vehicle-mounted LiDAR and stereo cameras, as well as sensors deployed at intersections. By leveraging shared data from infrastructure, our method significantly improves localization accuracy and robustness in complex, GPS-noisy urban scenarios.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.03908">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.03908.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.03908.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Parametric vector flows for registration fields in bounded domains with applications to nonlinear interpolation of shock-dominated flows</span>
        <span class="paper-authors">Jon Labatut, Jean-Baptiste Chapelier, Angelo Iollo, Tommaso Taddei</span>
        <span class="paper-meta">Updated 2026-01-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We present a registration procedure for parametric model order reduction (MOR) in two- and three-dimensional bounded domains. In the MOR framework, registration methods exploit solution snapshots to identify a parametric coordinate transformation that improves the approximation of the solution set through linear subspaces. For each training parameter, optimization-based (or variational) registration methods minimize a target function that measures the alignment of the coherent structures of interest (e.g., shocks, shear layers, cracks) for different parameter values, over a family of bijections of the computational domain $Ω$. We consider diffeomorphisms $Φ$ that are vector flows of given velocity fields $v$ with vanishing normal component on $\partial Ω$; we rely on a sensor to extract appropriate point clouds from the solution snapshots and we develop an expectation-maximization procedure to simultaneously solve the point cloud matching problem and to determine the velocity $v$ (and thus the bijection $Φ$); finally, we combine our registration method with the nonlinear interpolation technique of [Iollo, Taddei, J. Comput. Phys., 2022] to perform accurate interpolations of fluid dynamic fields in the presence of shocks. Numerical results for a two-dimensional inviscid transonic flow past a NACA airfoil and a three-dimensional viscous transonic flow past an ONERA M6 wing illustrate the many elements of the methodology and demonstrate the effectiveness of nonlinear interpolation for shock-dominated fields.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.22712">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.22712.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.22712.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Iterative Differential Entropy Minimization (IDEM) method for fine rigid pairwise 3D Point Cloud Registration: A Focus on the Metric</span>
        <span class="paper-authors">Emmanuele Barberi, Felice Sfravara, Filippo Cucinotta</span>
        <span class="paper-meta">Updated 2026-01-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Point cloud registration is a central theme in computer vision, with alignment algorithms continuously improving for greater robustness. Commonly used methods evaluate Euclidean distances between point clouds and minimize an objective function, such as Root Mean Square Error (RMSE). However, these approaches are most effective when the point clouds are well-prealigned and issues such as differences in density, noise, holes, and limited overlap can compromise the results. Traditional methods, such as Iterative Closest Point (ICP), require choosing one point cloud as fixed, since Euclidean distances lack commutativity. When only one point cloud has issues, adjustments can be made, but in real scenarios, both point clouds may be affected, often necessitating preprocessing. The authors introduce a novel differential entropy-based metric, designed to serve as the objective function within an optimization framework for fine rigid pairwise 3D point cloud registration, denoted as Iterative Differential Entropy Minimization (IDEM). This metric does not depend on the choice of a fixed point cloud and, during transformations, reveals a clear minimum corresponding to the best alignment. Multiple case studies are conducted, and the results are compared with those obtained using RMSE, Chamfer distance, and Hausdorff distance. The proposed metric proves effective even with density differences, noise, holes, and partial overlap, where RMSE does not always yield optimal alignment.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.09601">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.09601.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.09601.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A Multi-Mode Structured Light 3D Imaging System with Multi-Source Information Fusion for Underwater Pipeline Detection</span>
        <span class="paper-authors">Qinghan Hu, Haijiang Zhu, Na Sun, Lei Chen, Zhengqiang Fan, Zhiqing Li</span>
        <span class="paper-meta">Updated 2026-01-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Underwater pipelines are highly susceptible to corrosion, which not only shorten their service life but also pose significant safety risks. Compared with manual inspection, the intelligent real-time imaging system for underwater pipeline detection has become a more reliable and practical solution. Among various underwater imaging techniques, structured light 3D imaging can restore the sufficient spatial detail for precise defect characterization. Therefore, this paper develops a multi-mode underwater structured light 3D imaging system for pipeline detection (UW-SLD system) based on multi-source information fusion. First, a rapid distortion correction (FDC) method is employed for efficient underwater image rectification. To overcome the challenges of extrinsic calibration among underwater sensors, a factor graph-based parameter optimization method is proposed to estimate the transformation matrix between the structured light and acoustic sensors. Furthermore, a multi-mode 3D imaging strategy is introduced to adapt to the geometric variability of underwater pipelines. Given the presence of numerous disturbances in underwater environments, a multi-source information fusion strategy and an adaptive extended Kalman filter (AEKF) are designed to ensure stable pose estimation and high-accuracy measurements. In particular, an edge detection-based ICP (ED-ICP) algorithm is proposed. This algorithm integrates pipeline edge detection network with enhanced point cloud registration to achieve robust and high-fidelity reconstruction of defect structures even under variable motion conditions. Extensive experiments are conducted under different operation modes, velocities, and depths. The results demonstrate that the developed system achieves superior accuracy, adaptability and robustness, providing a solid foundation for autonomous underwater pipeline detection.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.11354">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.11354.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.11354.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Towards Zero-Shot Point Cloud Registration Across Diverse Scales, Scenes, and Sensor Setups</span>
        <span class="paper-authors">Hyungtae Lim, Minkyun Seo, Luca Carlone, Jaesik Park</span>
        <span class="paper-meta">Updated 2026-01-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Some deep learning-based point cloud registration methods struggle with zero-shot generalization, often requiring dataset-specific hyperparameter tuning or retraining for new environments. We identify three critical limitations: (a) fixed user-defined parameters (e.g., voxel size, search radius) that fail to generalize across varying scales, (b) learned keypoint detectors exhibit poor cross-domain transferability, and (c) absolute coordinates amplify scale mismatches between datasets. To address these three issues, we present BUFFER-X, a training-free registration framework that achieves zero-shot generalization through: (a) geometric bootstrapping for automatic hyperparameter estimation, (b) distribution-aware farthest point sampling to replace learned detectors, and (c) patch-level coordinate normalization to ensure scale consistency. Our approach employs hierarchical multi-scale matching to extract correspondences across local, middle, and global receptive fields, enabling robust registration in diverse environments. For efficiency-critical applications, we introduce BUFFER-X-Lite, which reduces total computation time by 43% (relative to BUFFER-X) through early exit strategies and fast pose solvers while preserving accuracy. We evaluate on a comprehensive benchmark comprising 12 datasets spanning object-scale, indoor, and outdoor scenes, including cross-sensor registration between heterogeneous LiDAR configurations. Results demonstrate that our approach generalizes effectively without manual tuning or prior knowledge of test domains. Code: https://github.com/MIT-SPARK/BUFFER-X.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.02759">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.02759.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.02759.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Subsecond 3D Mesh Generation for Robot Manipulation</span>
        <span class="paper-authors">Qian Wang, Omar Abdellall, Tony Gao, Xiatao Sun, Daniel Rakita</span>
        <span class="paper-meta">Updated 2025-12-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">3D meshes are a fundamental representation widely used in computer science and engineering. In robotics, they are particularly valuable because they capture objects in a form that aligns directly with how robots interact with the physical world, enabling core capabilities such as predicting stable grasps, detecting collisions, and simulating dynamics. Although automatic 3D mesh generation methods have shown promising progress in recent years, potentially offering a path toward real-time robot perception, two critical challenges remain. First, generating high-fidelity meshes is prohibitively slow for real-time use, often requiring tens of seconds per object. Second, mesh generation by itself is insufficient. In robotics, a mesh must be contextually grounded, i.e., correctly segmented from the scene and registered with the proper scale and pose. Additionally, unless these contextual grounding steps remain efficient, they simply introduce new bottlenecks. In this work, we introduce an end-to-end system that addresses these challenges, producing a high-quality, contextually grounded 3D mesh from a single RGB-D image in under one second. Our pipeline integrates open-vocabulary object segmentation, accelerated diffusion-based mesh generation, and robust point cloud registration, each optimized for both speed and accuracy. We demonstrate its effectiveness in a real-world manipulation task, showing that it enables meshes to be used as a practical, on-demand representation for robotics perception and planning.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.24428">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.24428.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.24428.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MCI-Net: A Robust Multi-Domain Context Integration Network for Point Cloud Registration</span>
        <span class="paper-authors">Shuyuan Lin, Wenwu Peng, Junjie Huang, Qiang Qi, Miaohui Wang, Jian Weng</span>
        <span class="paper-meta">Updated 2025-12-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Robust and discriminative feature learning is critical for high-quality point cloud registration. However, existing deep learning-based methods typically rely on Euclidean neighborhood-based strategies for feature extraction, which struggle to effectively capture the implicit semantics and structural consistency in point clouds. To address these issues, we propose a multi-domain context integration network (MCI-Net) that improves feature representation and registration performance by aggregating contextual cues from diverse domains. Specifically, we propose a graph neighborhood aggregation module, which constructs a global graph to capture the overall structural relationships within point clouds. We then propose a progressive context interaction module to enhance feature discriminability by performing intra-domain feature decoupling and inter-domain context interaction. Finally, we design a dynamic inlier selection method that optimizes inlier weights using residual information from multiple iterations of pose estimation, thereby improving the accuracy and robustness of registration. Extensive experiments on indoor RGB-D and outdoor LiDAR datasets show that the proposed MCI-Net significantly outperforms existing state-of-the-art methods, achieving the highest registration recall of 96.4\% on 3DMatch. Source code is available at http://www.linshuyuan.com.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.23472">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.23472.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.23472.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FUSER: Feed-Forward MUltiview 3D Registration Transformer and SE(3)$^N$ Diffusion Refinement</span>
        <span class="paper-authors">Haobo Jiang, Jin Xie, Jian Yang, Liang Yu, Jianmin Zheng</span>
        <span class="paper-meta">Updated 2025-12-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Registration of multiview point clouds conventionally relies on extensive pairwise matching to build a pose graph for global synchronization, which is computationally expensive and inherently ill-posed without holistic geometric constraints. This paper proposes FUSER, the first feed-forward multiview registration transformer that jointly processes all scans in a unified, compact latent space to directly predict global poses without any pairwise estimation. To maintain tractability, FUSER encodes each scan into low-resolution superpoint features via a sparse 3D CNN that preserves absolute translation cues, and performs efficient intra- and inter-scan reasoning through a Geometric Alternating Attention module. Particularly, we transfer 2D attention priors from off-the-shelf foundation models to enhance 3D feature interaction and geometric consistency. Building upon FUSER, we further introduce FUSER-DF, an SE(3)$^N$ diffusion refinement framework to correct FUSER&#x27;s estimates via denoising in the joint SE(3)$^N$ space. FUSER acts as a surrogate multiview registration model to construct the denoiser, and a prior-conditioned SE(3)$^N$ variational lower bound is derived for denoising supervision. Extensive experiments on 3DMatch, ScanNet and ArkitScenes demonstrate that our approach achieves the superior registration accuracy and outstanding computational efficiency.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.09373">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.09373.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.09373.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A dynamic memory assignment strategy for dilation-based ICP algorithm on embedded GPUs</span>
        <span class="paper-authors">Qiong Chang, Weimin Wang, Junpei Zhong, Jun Miyazaki</span>
        <span class="paper-meta">Updated 2025-12-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">This paper proposes a memory-efficient optimization strategy for the high-performance point cloud registration algorithm VANICP, enabling lightweight execution on embedded GPUs with constrained hardware resources. VANICP is a recently published acceleration framework that significantly improves the computational efficiency of point-cloud-based applications. By transforming the global nearest neighbor search into a localized process through a dilation-based information propagation mechanism, VANICP greatly reduces the computational complexity of the NNS. However, its original implementation demands a considerable amount of memory, which restricts its deployment in resource-constrained environments such as embedded systems. To address this issue, we propose a GPU-oriented dynamic memory assignment strategy that optimizes the memory usage of the dilation operation. Furthermore, based on this strategy, we construct an enhanced version of the VANICP framework that achieves over 97% reduction in memory consumption while preserving the original performance. Source code is published on: https://github.com/changqiong/VANICP4Em.git.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.04996">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.04996.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.04996.pdf">
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
        <span class="paper-title">TALO: Pushing 3D Vision Foundation Models Towards Globally Consistent Online Reconstruction</span>
        <span class="paper-authors">Fengyi Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-12-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.02341">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.02341.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.02341.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">PointCNN++: Performant Convolution on Native Points</span>
        <span class="paper-authors">Lihan Li, Haofeng Zhong, Rui Bu, Mingchao Sun, Wenzheng Chen, Baoquan Chen, Yangyan Li</span>
        <span class="paper-meta">Updated 2025-12-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Existing convolutional learning methods for 3D point cloud data are divided into two paradigms: point-based methods that preserve geometric precision but often face performance challenges, and voxel-based methods that achieve high efficiency through quantization at the cost of geometric fidelity. This loss of precision is a critical bottleneck for tasks such as point cloud registration. We propose PointCNN++, a novel architectural design that fundamentally mitigates this precision-performance trade-off. It $\textbf{generalizes sparse convolution from voxels to points}$, treating voxel-based convolution as a specialized, degraded case of our more general point-based convolution. First, we introduce a point-centric convolution where the receptive field is centered on the original, high-precision point coordinates. Second, to make this high-fidelity operation performant, we design a computational strategy that operates $\textbf{natively}$ on points. We formulate the convolution on native points as a Matrix-Vector Multiplication and Reduction (MVMR) problem, for which we develop a dedicated, highly-optimized GPU kernel. Experiments demonstrate that PointCNN++ $\textbf{uses an order of magnitude less memory and is several times faster}$ than representative point-based methods. Furthermore, when used as a simple replacement for the voxel-based backbones it generalizes, it $\textbf{significantly improves point cloud registration accuracies while proving both more memory-efficient and faster}$. PointCNN++ shows that preserving geometric detail and achieving high performance are not mutually exclusive, paving the way for a new class of 3D learning with high fidelity and efficiency. Our code will be open sourced.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.23227">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.23227.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.23227.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Register Any Point: Scaling 3D Point Cloud Registration by Flow Matching</span>
        <span class="paper-authors">Yue Pan, Tao Sun, Liyuan Zhu, Lucas Nunes, Iro Armeni, Jens Behley, Cyrill Stachniss</span>
        <span class="paper-meta">Updated 2025-12-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Point cloud registration aligns multiple unposed point clouds into a common frame, and is a core step for 3D reconstruction and robot localization. In this work, we cast registration as conditional generation: a learned continuous, point-wise velocity field transports noisy points to a registered scene, from which the pose of each view is recovered. Unlike previous methods that conduct correspondence matching to estimate the transformation between a pair of point clouds and then optimize the pairwise transformations to realize multi-view registration, our model directly generates the registered point cloud. With a lightweight local feature extractor and test-time rigidity enforcement, our approach achieves state-of-the-art results on pairwise and multi-view registration benchmarks, particularly with low overlap, and generalizes across scales and sensor modalities. It further supports downstream tasks including relocalization, multi-robot SLAM, and multi-session map merging. Source code available at: https://github.com/PRBonn/RAP.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.01850">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.01850.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.01850.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LAHNet: Local Attentive Hashing Network for Point Cloud Registration</span>
        <span class="paper-authors">Wentao Qu, Xiaoshui Huang, Liang Xiao</span>
        <span class="paper-meta">Updated 2025-11-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Most existing learning-based point cloud descriptors for point cloud registration focus on perceiving local information of point clouds to generate distinctive features. However, a reasonable and broader receptive field is essential for enhancing feature distinctiveness. In this paper, we propose a Local Attentive Hashing Network for point cloud registration, called LAHNet, which introduces a local attention mechanism with the inductive bias of locality of convolution-like operators into point cloud descriptors. Specifically, a Group Transformer is designed to capture reasonable long-range context between points. This employs a linear neighborhood search strategy, Locality-Sensitive Hashing, enabling uniformly partitioning point clouds into non-overlapping windows. Meanwhile, an efficient cross-window strategy is adopted to further expand the reasonable feature receptive field. Furthermore, building on this effective windowing strategy, we propose an Interaction Transformer to enhance the feature interactions of the overlap regions within point cloud pairs. This computes an overlap matrix to match overlap regions between point cloud pairs by representing each window as a global signal. Extensive results demonstrate that LAHNet can learn robust and distinctive features, achieving significant registration results on real-world indoor and outdoor benchmarks.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.00927">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.00927.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.00927.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ViGG: Robust RGB-D Point Cloud Registration using Visual-Geometric Mutual Guidance</span>
        <span class="paper-authors">Congjia Chen, Shen Yan, Yufu Qu</span>
        <span class="paper-meta">Updated 2025-11-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Point cloud registration is a fundamental task in 3D vision. Most existing methods only use geometric information for registration. Recently proposed RGB-D registration methods primarily focus on feature fusion or improving feature learning, which limits their ability to exploit image information and hinders their practical applicability. In this paper, we propose ViGG, a robust RGB-D registration method using mutual guidance. First, we solve clique alignment in a visual-geometric combination form, employing a geometric guidance design to suppress ambiguous cliques. Second, to mitigate accuracy degradation caused by noise in visual matches, we propose a visual-guided geometric matching method that utilizes visual priors to determine the search space, enabling the extraction of high-quality, noise-insensitive correspondences. This mutual guidance strategy brings our method superior robustness, making it applicable for various RGB-D registration tasks. The experiments on 3DMatch, ScanNet and KITTI datasets show that our method outperforms recent state-of-the-art methods in both learning-free and learning-based settings. Code is available at https://github.com/ccjccjccj/ViGG.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.22908">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.22908.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.22908.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Aquas: Enhancing Domain Specialization through Holistic Hardware-Software Co-Optimization based on MLIR</span>
        <span class="paper-authors">Yuyang Zou et.al.</span>
        <span class="paper-meta">Updated 2025-11-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.22267">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.22267.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.22267.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Enhanced Landmark Detection Model in Pelvic Fluoroscopy using 2D/3D Registration Loss</span>
        <span class="paper-authors">Chou Mo et.al.</span>
        <span class="paper-meta">Updated 2025-11-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.21575">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.21575.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.21575.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">E-M3RF: An Equivariant Multimodal 3D Re-assembly Framework</span>
        <span class="paper-authors">Adeela Islam et.al.</span>
        <span class="paper-meta">Updated 2025-11-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.21422">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.21422.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.21422.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Dynamic-ICP: Doppler-Aware Iterative Closest Point Registration for Dynamic Scenes</span>
        <span class="paper-authors">Dong Wang et.al.</span>
        <span class="paper-meta">Updated 2025-11-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.20292">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.20292.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.20292.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MFM-point: Multi-scale Flow Matching for Point Cloud Generation</span>
        <span class="paper-authors">Petr Molodyk et.al.</span>
        <span class="paper-meta">Updated 2025-11-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.20041">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.20041.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.20041.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Efficient Transferable Optimal Transport via Min-Sliced Transport Plans</span>
        <span class="paper-authors">Xinran Liu et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.19741">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.19741.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.19741.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Structured Matching via Cost-Regularized Unbalanced Optimal Transport</span>
        <span class="paper-authors">Emanuele Pardini et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.19075">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.19075.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.19075.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Inverse Rendering for High-Genus Surface Meshes from Multi-View Images</span>
        <span class="paper-authors">Xiang Gao et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.18680">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.18680.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.18680.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Matching correlated VAR time series</span>
        <span class="paper-authors">Ernesto Araya et.al.</span>
        <span class="paper-meta">Updated 2025-11-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.18553">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.18553.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.18553.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ArticFlow: Generative Simulation of Articulated Mechanisms</span>
        <span class="paper-authors">Jiong Lin et.al.</span>
        <span class="paper-meta">Updated 2025-11-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.17883">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.17883.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.17883.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MorphSeek: Fine-grained Latent Representation-Level Policy Optimization for Deformable Image Registration</span>
        <span class="paper-authors">Runxun Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-11-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.17392">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.17392.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.17392.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SlsReuse: LLM-Powered Serverless Function Reuse</span>
        <span class="paper-authors">Jinfeng Wen et.al.</span>
        <span class="paper-meta">Updated 2025-11-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.17262">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.17262.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.17262.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">The Joint Gromov Wasserstein Objective for Multiple Object Matching</span>
        <span class="paper-authors">Aryan Tajmir Riahi et.al.</span>
        <span class="paper-meta">Updated 2025-11-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.16868">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.16868.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.16868.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">The MeerKAT Fornax Survey VI. The collapse of the galaxy HI Mass Function in Fornax</span>
        <span class="paper-authors">D. Kleiner et.al.</span>
        <span class="paper-meta">Updated 2025-11-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.15795">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.15795.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.15795.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Mesh RAG: Retrieval Augmentation for Autoregressive Mesh Generation</span>
        <span class="paper-authors">Xiatao Sun et.al.</span>
        <span class="paper-meta">Updated 2025-11-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.16807">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.16807.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.16807.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">CRISTAL: Real-time Camera Registration in Static LiDAR Scans using Neural Rendering</span>
        <span class="paper-authors">Joni Vanherck et.al.</span>
        <span class="paper-meta">Updated 2025-11-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.16349">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.16349.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.16349.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">US-X Complete: A Multi-Modal Approach to Anatomical 3D Shape Recovery</span>
        <span class="paper-authors">Miruna-Alexandra Gafencu et.al.</span>
        <span class="paper-meta">Updated 2025-11-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.15600">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.15600.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.15600.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Text2Loc++: Generalizing 3D Point Cloud Localization from Natural Language</span>
        <span class="paper-authors">Yan Xia et.al.</span>
        <span class="paper-meta">Updated 2025-11-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.15308">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.15308.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.15308.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A visual study of ICP variants for Lidar Odometry</span>
        <span class="paper-authors">Sebastian Dingler et.al.</span>
        <span class="paper-meta">Updated 2025-11-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.14919">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.14919.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.14919.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Silhouette-to-Contour Registration: Aligning Intraoral Scan Models with Cephalometric Radiographs</span>
        <span class="paper-authors">Yiyi Miao et.al.</span>
        <span class="paper-meta">Updated 2025-11-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.14343">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.14343.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.14343.pdf">
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
        <span class="paper-title">AtlasMorph: Learning conditional deformable templates for brain MRI</span>
        <span class="paper-authors">Marianne Rakic et.al.</span>
        <span class="paper-meta">Updated 2025-11-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.13609">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.13609.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.13609.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FUSE: A Flow-based Mapping Between Shapes</span>
        <span class="paper-authors">Lorenzo Olearo et.al.</span>
        <span class="paper-meta">Updated 2025-11-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.13431">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.13431.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.13431.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">An Evaluation of Representation Learning Methods in Particle Physics Foundation Models</span>
        <span class="paper-authors">Michael Chen et.al.</span>
        <span class="paper-meta">Updated 2025-11-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.12829">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.12829.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.12829.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Toward bilipshiz geometric models</span>
        <span class="paper-authors">Yonatan Sverdlov et.al.</span>
        <span class="paper-meta">Updated 2025-11-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.11735">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.11735.pdf">PDF</a>
          <a class="chip" href="https://github.com/yonatansverdlov/Toward-bilipshiz-geometric-models">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.11735.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">IPCD: Intrinsic Point-Cloud Decomposition</span>
        <span class="paper-authors">Shogo Sato et.al.</span>
        <span class="paper-meta">Updated 2025-11-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.09866">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.09866.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.09866.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">BronchOpt : Vision-Based Pose Optimization with Fine-Tuned Foundation Models for Accurate Bronchoscopy Navigation</span>
        <span class="paper-authors">Hongchao Shu et.al.</span>
        <span class="paper-meta">Updated 2025-11-12</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.09443">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.09443.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.09443.pdf">
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
          <a class="chip" href="https://github.com/url-kaist/multi-mapcher">Code</a>
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
        <span class="paper-title">MambaNetLK: Enhancing Colonoscopy Point Cloud Registration with Mamba</span>
        <span class="paper-authors">Linzhe Jiang et.al.</span>
        <span class="paper-meta">Updated 2025-10-31</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.00260">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.00260.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.00260.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Quality-controlled registration of urban MLS point clouds reducing drift effects by adaptive fragmentation</span>
        <span class="paper-authors">Marco Antonio Ortiz Rincon et.al.</span>
        <span class="paper-meta">Updated 2025-10-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.23416">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.23416.pdf">PDF</a>
          <a class="chip" href="https://github.com/Marco-23/SSC-Registration">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.23416.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Breaking the Static Assumption: A Dynamic-Aware LIO Framework Via Spatio-Temporal Normal Analysis</span>
        <span class="paper-authors">Chen Zhiqiang et.al.</span>
        <span class="paper-meta">Updated 2025-10-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.22313">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.22313.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.22313.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Registration is a Powerful Rotation-Invariance Learner for 3D Anomaly Detection</span>
        <span class="paper-authors">Yuyang Yu et.al.</span>
        <span class="paper-meta">Updated 2025-10-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.16865">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.16865.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.16865.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Novel point cloud registration approach for noninvasive patient specific estimation of leaflet strain from 3D images of heart valves</span>
        <span class="paper-authors">Wensi Wu et.al.</span>
        <span class="paper-meta">Updated 2025-10-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.06578">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.06578.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.06578.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DINOReg: Strong Point Cloud Registration with Vision Foundation Model</span>
        <span class="paper-authors">Congjia Chen et.al.</span>
        <span class="paper-meta">Updated 2025-09-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.24370">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.24370.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.24370.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Robust Partial 3D Point Cloud Registration via Confidence Estimation under Global Context</span>
        <span class="paper-authors">Yongqiang Wang et.al.</span>
        <span class="paper-meta">Updated 2025-09-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.24275">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.24275.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.24275.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Skeleton-based Robust Registration Framework for Corrupted 3D Point Clouds</span>
        <span class="paper-authors">Yongqiang Wang et.al.</span>
        <span class="paper-meta">Updated 2025-09-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.24273">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.24273.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.24273.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">AssemblyHands-X: Modeling 3D Hand-Body Coordination for Understanding Bimanual Human Activities</span>
        <span class="paper-authors">Tatsuro Banno et.al.</span>
        <span class="paper-meta">Updated 2025-09-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.23888">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.23888.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.23888.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">An Adaptive ICP LiDAR Odometry Based on Reliable Initial Pose</span>
        <span class="paper-authors">Qifeng Wang et.al.</span>
        <span class="paper-meta">Updated 2025-09-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.22058">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.22058.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.22058.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Building Information Models to Robot-Ready Site Digital Twins (BIM2RDT): An Agentic AI Safety-First Framework</span>
        <span class="paper-authors">Reza Akhavian et.al.</span>
        <span class="paper-meta">Updated 2025-09-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.20705">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.20705.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.20705.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Human-Interpretable Uncertainty Explanations for Point Cloud Registration</span>
        <span class="paper-authors">Johannes A. Gaus et.al.</span>
        <span class="paper-meta">Updated 2025-09-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.18786">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.18786.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.18786.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Self-Supervised Cross-Modal Learning for Image-to-Point Cloud Registration</span>
        <span class="paper-authors">Xingmei Wang et.al.</span>
        <span class="paper-meta">Updated 2025-09-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.15882">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.15882.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.15882.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FingerSplat: Contactless Fingerprint 3D Reconstruction and Generation based on 3D Gaussian Splatting</span>
        <span class="paper-authors">Yuwei Jia et.al.</span>
        <span class="paper-meta">Updated 2025-09-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.15648">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.15648.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.15648.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MATTER: Multiscale Attention for Registration Error Regression</span>
        <span class="paper-authors">Shipeng Liu et.al.</span>
        <span class="paper-meta">Updated 2025-09-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.12924">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.12924.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.12924.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DisorientLiDAR: Physical Attacks on LiDAR-based Localization</span>
        <span class="paper-authors">Yizhen Lao et.al.</span>
        <span class="paper-meta">Updated 2025-09-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.12595">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.12595.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.12595.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">iMatcher: Improve matching in point cloud registration via local-to-global geometric consistency learning</span>
        <span class="paper-authors">Karim Slimani et.al.</span>
        <span class="paper-meta">Updated 2025-09-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.08982">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.08982.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.08982.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Unidimensional semi-discrete partial optimal transport</span>
        <span class="paper-authors">Adrien Cances et.al.</span>
        <span class="paper-meta">Updated 2025-09-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.08799">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.08799.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.08799.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A Robust Approach for LiDAR-Inertial Odometry Without Sensor-Specific Modeling</span>
        <span class="paper-authors">Meher V. R. Malladi et.al.</span>
        <span class="paper-meta">Updated 2025-09-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.06593">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.06593.pdf">PDF</a>
          <a class="chip" href="https://github.com/PRBonn/rko_lio">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.06593.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Cross3DReg: Towards a Large-scale Real-world Cross-source Point Cloud Registration Benchmark</span>
        <span class="paper-authors">Zongyi Xu et.al.</span>
        <span class="paper-meta">Updated 2025-09-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.06456">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.06456.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.06456.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DCReg: Decoupled Characterization for Efficient Degenerate LiDAR Registration</span>
        <span class="paper-authors">Xiangcheng Hu et.al.</span>
        <span class="paper-meta">Updated 2025-09-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.06285">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.06285.pdf">PDF</a>
          <a class="chip" href="https://github.com/JokerJohn/DCReg">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.06285.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Surfel-based 3D Registration with Equivariant SE(3) Features</span>
        <span class="paper-authors">Xueyang Kang et.al.</span>
        <span class="paper-meta">Updated 2025-08-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2508.20789">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2508.20789.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2508.20789.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Robust Point Cloud Registration via Geometric Overlapping Guided Rotation Search</span>
        <span class="paper-authors">Zhao Zheng et.al.</span>
        <span class="paper-meta">Updated 2025-08-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2508.17427">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2508.17427.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2508.17427.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GPL-SLAM: A Laser SLAM Framework with Gaussian Process Based Extended Landmarks</span>
        <span class="paper-authors">Ali Emre Balcı et.al.</span>
        <span class="paper-meta">Updated 2025-08-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2508.16459">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2508.16459.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2508.16459.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">4D Virtual Imaging Platform for Dynamic Joint Assessment via Uni-Plane X-ray and 2D-3D Registration</span>
        <span class="paper-authors">Hao Tang et.al.</span>
        <span class="paper-meta">Updated 2025-08-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2508.16138">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2508.16138.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2508.16138.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Fast globally optimal Truncated Least Squares point cloud registration with fixed rotation axis</span>
        <span class="paper-authors">Ivo Ivanov et.al.</span>
        <span class="paper-meta">Updated 2025-08-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2508.15613">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2508.15613.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2508.15613.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">PKSS-Align: Robust Point Cloud Registration on Pre-Kendall Shape Space</span>
        <span class="paper-authors">Chenlei Lv et.al.</span>
        <span class="paper-meta">Updated 2025-08-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2508.04286">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2508.04286.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2508.04286.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A Multi-Level Similarity Approach for Single-View Object Grasping: Matching, Planning, and Fine-Tuning</span>
        <span class="paper-authors">Hao Chen et.al.</span>
        <span class="paper-meta">Updated 2025-07-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.11938">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.11938.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.11938.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Diff$^2$I2P: Differentiable Image-to-Point Cloud Registration with Diffusion Prior</span>
        <span class="paper-authors">Juncheng Mu et.al.</span>
        <span class="paper-meta">Updated 2025-07-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.06651">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.06651.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.06651.pdf">
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
        <span class="paper-title">Lidar Variability: A Novel Dataset and Comparative Study of Solid-State and Spinning Lidars</span>
        <span class="paper-authors">Doumegna Mawuto Koudjo Felix et.al.</span>
        <span class="paper-meta">Updated 2025-07-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.04321">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.04321.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.04321.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">TurboReg: TurboClique for Robust and Efficient Point Cloud Registration</span>
        <span class="paper-authors">Shaocheng Yan et.al.</span>
        <span class="paper-meta">Updated 2025-07-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.01439">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.01439.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.01439.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">CA-I2P: Channel-Adaptive Registration Network with Global Optimal Selection</span>
        <span class="paper-authors">Zhixin Cheng et.al.</span>
        <span class="paper-meta">Updated 2025-06-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.21364">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.21364.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.21364.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Correspondence-Free Multiview Point Cloud Registration via Depth-Guided Joint Optimisation</span>
        <span class="paper-authors">Yiran Zhou et.al.</span>
        <span class="paper-meta">Updated 2025-06-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.18922">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.18922.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.18922.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">BCRNet: Enhancing Landmark Detection in Laparoscopic Liver Surgery via Bezier Curve Refinement</span>
        <span class="paper-authors">Qian Li et.al.</span>
        <span class="paper-meta">Updated 2025-06-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.15279">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.15279.pdf">PDF</a>
          <a class="chip" href="https://github.com/jinlab-imvr/BCRNet">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.15279.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MT-PCR: A Hybrid Mamba-Transformer with Spatial Serialization for Hierarchical Point Cloud Registration</span>
        <span class="paper-authors">Bingxi Liu et.al.</span>
        <span class="paper-meta">Updated 2025-06-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.13183">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.13183.pdf">PDF</a>
          <a class="chip" href="https://github.com/an1iu/MT-PCR">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.13183.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Robust Filtering -- Novel Statistical Learning and Inference Algorithms with Applications</span>
        <span class="paper-authors">Aamir Hussain Chughtai et.al.</span>
        <span class="paper-meta">Updated 2025-06-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.11530">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.11530.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.11530.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Accurate and efficient zero-shot 6D pose estimation with frozen foundation models</span>
        <span class="paper-authors">Andrea Caraffa et.al.</span>
        <span class="paper-meta">Updated 2025-06-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.09784">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.09784.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.09784.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Rectified Point Flow: Generic Point Cloud Pose Estimation</span>
        <span class="paper-authors">Tao Sun et.al.</span>
        <span class="paper-meta">Updated 2025-06-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.05282">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.05282.pdf">PDF</a>
          <a class="chip" href="https://github.com/GradientSpaces/Rectified-Point-Flow">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.05282.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Guiding Registration with Emergent Similarity from Pre-Trained Diffusion Models</span>
        <span class="paper-authors">Nurislam Tursynbek et.al.</span>
        <span class="paper-meta">Updated 2025-06-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.02419">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.02419.pdf">PDF</a>
          <a class="chip" href="https://github.com/uncbiag/dgir">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.02419.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A 3D Mobile Crowdsensing Framework for Sustainable Urban Digital Twins</span>
        <span class="paper-authors">Taku Yamazaki et.al.</span>
        <span class="paper-meta">Updated 2025-05-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.24348">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.24348.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.24348.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A Coarse to Fine 3D LiDAR Localization with Deep Local Features for Long Term Robot Navigation in Large Environments</span>
        <span class="paper-authors">Míriam Máximo et.al.</span>
        <span class="paper-meta">Updated 2025-05-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.18340">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.18340.pdf">PDF</a>
          <a class="chip" href="https://github.com/miriammaximo/mcl-dlf">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.18340.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">D-LIO: 6DoF Direct LiDAR-Inertial Odometry based on Simultaneous Truncated Distance Field Mapping</span>
        <span class="paper-authors">Lucia Coto-Elena et.al.</span>
        <span class="paper-meta">Updated 2025-05-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.16726">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.16726.pdf">PDF</a>
          <a class="chip" href="https://github.com/robotics-upo/D-LIO">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.16726.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Cross-modal feature fusion for robust point cloud registration with ambiguous geometry</span>
        <span class="paper-authors">Zhaoyi Wang et.al.</span>
        <span class="paper-meta">Updated 2025-05-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.13088">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.13088.pdf">PDF</a>
          <a class="chip" href="https://github.com/zhaoyiww/coff">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.13088.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MonoMobility: Zero-Shot 3D Mobility Analysis from Monocular Videos</span>
        <span class="paper-authors">Hongyi Zhou et.al.</span>
        <span class="paper-meta">Updated 2025-05-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.11868">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.11868.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.11868.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">VGC-RIO: A Tightly Integrated Radar-Inertial Odometry with Spatial Weighted Doppler Velocity and Local Geometric Constrained RCS Histograms</span>
        <span class="paper-authors">Jianguang Xiang et.al.</span>
        <span class="paper-meta">Updated 2025-05-15</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.09103">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.09103.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.09103.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">3D Hand-Eye Calibration for Collaborative Robot Arm: Look at Robot Base Once</span>
        <span class="paper-authors">Leihui Li et.al.</span>
        <span class="paper-meta">Updated 2025-05-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.21619">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.21619.pdf">PDF</a>
          <a class="chip" href="https://github.com/leihui6/lrbo">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.21619.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">An Efficient Method for Accurate Pose Estimation and Error Correction of Cuboidal Objects</span>
        <span class="paper-authors">Utsav Rai et.al.</span>
        <span class="paper-meta">Updated 2025-05-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.04962">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.04962.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.04962.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FA-KPConv: Introducing Euclidean Symmetries to KPConv via Frame Averaging</span>
        <span class="paper-authors">Ali Alawieh et.al.</span>
        <span class="paper-meta">Updated 2025-05-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.04485">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.04485.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.04485.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Registration of 3D Point Sets Using Exponential-based Similarity Matrix</span>
        <span class="paper-authors">Ashutosh Singandhupe et.al.</span>
        <span class="paper-meta">Updated 2025-05-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.04540">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.04540.pdf">PDF</a>
          <a class="chip" href="https://github.com/aralab-unr/esm_icp">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.04540.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Matching Distance and Geometric Distribution Aided Learning Multiview Point Cloud Registration</span>
        <span class="paper-authors">Shiqi Li et.al.</span>
        <span class="paper-meta">Updated 2025-05-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.03692">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.03692.pdf">PDF</a>
          <a class="chip" href="https://github.com/shi-qi-li/mdgd">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.03692.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Enhancing Lidar Point Cloud Sampling via Colorization and Super-Resolution of Lidar Imagery</span>
        <span class="paper-authors">Sier Ha et.al.</span>
        <span class="paper-meta">Updated 2025-05-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.02049">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.02049.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.02049.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Multiview Point Cloud Registration via Optimization in an Autoencoder Latent Space</span>
        <span class="paper-authors">Luc Vedrenne et.al.</span>
        <span class="paper-meta">Updated 2025-04-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.21467">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.21467.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.21467.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Landmark-Free Preoperative-to-Intraoperative Registration in Laparoscopic Liver Resection</span>
        <span class="paper-authors">Jun Zhou et.al.</span>
        <span class="paper-meta">Updated 2025-04-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.15152">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.15152.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.15152.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Investigating Vision-Language Model for Point Cloud-based Vehicle Classification</span>
        <span class="paper-authors">Yiqiao Li et.al.</span>
        <span class="paper-meta">Updated 2025-04-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.08154">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.08154.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.08154.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A Convex and Global Solution for the P$n$P Problem in 2D Forward-Looking Sonar</span>
        <span class="paper-authors">Jiayi Su et.al.</span>
        <span class="paper-meta">Updated 2025-04-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.04445">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.04445.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.04445.pdf">
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
        <span class="paper-title">FACT: Multinomial Misalignment Classification for Point Cloud Registration</span>
        <span class="paper-authors">Ludvig Dillén et.al.</span>
        <span class="paper-meta">Updated 2025-04-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.06627">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.06627.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.06627.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">IMPACT: A Generic Semantic Loss for Multimodal Medical Image Registration</span>
        <span class="paper-authors">Valentin Boussot et.al.</span>
        <span class="paper-meta">Updated 2025-04-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.24121">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.24121.pdf">PDF</a>
          <a class="chip" href="https://github.com/vboussot/impactloss">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.24121.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Bridge 2D-3D: Uncertainty-aware Hierarchical Registration Network with Domain Alignment</span>
        <span class="paper-authors">Zhixin Cheng et.al.</span>
        <span class="paper-meta">Updated 2025-04-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.01641">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.01641.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.01641.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">R2LDM: An Efficient 4D Radar Super-Resolution Framework Leveraging Diffusion Model</span>
        <span class="paper-authors">Boyuan Zheng et.al.</span>
        <span class="paper-meta">Updated 2025-03-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.17097">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.17097.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.17097.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Three-dimensional Reconstruction of the Lumbar Spine with Submillimeter Accuracy Using Biplanar X-ray Images</span>
        <span class="paper-authors">Wanxin Yu et.al.</span>
        <span class="paper-meta">Updated 2025-03-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.14573">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.14573.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.14573.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MT-PCR: Leveraging Modality Transformation for Large-Scale Point Cloud Registration with Limited Overlap</span>
        <span class="paper-authors">Yilong Wu et.al.</span>
        <span class="paper-meta">Updated 2025-03-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.12833">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.12833.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.12833.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Unlocking Generalization Power in LiDAR Point Cloud Registration</span>
        <span class="paper-authors">Zhenxuan Zeng et.al.</span>
        <span class="paper-meta">Updated 2025-03-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.10149">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.10149.pdf">PDF</a>
          <a class="chip" href="https://github.com/peakpang/ugp">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.10149.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">BUFFER-X: Towards Zero-Shot Point Cloud Registration in Diverse Scenes</span>
        <span class="paper-authors">Minkyun Seo et.al.</span>
        <span class="paper-meta">Updated 2025-03-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.07940">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.07940.pdf">PDF</a>
          <a class="chip" href="https://github.com/mit-spark/buffer-x">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.07940.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SANDRO: a Robust Solver with a Splitting Strategy for Point Cloud Registration</span>
        <span class="paper-authors">Michael Adlerstein et.al.</span>
        <span class="paper-meta">Updated 2025-03-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.07743">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.07743.pdf">PDF</a>
          <a class="chip" href="https://github.com/iit-DLSLab/SANDRO">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.07743.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">HybridReg: Robust 3D Point Cloud Registration with Hybrid Motions</span>
        <span class="paper-authors">Keyu Du et.al.</span>
        <span class="paper-meta">Updated 2025-03-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.07019">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.07019.pdf">PDF</a>
          <a class="chip" href="https://github.com/hxwork/HybridReg_PyTorch">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.07019.pdf">
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
        <span class="paper-title">HyperGCT: A Dynamic Hyper-GNN-Learned Geometric Constraint for 3D Registration</span>
        <span class="paper-authors">Xiyu Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-03-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.02195">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.02195.pdf">PDF</a>
          <a class="chip" href="https://github.com/zhangxy0517/HyperGCT">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.02195.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Semantic-ICP: Iterative Closest Point for Non-rigid Multi-Organ Point Cloud Registration</span>
        <span class="paper-authors">Wanwen Chen et.al.</span>
        <span class="paper-meta">Updated 2025-03-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.00972">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.00972.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.00972.pdf">
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
        <span class="paper-title">Occlusion-aware Non-Rigid Point Cloud Registration via Unsupervised Neural Deformation Correntropy</span>
        <span class="paper-authors">Mingyang Zhao et.al.</span>
        <span class="paper-meta">Updated 2025-02-15</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2502.10704">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2502.10704.pdf">PDF</a>
          <a class="chip" href="https://github.com/zikai1/oareg">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2502.10704.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Fully-Geometric Cross-Attention for Point Cloud Registration</span>
        <span class="paper-authors">Weijie Wang et.al.</span>
        <span class="paper-meta">Updated 2025-02-12</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2502.08285">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2502.08285.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2502.08285.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
</section>
