---
layout: default
title: SLAM
---

<section class="topic-hero" style="--accent: #ffb347;">
  <div>
    <p class="eyebrow">Topic</p>
    <h1>SLAM</h1>
    <p class="topic-lede">Updated 2026.04.09 · 234 papers</p>
  </div>
  <a class="btn ghost" href="../index.html#topics">← Back to topics</a>
</section>

<section class="paper-grid">
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">VGGT-SLAM++</span>
        <span class="paper-authors">Avilasha Mandal, Rajesh Kumar, Sudarshan Sunil Harithas, Chetan Arora</span>
        <span class="paper-meta">Updated 2026-04-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We introduce VGGT-SLAM++, a complete visual SLAM system that leverages the geometry-rich outputs of the Visual Geometry Grounded Transformer (VGGT). The system comprises a visual odometry (front-end) fusing the VGGT feed-forward transformer and a Sim(3) solution, a Digital Elevation Map (DEM)-based graph construction module, and a back-end that jointly enable accurate large-scale mapping with bounded memory. While prior transformer-based SLAM pipelines such as VGGT-SLAM rely primarily on sparse loop closures or global Sim(3) manifold constraints - allowing short-horizon pose drift - VGGT-SLAM++ restores high-cadence local bundle adjustment (LBA) through a spatially corrective back-end. For each VGGT submap, we construct a dense planar-canonical DEM, partition it into patches, and compute their DINOv2 embeddings to integrate the submap into a covisibility graph. Spatial neighbors are retrieved using a Visual Place Recognition (VPR) module within the covisibility window, triggering frequent local optimization that stabilizes trajectories. Across standard SLAM benchmarks, VGGT-SLAM++ achieves state-of-the-art accuracy, substantially reducing short-term drift, accelerating graph convergence, and maintaining global consistency with compact DEM tiles and sublinear retrieval.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.06830">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.06830.pdf">PDF</a>
          <a class="chip" href="https://github.com/MIT-SPARK/VGGT-SLAM">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.06830.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DINO-VO: Learning Where to Focus for Enhanced State Estimation</span>
        <span class="paper-authors">Qi Chen, Guanghao Li, Sijia Hu, Xin Gao, Junpeng Ma, Xiangyang Xue, Jian Pu</span>
        <span class="paper-meta">Updated 2026-04-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We present DINO Patch Visual Odometry (DINO-VO), an end-to-end monocular visual odometry system with strong scene generalization. Current Visual Odometry (VO) systems often rely on heuristic feature extraction strategies, which can degrade accuracy and robustness, particularly in large-scale outdoor environments. DINO-VO addresses these limitations by incorporating a differentiable adaptive patch selector into the end-to-end pipeline, improving the quality of extracted patches and enhancing generalization across diverse datasets. Additionally, our system integrates a multi-task feature extraction module with a differentiable bundle adjustment (BA) module that leverages inverse depth priors, enabling the system to learn and utilize appearance and geometric information effectively. This integration bridges the gap between feature learning and state estimation. Extensive experiments on the TartanAir, KITTI, Euroc, and TUM datasets demonstrate that DINO-VO exhibits strong generalization across synthetic, indoor, and outdoor environments, achieving state-of-the-art tracking accuracy.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.04055">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.04055.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.04055.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ViBA: Implicit Bundle Adjustment with Geometric and Temporal Consistency for Robust Visual Matching</span>
        <span class="paper-authors">Xiaoji Niu, Yuqing Wang, Yan Wang, Hailiang Tang, Tisheng Zhang</span>
        <span class="paper-meta">Updated 2026-04-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Most existing image keypoint detection and description methods rely on datasets with accurate pose and depth annotations, limiting scalability and generalization, and often degrading navigation and localization performance. We propose ViBA, a sustainable learning framework that integrates geometric optimization with feature learning for continuous online training on unconstrained video streams. Embedded in a standard visual odometry pipeline, it consists of an implicitly differentiable geometric residual framework: (i) an initial tracking network for inter-frame correspondences, (ii) depth-based outlier filtering, and (iii) differentiable global bundle adjustment that jointly refines camera poses and feature positions by minimizing reprojection errors. By combining geometric consistency from BA with long-term temporal consistency across frames, ViBA enforces stable and accurate feature representations. We evaluate ViBA on EuRoC and UMA datasets. Compared with state-of-the-art methods such as SuperPoint+SuperGlue, ALIKED, and LightGlue, ViBA reduces mean absolute translation error (ATE) by 12-18% and absolute rotation error (ARE) by 5-10% across sequences, while maintaining real-time inference speeds (FPS 36-91). When evaluated on unseen sequences, it retains over 90% localization accuracy, demonstrating robust generalization. These results show that ViBA supports continuous online learning with geometric and temporal consistency, consistently improving navigation and localization in real-world scenarios.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.03377">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.03377.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.03377.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">HyVGGT-VO: Tightly Coupled Hybrid Dense Visual Odometry with Feed-Forward Models</span>
        <span class="paper-authors">Junxiang Pan, Lipu Zhou, Baojie Chen</span>
        <span class="paper-meta">Updated 2026-04-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Dense visual odometry (VO), which provides pose estimation and dense 3D reconstruction, serves as the cornerstone for applications ranging from robotics to augmented reality. Recently, feed-forward models have demonstrated remarkable capabilities in dense mapping. However, when these models are used in dense visual SLAM systems, their heavy computational burden restricts them to yielding sparse pose outputs at keyframes while still failing to achieve real-time pose estimation. In contrast, traditional sparse methods provide high computational efficiency and high-frequency pose outputs, but lack the capability for dense reconstruction. To address these limitations, we propose HyVGGT-VO, a novel framework that combines the computational efficiency of sparse VO with the dense reconstruction capabilities of feed-forward models. To the best of our knowledge, this is the first work to tightly couple a traditional VO framework with VGGT, a state-of-the-art feed-forward model. Specifically, we design an adaptive hybrid tracking frontend that dynamically switches between traditional optical flow and the VGGT tracking head to ensure robustness. Furthermore, we introduce a hierarchical optimization framework that jointly refines VO poses and the scale of VGGT predictions to ensure global scale consistency. Our approach achieves an approximately 5x processing speedup compared to existing VGGT-based methods, while reducing the average trajectory error by 85% on the indoor EuRoC dataset and 12% on the outdoor KITTI benchmark. Our code will be publicly available upon acceptance. Project page: https://geneta2580.github.io/HyVGGT-VO.io.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2604.02107">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2604.02107.pdf">PDF</a>
          <a class="chip" href="https://github.com/Geneta2580/HyVGGT-VO">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2604.02107.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Image-Conditioned Adaptive Parameter Tuning for Visual Odometry Frontends</span>
        <span class="paper-authors">Simone Nascivera, Leonard Bauersfeld, Jeff Delaune, Davide Scaramuzza</span>
        <span class="paper-meta">Updated 2026-03-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Resource-constrained autonomous robots rely on sparse direct and semi-direct visual-(inertial)-odometry (VO) pipelines, as they provide a favorable tradeoff between accuracy, robustness, and computational cost. However, the performance of most systems depends critically on hand-tuned hyperparameters governing feature detection, tracking, and outlier rejection. These parameters are typically fixed during deployment, even though their optimal values vary with scene characteristics such as texture density, illumination, motion blur, and sensor noise, leading to brittle performance in real-world environments. We propose the first image-conditioned reinforcement learning framework for online tuning of VO frontend parameters, effectively embedding the expert into the system. Our key idea is to formulate the frontend configuration as a sequential decision-making problem and learn a policy that directly maps visual input to feature detection and tracking parameters. The policy uses a lightweight texture-aware CNN encoder and a privileged critic during training. Unlike prior RL-based approaches that rely solely on internal VO statistics, our method observes the image content and proactively adapts parameters before tracking degrades. Experiments on TartanAirV2 and TUM RGB-D show 3x longer feature tracks and 3x lower computational cost, despite training entirely in simulation.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.21785">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.21785.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.21785.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Benchmarking Visual Feature Representations for LiDAR-Inertial-Visual Odometry Under Challenging Conditions</span>
        <span class="paper-authors">Eunseon Choi, Junwoo Hong, Daehan Lee, Sanghyun Park, Hyunyoung Jo, Sunyoung Kim, Changho Kang, Seongsam Kim, Yonghan Jung, Jungwook Park, Seul Koo, Soohee Han</span>
        <span class="paper-meta">Updated 2026-03-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Accurate localization in autonomous driving is critical for successful missions including environmental mapping and survivor searches. In visually challenging environments, including low-light conditions, overexposure, illumination changes, and high parallax, the performance of conventional visual odometry methods significantly degrade undermining robust robotic navigation. Researchers have recently proposed LiDAR-inertial-visual odometry (LIVO) frameworks, that integrate LiDAR, IMU, and camera sensors, to address these challenges. This paper extends the FAST-LIVO2-based framework by introducing a hybrid approach that integrates direct photometric methods with descriptor-based feature matching. For the descriptor-based feature matching, this work proposes pairs of ORB with the Hamming distance, SuperPoint with SuperGlue, SuperPoint with LightGlue, and XFeat with the mutual nearest neighbor. The proposed configurations are benchmarked by accuracy, computational cost, and feature tracking stability, enabling a quantitative comparison of the adaptability and applicability of visual descriptors. The experimental results reveal that the proposed hybrid approach outperforms the conventional sparse-direct method. Although the sparse-direct method often fails to converge in regions where photometric inconsistency arises due to illumination changes, the proposed approach still maintains robust performance under the same conditions. Furthermore, the hybrid approach with learning-based descriptors enables robust and reliable visual state estimation across challenging environments.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.18589">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.18589.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.18589.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Full Stack Navigation, Mapping, and Planning for the Lunar Autonomy Challenge</span>
        <span class="paper-authors">Adam Dai, Asta Wu, Keidai Iiyama, Guillem Casadesus Vila, Kaila Coimbra, Thomas Deng, Grace Gao</span>
        <span class="paper-meta">Updated 2026-03-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We present a modular, full-stack autonomy system for lunar surface navigation and mapping developed for the Lunar Autonomy Challenge. Operating in a GNSS-denied, visually challenging environment, our pipeline integrates semantic segmentation, stereo visual odometry, pose graph SLAM with loop closures, and layered planning and control. We leverage lightweight learning-based perception models for real-time segmentation and feature tracking and use a factor-graph backend to maintain globally consistent localization. High-level waypoint planning is designed to promote mapping coverage while encouraging frequent loop closures, and local motion planning uses arc sampling with geometric obstacle checks for efficient, reactive control. We evaluate our approach in the competition&#x27;s high-fidelity lunar simulator, demonstrating centimeter-level localization accuracy, high-fidelity map generation, and strong repeatability across random seeds and rock distributions. Our solution achieved first place in the final competition evaluation.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.17232">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.17232.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.17232.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Industrial cuVSLAM Benchmark &amp; Integration</span>
        <span class="paper-authors">Charbel Abi Hana, Kameel Amareen, Mohamad Mostafa, Dmitry Slepichev, Hesam Rabeti, Zheng Wang, Mihir Acharya, Anthony Rizk</span>
        <span class="paper-meta">Updated 2026-03-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">This work presents a comprehensive benchmark evaluation of visual odometry (VO) and visual SLAM (VSLAM) systems for mobile robot navigation in real-world logistical environments. We compare multiple visual odometry approaches across controlled trajectories covering translational, rotational, and mixed motion patterns, as well as a large-scale production facility dataset spanning approximately 1.7 km. Performance is evaluated using Absolute Pose Error (APE) against ground truth from a Vicon motion capture system and a LiDAR-based SLAM reference. Our results show that a hybrid stack combining the cuVSLAM front-end with a custom SLAM back-end achieves the strongest mapping accuracy, motivating a deeper integration of cuVSLAM as the core VO component in our robotics stack. We further validate this integration by deploying and testing the cuVSLAM-based VO stack on an NVIDIA Jetson platform.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.16240">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.16240.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.16240.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Edged USLAM: Edge-Aware Event-Based SLAM with Learning-Based Depth Priors</span>
        <span class="paper-authors">Şebnem Sarıözkan, Hürkan Şahin, Olaya Álvarez-Tuñón, Erdal Kayacan</span>
        <span class="paper-meta">Updated 2026-03-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Conventional visual simultaneous localization and mapping (SLAM) algorithms often fail under rapid motion, low illumination, or abrupt lighting transitions due to motion blur and limited dynamic range. Event cameras mitigate these issues with high temporal resolution and high dynamic range (HDR), but their sparse, asynchronous outputs complicate feature extraction and integration with other sensors; e.g. inertial measurement units (IMUs) and standard cameras. We present Edged USLAM, a hybrid visual-inertial system that extends Ultimate SLAM (USLAM) with an edge-aware front-end and a lightweight depth module. The frontend enhances event frames for robust feature tracking and nonlinear motion compensation, while the depth module provides coarse, region-of-interest (ROI)-based scene depth to improve motion compensation and scale consistency. Evaluations across public benchmarks and real-world unmanned air vehicle (UAV) flights demonstrate that performance varies significantly by scenario. For instance, event-only methods like point-line event-based visual-inertial odometry (PL-EVIO) or learning-based pipelines such as deep event-based visual odometry (DEVO) excel in highly aggressive or extreme HDR conditions. In contrast, Edged USLAM provides superior stability and minimal drift in slow or structured trajectories, ensuring consistently accurate localization on real flights under challenging illumination. These findings highlight the complementary strengths of event-only, learning-based, and hybrid approaches, while positioning Edged USLAM as a robust solution for diverse aerial navigation tasks.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.08150">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.08150.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.08150.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Motion-aware Event Suppression for Event Cameras</span>
        <span class="paper-authors">Roberto Pellerito, Nico Messikommer, Giovanni Cioffi, Marco Cannici, Davide Scaramuzza</span>
        <span class="paper-meta">Updated 2026-02-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">In this work, we introduce the first framework for Motion-aware Event Suppression, which learns to filter events triggered by IMOs and ego-motion in real time. Our model jointly segments IMOs in the current event stream while predicting their future motion, enabling anticipatory suppression of dynamic events before they occur. Our lightweight architecture achieves 173 Hz inference on consumer-grade GPUs with less than 1 GB of memory usage, outperforming previous state-of-the-art methods on the challenging EVIMO benchmark by 67\% in segmentation accuracy while operating at a 53\% higher inference rate. Moreover, we demonstrate significant benefits for downstream applications: our method accelerates Vision Transformer inference by 83\% via token pruning and improves event-based visual odometry accuracy, reducing Absolute Trajectory Error (ATE) by 13\%.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.23204">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.23204.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.23204.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">OpenVO: Open-World Visual Odometry with Temporal Dynamics Awareness</span>
        <span class="paper-authors">Phuc D. A. Nguyen, Anh N. Nhu, Ming C. Lin</span>
        <span class="paper-meta">Updated 2026-02-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We introduce OpenVO, a novel framework for Open-world Visual Odometry (VO) with temporal awareness under limited input conditions. OpenVO effectively estimates real-world-scale ego-motion from monocular dashcam footage with varying observation rates and uncalibrated cameras, enabling robust trajectory dataset construction from rare driving events recorded in dashcam. Existing VO methods are trained on fixed observation frequency (e.g., 10Hz or 12Hz), completely overlooking temporal dynamics information. Many prior methods also require calibrated cameras with known intrinsic parameters. Consequently, their performance degrades when (1) deployed under unseen observation frequencies or (2) applied to uncalibrated cameras. These significantly limit their generalizability to many downstream tasks, such as extracting trajectories from dashcam footage. To address these challenges, OpenVO (1) explicitly encodes temporal dynamics information within a two-frame pose regression framework and (2) leverages 3D geometric priors derived from foundation models. We validate our method on three major autonomous-driving benchmarks - KITTI, nuScenes, and Argoverse 2 - achieving more than 20 performance improvement over state-of-the-art approaches. Under varying observation rate settings, our method is significantly more robust, achieving 46%-92% lower errors across all metrics. These results demonstrate the versatility of OpenVO for real-world 3D reconstruction and diverse downstream applications.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.19035">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.19035.pdf">PDF</a>
          <a class="chip" href="https://github.com/Ufere/Assingment_1">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.19035.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">UAV-SEAD: State Estimation Anomaly Dataset for UAVs</span>
        <span class="paper-authors">Aykut Kabaoglu, Sanem Sariel</span>
        <span class="paper-meta">Updated 2026-02-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Accurate state estimation in Unmanned Aerial Vehicles (UAVs) is crucial for ensuring reliable and safe operation, as anomalies occurring during mission execution may induce discrepancies between expected and observed system behaviors, thereby compromising mission success or posing potential safety hazards. It is essential to continuously monitor and detect such conditions in order to ensure a timely response and maintain system reliability. In this work, we focus on UAV state estimation anomalies and provide a large-scale real-world UAV dataset to facilitate research aimed at improving the development of anomaly detection. Unlike existing datasets that primarily rely on injected faults into simulated data, this dataset comprises 1396 real flight logs totaling over 52 hours of flight time, collected across diverse indoor and outdoor environments using a collection of PX4-based UAVs equipped with a variety of sensor configurations. The dataset comprises both normal and anomalous flights without synthetic manipulation, making it uniquely suitable for realistic anomaly detection tasks. A structured classification is proposed that categorizes UAV state estimation anomalies into four classes: mechanical and electrical, external position, global position, and altitude anomalies. These classifications reflect collective, contextual, and outlier anomalies observed in multivariate sensor data streams, including IMU, GPS, barometer, magnetometer, distance sensors, visual odometry, and optical flow, that can be found in the PX4 logging mechanism. It is anticipated that this dataset will play a key role in the development, training, and evaluation of anomaly detection and isolation systems to address the critical gap in UAV reliability research.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.13900">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.13900.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.13900.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GSO-SLAM: Bidirectionally Coupled Gaussian Splatting and Direct Visual Odometry</span>
        <span class="paper-authors">Jiung Yeon, Seongbo Ha, Hyeonwoo Yu</span>
        <span class="paper-meta">Updated 2026-02-12</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We propose GSO-SLAM, a real-time monocular dense SLAM system that leverages Gaussian scene representation. Unlike existing methods that couple tracking and mapping with a unified scene, incurring computational costs, or loosely integrate them with well-structured tracking frameworks, introducing redundancies, our method bidirectionally couples Visual Odometry (VO) and Gaussian Splatting (GS). Specifically, our approach formulates joint optimization within an Expectation-Maximization (EM) framework, enabling the simultaneous refinement of VO-derived semi-dense depth estimates and the GS representation without additional computational overhead. Moreover, we present Gaussian Splat Initialization, which utilizes image information, keyframe poses, and pixel associations from VO to produce close approximations to the final Gaussian scene, thereby eliminating the need for heuristic methods. Through extensive experiments, we validate the effectiveness of our method, showing that it not only operates in real time but also achieves state-of-the-art geometric/photometric fidelity of the reconstructed scene and tracking accuracy.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.11714">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.11714.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.11714.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Feature points evaluation on omnidirectional vision with a photorealistic fisheye sequence -- A report on experiments done in 2014</span>
        <span class="paper-authors">Julien Moreau, S. Ambellouis, Yassine Ruichek</span>
        <span class="paper-meta">Updated 2026-02-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">What is this report: This is a scientific report, contributing with a detailed bibliography, a dataset which we will call now PFSeq for &#x27;&#x27;Photorealistic Fisheye Sequence&#x27;&#x27; and make available at https://doi.org/10. 57745/DYIVVU, and comprehensive experiments. This work should be considered as a draft, and has been done during my PhD thesis &#x27;&#x27;Construction of 3D models from fisheye video data-Application to the localisation in urban area&#x27;&#x27; in 2014 [Mor16]. These results have never been published. The aim was to find the best features detector and descriptor for fisheye images, in the context of selfcalibration, with cameras mounted on the top of a car and aiming at the zenith (to proceed then fisheye visual odometry and stereovision in urban scenes). We face a chicken and egg problem, because we can not take advantage of an accurate projection model for an optimal features detection and description, and we rightly need good features to perform the calibration (i.e. to compute the accurate projection model of the camera). What is not this report: It does not contribute with new features algorithm. It does not compare standard features algorithms to algorithms designed for omnidirectional images (unfortunately). It has not been peer-reviewed. Discussions have been translated and enhanced but the experiments have not been run again and the report has not been updated accordingly to the evolution of the state-of-the-art (read this as a 2014 report).</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.05487">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.05487.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.05487.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">When Simultaneous Localization and Mapping Meets Wireless Communications: A Survey</span>
        <span class="paper-authors">Konstantinos Gounis, Sotiris A. Tegos, Dimitrios Tyrovolas, Panagiotis D. Diamantoulakis, George K. Karagiannidis</span>
        <span class="paper-meta">Updated 2026-01-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">The availability of commercial wireless communication and sensing equipment combined with the advancements in intelligent autonomous systems paves the way towards robust joint communications and simultaneous localization and mapping (SLAM). This paper surveys the state-of-the-art in the nexus of SLAM and Wireless Communications, attributing the bidirectional impact of each with a focus on visual SLAM (V-SLAM) integration. We provide an overview of key concepts related to wireless signal propagation, geometric channel modeling, and radio frequency (RF)-based localization and sensing. In addition to this, we show image processing techniques that can detect landmarks, proactively predicting optimal paths for wireless channels. Several dimensions are considered, including the prerequisites, techniques, background, and future directions and challenges of the intersection between SLAM and wireless communications. We analyze mathematical approaches such as probabilistic models, and spatial methods for signal processing, as well as key technological aspects. We expose techniques and items towards enabling a highly effective retrieval of the autonomous robot state. Among other interesting findings, we observe that monocular V-SLAM would benefit from RF relevant information, as the latter can serve as a proxy for the scale ambiguity resolution. Conversely, we find that wireless communications in the context of 5G and beyond can potentially benefit from visual odometry that is central in SLAM. Moreover, we examine other sources besides the camera for SLAM and describe the twofold relation with wireless communications. Finally, integrated solutions performing joint communications and SLAM are still in their infancy: theoretical and practical advancements are required to add higher-level localization and semantic perception capabilities to RF and multi-antenna technologies.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.06995">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.06995.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.06995.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Keyframe-Based Feed-Forward Visual Odometry</span>
        <span class="paper-authors">Weichen Dai, Wenhan Su, Da Kong, Yuhang Ming, Wanzeng Kong</span>
        <span class="paper-meta">Updated 2026-01-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">The emergence of visual foundation models has revolutionized visual odometry~(VO) and SLAM, enabling pose estimation and dense reconstruction within a single feed-forward network. However, unlike traditional pipelines that leverage keyframe methods to enhance efficiency and accuracy, current foundation model based methods, such as VGGT-Long, typically process raw image sequences indiscriminately. This leads to computational redundancy and degraded performance caused by low inter-frame parallax, which provides limited contextual stereo information. Integrating traditional geometric heuristics into these methods is non-trivial, as their performance depends on high-dimensional latent representations rather than explicit geometric metrics. To bridge this gap, we propose a novel keyframe-based feed-forward VO. Instead of relying on hand-crafted rules, our approach employs reinforcement learning to derive an adaptive keyframe policy in a data-driven manner, aligning selection with the intrinsic characteristics of the underlying foundation model. We train our agent on TartanAir dataset and conduct extensive evaluations across several real-world datasets. Experimental results demonstrate that the proposed method achieves consistent and substantial improvements over state-of-the-art feed-forward VO methods.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.16020">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.16020.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.16020.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">360DVO: Deep Visual Odometry for Monocular 360-Degree Camera</span>
        <span class="paper-authors">Xiaopeng Guo, Yinzhe Xu, Huajian Huang, Sai-Kit Yeung</span>
        <span class="paper-meta">Updated 2026-01-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Monocular omnidirectional visual odometry (OVO) systems leverage 360-degree cameras to overcome field-of-view limitations of perspective VO systems. However, existing methods, reliant on handcrafted features or photometric objectives, often lack robustness in challenging scenarios, such as aggressive motion and varying illumination. To address this, we present 360DVO, the first deep learning-based OVO framework. Our approach introduces a distortion-aware spherical feature extractor (DAS-Feat) that adaptively learns distortion-resistant features from 360-degree images. These sparse feature patches are then used to establish constraints for effective pose estimation within a novel omnidirectional differentiable bundle adjustment (ODBA) module. To facilitate evaluation in realistic settings, we also contribute a new real-world OVO benchmark. Extensive experiments on this benchmark and public synthetic datasets (TartanAir V2 and 360VO) demonstrate that 360DVO surpasses state-of-the-art baselines (including 360VO and OpenVSLAM), improving robustness by 50% and accuracy by 37.5%. Homepage: https://chris1004336379.github.io/360DVO-homepage</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.02309">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.02309.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.02309.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Learning to Anchor Visual Odometry: KAN-Based Pose Regression for Planetary Landing</span>
        <span class="paper-authors">Xubo Luo, Zhaojin Li, Xue Wan, Wei Zhang, Leizheng Shu</span>
        <span class="paper-meta">Updated 2025-12-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Accurate and real-time 6-DoF localization is mission-critical for autonomous lunar landing, yet existing approaches remain limited: visual odometry (VO) drifts unboundedly, while map-based absolute localization fails in texture-sparse or low-light terrain. We introduce KANLoc, a monocular localization framework that tightly couples VO with a lightweight but robust absolute pose regressor. At its core is a Kolmogorov-Arnold Network (KAN) that learns the complex mapping from image features to map coordinates, producing sparse but highly reliable global pose anchors. These anchors are fused into a bundle adjustment framework, effectively canceling drift while retaining local motion precision. KANLoc delivers three key advances: (i) a KAN-based pose regressor that achieves high accuracy with remarkable parameter efficiency, (ii) a hybrid VO-absolute localization scheme that yields globally consistent real-time trajectories (&gt;=15 FPS), and (iii) a tailored data augmentation strategy that improves robustness to sensor occlusion. On both realistic synthetic and real lunar landing datasets, KANLoc reduces average translation and rotation error by 32% and 45%, respectively, with per-trajectory gains of up to 45%/48%, outperforming strong baselines.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.06968">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.06968.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.06968.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Trifocal Tensor and Relative Pose Estimation with Known Vertical Direction</span>
        <span class="paper-authors">Tao Li, Zhenbao Yu, Banglei Guan, Jianli Han, Weimin Lv, Friedrich Fraundorfer</span>
        <span class="paper-meta">Updated 2025-12-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">This work presents two novel solvers for estimating the relative poses among views with known vertical directions. The vertical directions of camera views can be easily obtained using inertial measurement units (IMUs) which have been widely used in autonomous vehicles, mobile phones, and unmanned aerial vehicles (UAVs). Given the known vertical directions, our lgorithms only need to solve for two rotation angles and two translation vectors. In this paper, a linear closed-form solution has been described, requiring only four point correspondences in three views. We also propose a minimal solution with three point correspondences using the latest Gröbner basis solver. Since the proposed methods require fewer point correspondences, they can be efficiently applied within the RANSAC framework for outliers removal and pose estimation in visual odometry. The proposed method has been tested on both synthetic data and real-world scenes from KITTI. The experimental results show that the accuracy of the estimated poses is superior to other alternative methods.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.19110">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.19110.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.19110.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SUPER -- A Framework for Sensitivity-based Uncertainty-aware Performance and Risk Assessment in Visual Inertial Odometry</span>
        <span class="paper-authors">Johannes A. Gaus, Daniel Häufle, Woo-Jeong Baek</span>
        <span class="paper-meta">Updated 2025-12-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">While many visual odometry (VO), visual-inertial odometry (VIO), and SLAM systems achieve high accuracy, the majority of existing methods miss to assess risks at runtime. This paper presents SUPER (Sensitivity-based Uncertainty-aware PErformance and Risk assessment) that is a generic and explainable framework that propagates uncertainties via sensitivities for real-time risk assessment in VIO. The scientific novelty lies in the derivation of a real-time risk indicator that is backend-agnostic and exploits the Schur complement blocks of the Gauss-Newton normal matrix to propagate uncertainties. Practically, the Schur complement captures the sensitivity that reflects the influence of the uncertainty on the risk occurrence. Our framework estimates risks on the basis of the residual magnitudes, geometric conditioning, and short horizon temporal trends without requiring ground truth knowledge. Our framework enables to reliably predict trajectory degradation 50 frames ahead with an improvement of 20% to the baseline. In addition, SUPER initiates a stop or relocalization policy with 89.1% recall. The framework is backend agnostic and operates in real time with less than 0.2% additional CPU cost. Experiments show that SUPER provides consistent uncertainty estimates. A SLAM evaluation highlights the applicability to long horizon mapping.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.14189">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.14189.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.14189.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Inertial Magnetic SLAM Systems Using Low-Cost Sensors</span>
        <span class="paper-authors">Chuan Huang, Gustaf Hendeby, Isaac Skog</span>
        <span class="paper-meta">Updated 2025-12-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Spatially inhomogeneous magnetic fields offer a valuable, non-visual information source for positioning. Among systems leveraging this, magnetic field-based simultaneous localization and mapping (SLAM) systems are particularly attractive because they can provide positioning information and build a magnetic field map on the fly. Moreover, they have bounded error within mapped regions. However, state-of-the-art methods typically require low-drift odometry data provided by visual odometry or a wheel encoder, etc. This is because these systems need to minimize/reduce positioning errors while exploring, which happens when they are in unmapped regions. To address these limitations, this work proposes a loosely coupled and a tightly coupled inertial magnetic SLAM (IM-SLAM) system. The proposed systems use commonly available low-cost sensors: an inertial measurement unit (IMU), a magnetometer array, and a barometer. The use of non-visual data provides a significant advantage over visual-based systems, making it robust to low-visibility conditions. Both systems employ state-space representations, and magnetic field models on different scales. The difference lies in how they use a local and global magnetic field model. The loosely coupled system uses these models separately in two state-space models, while the tightly coupled system integrates them into one state-space model. Experiment results show that the tightly coupled IM-SLAM system achieves lower positioning errors than the loosely coupled system in most scenarios, with typical errors on the order of meters per 100 meters traveled. These results demonstrate the feasiblity of developing a full 3D IM-SLAM systems using low-cost sensors and the potential of applying these systems in emergency response scenarios such as mine/fire rescue.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.10128">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.10128.pdf">PDF</a>
          <a class="chip" href="https://github.com/Huang-Chuan/IM-SLAM">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.10128.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">KM-ViPE: Online Tightly Coupled Vision-Language-Geometry Fusion for Open-Vocabulary Semantic SLAM</span>
        <span class="paper-authors">Zaid Nasser et.al.</span>
        <span class="paper-meta">Updated 2025-12-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.01889">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.01889.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.01889.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Odometry Without Correspondence from Inertially Constrained Ruled Surfaces</span>
        <span class="paper-authors">Chenqi Zhu, Levi Burner, Yiannis Aloimonos</span>
        <span class="paper-meta">Updated 2025-11-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Visual odometry techniques typically rely on feature extraction from a sequence of images and subsequent computation of optical flow. This point-to-point correspondence between two consecutive frames can be costly to compute and suffers from varying accuracy, which affects the odometry estimate&#x27;s quality. Attempts have been made to bypass the difficulties originating from the correspondence problem by adopting line features and fusing other sensors (event camera, IMU) to improve performance, many of which still heavily rely on correspondence. If the camera observes a straight line as it moves, the image of the line sweeps a smooth surface in image-space time. It is a ruled surface and analyzing its shape gives information about odometry. Further, its estimation requires only differentially computed updates from point-to-line associations. Inspired by event cameras&#x27; propensity for edge detection, this research presents a novel algorithm to reconstruct 3D scenes and visual odometry from these ruled surfaces. By constraining the surfaces with the inertia measurements from an onboard IMU sensor, the dimensionality of the solution space is greatly reduced.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.00327">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.00327.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.00327.pdf">
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
        <span class="paper-authors">Sacchin Sundar, Atman Kikani, Aaliya Alam, Sumukh Shrote, A. Nayeemulla Khan, A. Shahina</span>
        <span class="paper-meta">Updated 2025-11-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Underwater visual localization remains challenging due to wavelength-dependent attenuation, poor texture, and non-Gaussian sensor noise. We introduce MARVO, a physics-aware, learning-integrated odometry framework that fuses underwater image formation modeling, differentiable matching, and reinforcement-learning optimization. At the front-end, we extend transformer-based feature matcher with a Physics Aware Radiance Adapter that compensates for color channel attenuation and contrast loss, yielding geometrically consistent feature correspondences under turbidity. These semi dense matches are combined with inertial and pressure measurements inside a factor-graph backend, where we formulate a keyframe-based visual-inertial-barometric estimator using GTSAM library. Each keyframe introduces (i) Pre-integrated IMU motion factors, (ii) MARVO-derived visual pose factors, and (iii) barometric depth priors, giving a full-state MAP estimate in real time. Lastly, we introduce a Reinforcement-Learningbased Pose-Graph Optimizer that refines global trajectories beyond local minima of classical least-squares solvers by learning optimal retraction actions on SE(2).</p>
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
        <span class="paper-title">Dual-Agent Reinforcement Learning for Adaptive and Cost-Aware Visual-Inertial Odometry</span>
        <span class="paper-authors">Feiyang Pan et.al.</span>
        <span class="paper-meta">Updated 2025-11-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.21083">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.21083.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.21083.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Conceptual Evaluation of Deep Visual Stereo Odometry for the MARWIN Radiation Monitoring Robot in Accelerator Tunnels</span>
        <span class="paper-authors">André Dehne et.al.</span>
        <span class="paper-meta">Updated 2025-11-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.00080">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.00080.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.00080.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Estimating Fog Parameters from a Sequence of Stereo Images</span>
        <span class="paper-authors">Yining Ding et.al.</span>
        <span class="paper-meta">Updated 2025-11-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.20865">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.20865.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.20865.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Metric, inertially aligned monocular state estimation via kinetodynamic priors</span>
        <span class="paper-authors">Jiaxin Liu, Min Li, Wanting Xu, Liang Li, Jiaqi Yang, Laurent Kneip</span>
        <span class="paper-meta">Updated 2025-11-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Accurate state estimation for flexible robotic systems poses significant challenges, particular for platforms with dynamically deforming structures that invalidate rigid-body assumptions. This paper tackles this problem and allows to extend existing rigid-body pose estimation methods to non-rigid systems. Our approach hinges on two core assumptions: first, the elastic properties are captured by an injective deformation-force model, efficiently learned via a Multi-Layer Perceptron; second, we solve the platform&#x27;s inherently smooth motion using continuous-time B-spline kinematic models. By continuously applying Newton&#x27;s Second Law, our method establishes a physical link between visually-derived trajectory acceleration and predicted deformation-induced acceleration. We demonstrate that our approach not only enables robust and accurate pose estimation on non-rigid platforms, but that the properly modeled platform physics instigate inertial sensing properties. We demonstrate this feasibility on a simple spring-camera system, and show how it robustly resolves the typically ill-posed problem of metric scale and gravity recovery in monocular visual odometry.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.20496">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.20496.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.20496.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">AMB3R: Accurate Feed-forward Metric-scale 3D Reconstruction with Backend</span>
        <span class="paper-authors">Hengyi Wang, Lourdes Agapito</span>
        <span class="paper-meta">Updated 2025-11-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We present AMB3R, a multi-view feed-forward model for dense 3D reconstruction on a metric-scale that addresses diverse 3D vision tasks. The key idea is to leverage a sparse, yet compact, volumetric scene representation as our backend, enabling geometric reasoning with spatial compactness. Although trained solely for multi-view reconstruction, we demonstrate that AMB3R can be seamlessly extended to uncalibrated visual odometry (online) or large-scale structure from motion without the need for task-specific fine-tuning or test-time optimization. Compared to prior pointmap-based models, our approach achieves state-of-the-art performance in camera pose, depth, and metric-scale estimation, 3D reconstruction, and even surpasses optimization-based SLAM and SfM methods with dense reconstruction priors on common benchmarks.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.20343">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.20343.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.20343.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">AutoOdom: Learning Auto-regressive Proprioceptive Odometry for Legged Locomotion</span>
        <span class="paper-authors">Changsheng Luo, Yushi Wang, Wenhan Cai, Mingguo Zhao</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Accurate proprioceptive odometry is fundamental for legged robot navigation in GPS-denied and visually degraded environments where conventional visual odometry systems fail. Current approaches face critical limitations: analytical filtering methods suffer from modeling uncertainties and cumulative drift, hybrid learning-filtering approaches remain constrained by their analytical components, while pure learning-based methods struggle with simulation-to-reality transfer and demand extensive real-world data collection. This paper introduces AutoOdom, a novel autoregressive proprioceptive odometry system that overcomes these challenges through an innovative two-stage training paradigm. Stage 1 employs large-scale simulation data to learn complex nonlinear dynamics and rapidly changing contact states inherent in legged locomotion, while Stage 2 introduces an autoregressive enhancement mechanism using limited real-world data to effectively bridge the sim-to-real gap. The key innovation lies in our autoregressive training approach, where the model learns from its own predictions to develop resilience against sensor noise and improve robustness in highly dynamic environments. Comprehensive experimental validation on the Booster T1 humanoid robot demonstrates that AutoOdom significantly outperforms state-of-the-art methods across all evaluation metrics, achieving 57.2% improvement in absolute trajectory error, 59.2% improvement in Umeyama-aligned error, and 36.2% improvement in relative pose error compared to the Legolas baseline. Extensive ablation studies provide critical insights into sensor modality selection and temporal modeling, revealing counterintuitive findings about IMU acceleration data and validating our systematic design choices for robust proprioceptive odometry in challenging locomotion scenarios.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.18857">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.18857.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.18857.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">IndustryNav: Exploring Spatial Reasoning of Embodied Agents in Dynamic Industrial Navigation</span>
        <span class="paper-authors">Yifan Li et.al.</span>
        <span class="paper-meta">Updated 2025-11-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.17384">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.17384.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.17384.pdf">
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
        <span class="paper-title">DPVO-QAT++: Heterogeneous QAT and CUDA Kernel Fusion for High-Performance Deep Patch Visual Odometry</span>
        <span class="paper-authors">Cheng Liao</span>
        <span class="paper-meta">Updated 2025-11-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Deep learning-based Visual SLAM (vSLAM) systems exhibit exceptional geometric reasoning capabilities, yet their prohibitive computational overhead severely restricts deployment on resource-constrained autonomous platforms. This paper presents a hierarchical quantization optimization framework, DPVO-QAT++ (DPVO-QAT++: Heterogeneous QAT and CUDA Kernel Fusion for High-Performance Deep Patch Visual Odometry). Through the synergistic integration of learnable scale parameterization, a heterogeneous precision design for the Visual Odometry (VO) front-end and back-end (front-end floating-point fake quantization with FP16/FP32; back-end full precision), and GPU-native kernel fusion for fake quantization (custom CUDA kernels), our framework significantly reduces memory footprint and increases processing speed while preserving the trajectory accuracy of the original model. On the TartanAir dataset, our framework achieves an average FPS increase of 52.1%, a 29.1% reduction in median latency, and a 64.9% reduction in peak GPU memory reservation, while maintaining trajectory accuracy (ATE) comparable to the original DPVO model across 32 validation sequences. On the EuRoC dataset, it realizes an average FPS increase of 30.1%, a 23.1% reduction in median latency, and a 37.7% reduction in peak GPU memory reservation, maintaining comparable trajectory accuracy (ATE) across 11 validation sequences. Experimental results demonstrate that DPVO-QAT++ effectively bridges the gap between high-precision deep VO and the efficiency requirements for practical deployment, offering a viable engineering paradigm for the application of this technology on real-world embedded platforms.   Keywords: Visual Odometry, Heterogeneous Precision Architecture, Quantization-Aware Training, CUDA Kernel Fusion, Scale-Only Training, Deep Patch Visual Odometry, GPU-Native Kernel Fusion.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.12653">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.12653.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.12653.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DualVision ArthroNav: Investigating Opportunities to Enhance Localization and Reconstruction in Image-based Arthroscopy Navigation via External Cameras</span>
        <span class="paper-authors">Hongchao Shu et.al.</span>
        <span class="paper-meta">Updated 2025-11-12</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.10699">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.10699.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.10699.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SMF-VO: Direct Ego-Motion Estimation via Sparse Motion Fields</span>
        <span class="paper-authors">Sangheon Yang et.al.</span>
        <span class="paper-meta">Updated 2025-11-12</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.09072">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.09072.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.09072.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Integration of Visual SLAM into Consumer-Grade Automotive Localization</span>
        <span class="paper-authors">Luis Diener et.al.</span>
        <span class="paper-meta">Updated 2025-11-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.06919">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.06919.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.06919.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Robust and High-Fidelity 3D Gaussian Splatting: Fusing Pose Priors and Geometry Constraints for Texture-Deficient Outdoor Scenes</span>
        <span class="paper-authors">Meijun Guo et.al.</span>
        <span class="paper-meta">Updated 2025-11-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.06765">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.06765.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.06765.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LiDAR-VGGT: Cross-Modal Coarse-to-Fine Fusion for Globally Consistent and Metric-Scale Dense Mapping</span>
        <span class="paper-authors">Lijie Wang et.al.</span>
        <span class="paper-meta">Updated 2025-11-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.01186">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.01186.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.01186.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian Splatting SLAM</span>
        <span class="paper-authors">Mirko Usuelli et.al.</span>
        <span class="paper-meta">Updated 2025-10-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.26358">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.26358.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.26358.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">EA3D: Online Open-World 3D Object Extraction from Streaming Videos</span>
        <span class="paper-authors">Xiaoyu Zhou et.al.</span>
        <span class="paper-meta">Updated 2025-10-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.25146">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.25146.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.25146.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Degradation-Aware Cooperative Multi-Modal GNSS-Denied Localization Leveraging LiDAR-Based Robot Detections</span>
        <span class="paper-authors">Václav Pritzl et.al.</span>
        <span class="paper-meta">Updated 2025-10-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.20480">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.20480.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.20480.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SPORTS: Simultaneous Panoptic Odometry, Rendering, Tracking and Segmentation for Urban Scenes Understanding</span>
        <span class="paper-authors">Zhiliu Yang et.al.</span>
        <span class="paper-meta">Updated 2025-10-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.12749">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.12749.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.12749.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">PolygMap: A Perceptive Locomotion Framework for Humanoid Robot Stair Climbing</span>
        <span class="paper-authors">Bingquan Li et.al.</span>
        <span class="paper-meta">Updated 2025-10-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.12346">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.12346.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.12346.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Visual Odometry with Transformers</span>
        <span class="paper-authors">Vlardimir Yugay et.al.</span>
        <span class="paper-meta">Updated 2025-10-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.03348">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.03348.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.03348.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Omni-LIVO: Robust RGB-Colored Multi-Camera Visual-Inertial-LiDAR Odometry via Photometric Migration and ESIKF Fusion</span>
        <span class="paper-authors">Yinong Cao et.al.</span>
        <span class="paper-meta">Updated 2025-09-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.15673">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.15673.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.15673.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">BEV-ODOM2: Enhanced BEV-based Monocular Visual Odometry with PV-BEV Fusion and Dense Flow Supervision for Ground Robots</span>
        <span class="paper-authors">Yufei Wei et.al.</span>
        <span class="paper-meta">Updated 2025-09-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.14636">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.14636.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.14636.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">UM-Depth : Uncertainty Masked Self-Supervised Monocular Depth Estimation with Visual Odometry</span>
        <span class="paper-authors">Tae-Wook Um et.al.</span>
        <span class="paper-meta">Updated 2025-09-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.13713">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.13713.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.13713.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Barometer-Aided Attitude Estimation</span>
        <span class="paper-authors">Méloné Nyoba Tchonkeu et.al.</span>
        <span class="paper-meta">Updated 2025-09-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.13649">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.13649.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.13649.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Good Deep Features to Track: Self-Supervised Feature Extraction and Tracking in Visual Odometry</span>
        <span class="paper-authors">Sai Puneeth Reddy Gottam et.al.</span>
        <span class="paper-meta">Updated 2025-09-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.08333">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.08333.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.08333.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Deep Visual Odometry for Stereo Event Cameras</span>
        <span class="paper-authors">Sheng Zhong et.al.</span>
        <span class="paper-meta">Updated 2025-09-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.08235">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.08235.pdf">PDF</a>
          <a class="chip" href="https://github.com/USTCPCS/CVPR2018_attention">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.08235.pdf">
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
        <span class="paper-title">Odometry Calibration and Pose Estimation of a 4WIS4WID Mobile Wall Climbing Robot</span>
        <span class="paper-authors">Branimir Ćaran et.al.</span>
        <span class="paper-meta">Updated 2025-09-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.04016">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.04016.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.04016.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">CoProU-VO: Combining Projected Uncertainty for End-to-End Unsupervised Monocular Visual Odometry</span>
        <span class="paper-authors">Jingchao Xie et.al.</span>
        <span class="paper-meta">Updated 2025-08-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2508.00568">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2508.00568.pdf">PDF</a>
          <a class="chip" href="https://github.com/Jchao-Xie/CoProU">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2508.00568.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A Fast and Light-weight Non-Iterative Visual Odometry with RGB-D Cameras</span>
        <span class="paper-authors">Zheng Yang et.al.</span>
        <span class="paper-meta">Updated 2025-07-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.18886">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.18886.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.18886.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DiffPF: Differentiable Particle Filtering with Generative Sampling via Conditional Diffusion Models</span>
        <span class="paper-authors">Ziyu Wan et.al.</span>
        <span class="paper-meta">Updated 2025-07-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.15716">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.15716.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.15716.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Dense-depth map guided deep Lidar-Visual Odometry with Sparse Point Clouds and Images</span>
        <span class="paper-authors">JunYing Huang et.al.</span>
        <span class="paper-meta">Updated 2025-07-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.15496">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.15496.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.15496.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DINO-VO: A Feature-based Visual Odometry Leveraging a Visual Foundation Model</span>
        <span class="paper-authors">Maulana Bisyir Azhari et.al.</span>
        <span class="paper-meta">Updated 2025-07-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.13145">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.13145.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.13145.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MoCap2GT: A High-Precision Ground Truth Estimator for SLAM Benchmarking Based on Motion Capture and IMU Fusion</span>
        <span class="paper-authors">Zichao Shu et.al.</span>
        <span class="paper-meta">Updated 2025-07-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.12920">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.12920.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.12920.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Next-Gen Museum Guides: Autonomous Navigation and Visitor Interaction with an Agentic Robot</span>
        <span class="paper-authors">Luca Garello et.al.</span>
        <span class="paper-meta">Updated 2025-07-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.12273">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.12273.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.12273.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Tree-SLAM: semantic object SLAM for efficient mapping of individual trees in orchards</span>
        <span class="paper-authors">David Rapado-Rincon et.al.</span>
        <span class="paper-meta">Updated 2025-07-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.12093">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.12093.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.12093.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Towards Robust Sensor-Fusion Ground SLAM: A Comprehensive Benchmark and A Resilient Framework</span>
        <span class="paper-authors">Deteng Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-07-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.08364">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.08364.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.08364.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Hardware-Aware Feature Extraction Quantisation for Real-Time Visual Odometry on FPGA Platforms</span>
        <span class="paper-authors">Mateusz Wasala et.al.</span>
        <span class="paper-meta">Updated 2025-07-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.07903">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.07903.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.07903.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">IRAF-SLAM: An Illumination-Robust and Adaptive Feature-Culling Front-End for Visual SLAM in Challenging Environments</span>
        <span class="paper-authors">Thanh Nguyen Canh et.al.</span>
        <span class="paper-meta">Updated 2025-07-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.07752">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.07752.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.07752.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">g2o vs. Ceres: Optimizing Scan Matching in Cartographer SLAM</span>
        <span class="paper-authors">Quanjie Qiu et.al.</span>
        <span class="paper-meta">Updated 2025-07-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.07142">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.07142.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.07142.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Gaussian-LIC2: LiDAR-Inertial-Camera Gaussian Splatting SLAM</span>
        <span class="paper-authors">Xiaolei Lang et.al.</span>
        <span class="paper-meta">Updated 2025-07-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.04004">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.04004.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.04004.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Mapping the Catacombs: An Underwater Cave Segment of the Devil&#x27;s Eye System</span>
        <span class="paper-authors">Michalis Chatzispyrou et.al.</span>
        <span class="paper-meta">Updated 2025-07-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.06397">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.06397.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.06397.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Cooperative Mapping, Localization, and Beam Management via Multi-Modal SLAM in ISAC Systems</span>
        <span class="paper-authors">Hang Que et.al.</span>
        <span class="paper-meta">Updated 2025-07-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.05718">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.05718.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.05718.pdf">
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
        <span class="paper-title">Outdoor Monocular SLAM with Global Scale-Consistent 3D Gaussian Pointmaps</span>
        <span class="paper-authors">Chong Cheng et.al.</span>
        <span class="paper-meta">Updated 2025-07-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.03737">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.03737.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.03737.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">RaGNNarok: A Light-Weight Graph Neural Network for Enhancing Radar Point Clouds on Unmanned Ground Vehicles</span>
        <span class="paper-authors">David Hunt et.al.</span>
        <span class="paper-meta">Updated 2025-07-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.00937">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.00937.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.00937.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Generation of Indoor Open Street Maps for Robot Navigation from CAD Files</span>
        <span class="paper-authors">Jiajie Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-07-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.00552">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.00552.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.00552.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">VOCAL: Visual Odometry via ContrAstive Learning</span>
        <span class="paper-authors">Chi-Yao Huang et.al.</span>
        <span class="paper-meta">Updated 2025-06-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.00243">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.00243.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.00243.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">TVG-SLAM: Robust Gaussian Splatting SLAM with Tri-view Geometric Constraints</span>
        <span class="paper-authors">Zhen Tan et.al.</span>
        <span class="paper-meta">Updated 2025-06-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.23207">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.23207.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.23207.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Event-based Stereo Visual-Inertial Odometry with Voxel Map</span>
        <span class="paper-authors">Zhaoxing Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-06-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.23078">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.23078.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.23078.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Adaptive Multipath-Based SLAM for Distributed MIMO Systems</span>
        <span class="paper-authors">Xuhong Li et.al.</span>
        <span class="paper-meta">Updated 2025-06-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.21798">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.21798.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.21798.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">EndoFlow-SLAM: Real-Time Endoscopic SLAM with Flow-Constrained Gaussian Splatting</span>
        <span class="paper-authors">Taoyu Wu et.al.</span>
        <span class="paper-meta">Updated 2025-06-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.21420">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.21420.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.21420.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">CURL-SLAM: Continuous and Compact LiDAR Mapping</span>
        <span class="paper-authors">Kaicheng Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-06-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.21077">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.21077.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.21077.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SPARK: Graph-Based Online Semantic Integration System for Robot Task Planning</span>
        <span class="paper-authors">Mimo Shirasaka et.al.</span>
        <span class="paper-meta">Updated 2025-06-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.20394">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.20394.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.20394.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Real-Time Obstacle Avoidance Algorithms for Unmanned Aerial and Ground Vehicles</span>
        <span class="paper-authors">Jingwen Wei et.al.</span>
        <span class="paper-meta">Updated 2025-06-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.20311">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.20311.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.20311.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Ark: An Open-source Python-based Framework for Robot Learning</span>
        <span class="paper-authors">Magnus Dierking et.al.</span>
        <span class="paper-meta">Updated 2025-06-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.21628">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.21628.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.21628.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Posterior Cramér-Rao Bounds on Localization and Mapping Errors in Distributed MIMO SLAM</span>
        <span class="paper-authors">Benjamin J. B. Deutschmann et.al.</span>
        <span class="paper-meta">Updated 2025-06-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.19957">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.19957.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.19957.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Multimodal Fusion SLAM with Fourier Attention</span>
        <span class="paper-authors">Youjie Zhou et.al.</span>
        <span class="paper-meta">Updated 2025-06-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.18204">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.18204.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.18204.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">RA-NeRF: Robust Neural Radiance Field Reconstruction with Accurate Camera Pose Estimation under Complex Trajectories</span>
        <span class="paper-authors">Qingsong Yan et.al.</span>
        <span class="paper-meta">Updated 2025-06-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.15242">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.15242.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.15242.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GRAND-SLAM: Local Optimization for Globally Consistent Large-Scale Multi-Agent Gaussian SLAM</span>
        <span class="paper-authors">Annika Thomas et.al.</span>
        <span class="paper-meta">Updated 2025-06-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.18885">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.18885.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.18885.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation</span>
        <span class="paper-authors">Tianchen Deng et.al.</span>
        <span class="paper-meta">Updated 2025-06-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.18678">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.18678.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.18678.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ADA-DPM: A Neural Descriptors-based Adaptive Noise Point Filtering Strategy for SLAM</span>
        <span class="paper-authors">Yongxin Shao et.al.</span>
        <span class="paper-meta">Updated 2025-06-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.18016">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.18016.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.18016.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Optimizing Exploration with a New Uncertainty Framework for Active SLAM Systems</span>
        <span class="paper-authors">Sebastian Sansoni et.al.</span>
        <span class="paper-meta">Updated 2025-06-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.17775">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.17775.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.17775.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MCOO-SLAM: A Multi-Camera Omnidirectional Object SLAM System</span>
        <span class="paper-authors">Miaoxin Pan et.al.</span>
        <span class="paper-meta">Updated 2025-06-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.15402">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.15402.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.15402.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SHeRLoc: Synchronized Heterogeneous Radar Place Recognition for Cross-Modal Localization</span>
        <span class="paper-authors">Hanjun Kim et.al.</span>
        <span class="paper-meta">Updated 2025-06-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.15175">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.15175.pdf">PDF</a>
          <a class="chip" href="https://github.com/hanjun815/SHeRLoc">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.15175.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">VIMS: A Visual-Inertial-Magnetic-Sonar SLAM System in Underwater Environments</span>
        <span class="paper-authors">Bingbing Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-06-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.15126">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.15126.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.15126.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Slanted light-sheet array microscopy for large volume imaging at rates exceeding 100 Hz</span>
        <span class="paper-authors">Kai Long et.al.</span>
        <span class="paper-meta">Updated 2025-06-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.13664">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.13664.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.13664.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Cognitive Synergy Architecture: SEGO for Human-Centric Collaborative Robots</span>
        <span class="paper-authors">Jaehong Oh et.al.</span>
        <span class="paper-meta">Updated 2025-06-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.13149">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.13149.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.13149.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A Novel ViDAR Device With Visual Inertial Encoder Odometry and Reinforcement Learning-Based Active SLAM Method</span>
        <span class="paper-authors">Zhanhua Xin et.al.</span>
        <span class="paper-meta">Updated 2025-06-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.13100">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.13100.pdf">PDF</a>
          <a class="chip" href="https://github.com/dev-org-12-may-1000-4000/testing-04-May1310004000Repo2506">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.13100.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SuperPoint-SLAM3: Augmenting ORB-SLAM3 with Deep Features, Adaptive NMS, and Learning-Based Loop Closure</span>
        <span class="paper-authors">Shahram Najam Syed et.al.</span>
        <span class="paper-meta">Updated 2025-06-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.13089">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.13089.pdf">PDF</a>
          <a class="chip" href="https://github.com/shahram95/superpointslam3">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.13089.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LRSLAM: Low-rank Representation of Signed Distance Fields in Dense Visual SLAM System</span>
        <span class="paper-authors">Hongbeen Park et.al.</span>
        <span class="paper-meta">Updated 2025-06-12</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.10567">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.10567.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.10567.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">VAULT: A Mobile Mapping System for ROS 2-based Autonomous Robots</span>
        <span class="paper-authors">Miguel Á. González-Santamarta et.al.</span>
        <span class="paper-meta">Updated 2025-06-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.09583">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.09583.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.09583.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">UFM: A Simple Path towards Unified Dense Correspondence with Flow</span>
        <span class="paper-authors">Yuchen Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-06-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.09278">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.09278.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.09278.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Princeton365: A Diverse Dataset with Accurate Camera Pose</span>
        <span class="paper-authors">Karhan Kayan et.al.</span>
        <span class="paper-meta">Updated 2025-06-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.09035">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.09035.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.09035.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Planar Collisionless Shock Simulations with Semi-Implicit Particle-in-Cell Model FLEKS</span>
        <span class="paper-authors">Hongyang Zhou et.al.</span>
        <span class="paper-meta">Updated 2025-06-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.08384">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.08384.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.08384.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ZeroVO: Visual Odometry with Minimal Assumptions</span>
        <span class="paper-authors">Lei Lai et.al.</span>
        <span class="paper-meta">Updated 2025-06-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.08005">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.08005.pdf">PDF</a>
          <a class="chip" href="https://github.com/h2xlab/ZeroVO">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.08005.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Faster than Fast: Accelerating Oriented FAST Feature Detection on Low-end Embedded GPUs</span>
        <span class="paper-authors">Qiong Chang et.al.</span>
        <span class="paper-meta">Updated 2025-06-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.07164">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.07164.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.07164.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">UNO: Unified Self-Supervised Monocular Odometry for Platform-Agnostic Deployment</span>
        <span class="paper-authors">Wentao Zhao et.al.</span>
        <span class="paper-meta">Updated 2025-06-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.07013">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.07013.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.07013.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GS4: Generalizable Sparse Splatting Semantic SLAM</span>
        <span class="paper-authors">Mingqi Jiang et.al.</span>
        <span class="paper-meta">Updated 2025-06-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.06517">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.06517.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.06517.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Enhancing Situational Awareness in Underwater Robotics with Multi-modal Spatial Perception</span>
        <span class="paper-authors">Pushyami Kaveti et.al.</span>
        <span class="paper-meta">Updated 2025-06-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.06476">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.06476.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.06476.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Dy3DGS-SLAM: Monocular 3D Gaussian Splatting SLAM for Dynamic Environments</span>
        <span class="paper-authors">Mingrui Li et.al.</span>
        <span class="paper-meta">Updated 2025-06-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.05965">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.05965.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.05965.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Analysis of points outcome in ATP Grand Slam Tennis using big data and machine learning</span>
        <span class="paper-authors">Martin Illum et.al.</span>
        <span class="paper-meta">Updated 2025-06-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.05866">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.05866.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.05866.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
        <span class="paper-title">cuVSLAM: CUDA accelerated visual odometry</span>
        <span class="paper-authors">Alexander Korovko et.al.</span>
        <span class="paper-meta">Updated 2025-06-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.04359">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.04359.pdf">PDF</a>
          <a class="chip" href="https://github.com/nvlabs/pycuvslam">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.04359.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Seeing in the Dark: Benchmarking Egocentric 3D Vision with the Oxford Day-and-Night Dataset</span>
        <span class="paper-authors">Zirui Wang et.al.</span>
        <span class="paper-meta">Updated 2025-06-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.04224">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.04224.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.04224.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LEG-SLAM: Real-Time Language-Enhanced Gaussian Splatting for SLAM</span>
        <span class="paper-authors">Roman Titkov et.al.</span>
        <span class="paper-meta">Updated 2025-06-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.03073">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.03073.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.03073.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Online Performance Assessment of Multi-Source-Localization for Autonomous Driving Systems Using Subjective Logic</span>
        <span class="paper-authors">Stefan Orf et.al.</span>
        <span class="paper-meta">Updated 2025-06-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.02932">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.02932.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.02932.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">VTGaussian-SLAM: RGBD SLAM for Large Scale Scenes with Splatting View-Tied 3D Gaussians</span>
        <span class="paper-authors">Pengchong Hu et.al.</span>
        <span class="paper-meta">Updated 2025-06-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.02741">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.02741.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.02741.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GeneA-SLAM2: Dynamic SLAM with AutoEncoder-Preprocessed Genetic Keypoints Resampling and Depth Variance-Guided Dynamic Region Removal</span>
        <span class="paper-authors">Shufan Qing et.al.</span>
        <span class="paper-meta">Updated 2025-06-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.02736">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.02736.pdf">PDF</a>
          <a class="chip" href="https://github.com/qingshufan/GeneA-SLAM2">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.02736.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Olfactory Inertial Odometry: Methodology for Effective Robot Navigation by Scent</span>
        <span class="paper-authors">Kordel K. France et.al.</span>
        <span class="paper-meta">Updated 2025-06-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.02373">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.02373.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.02373.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Globally Consistent RGB-D SLAM with 2D Gaussian Splatting</span>
        <span class="paper-authors">Xingguang Zhong et.al.</span>
        <span class="paper-meta">Updated 2025-06-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.00970">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.00970.pdf">PDF</a>
          <a class="chip" href="https://github.com/PRBonn/2DGS-SLAM">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.00970.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Black-box Adversarial Attacks on CNN-based SLAM Algorithms</span>
        <span class="paper-authors">Maria Rafaela Gkeka et.al.</span>
        <span class="paper-meta">Updated 2025-05-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.24654">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.24654.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.24654.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Semantic Exploration and Dense Mapping of Complex Environments using Ground Robots Equipped with LiDAR and Panoramic Camera</span>
        <span class="paper-authors">Xiaoyang Zhan et.al.</span>
        <span class="paper-meta">Updated 2025-05-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.22880">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.22880.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.22880.pdf">
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
        <span class="paper-title">UP-SLAM: Adaptively Structured Gaussian SLAM with Uncertainty Prediction in Dynamic Environments</span>
        <span class="paper-authors">Wancai Zheng et.al.</span>
        <span class="paper-meta">Updated 2025-05-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.22335">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.22335.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.22335.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">HS-SLAM: A Fast and Hybrid Strategy-Based SLAM Approach for Low-Speed Autonomous Driving</span>
        <span class="paper-authors">Bingxiang Kang et.al.</span>
        <span class="paper-meta">Updated 2025-05-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.20906">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.20906.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.20906.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ProBA: Probabilistic Bundle Adjustment with the Bhattacharyya Coefficient</span>
        <span class="paper-authors">Jason Chui et.al.</span>
        <span class="paper-meta">Updated 2025-05-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.20858">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.20858.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.20858.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ADD-SLAM: Adaptive Dynamic Dense SLAM with Gaussian Splatting</span>
        <span class="paper-authors">Wenhua Wu et.al.</span>
        <span class="paper-meta">Updated 2025-05-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.19420">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.19420.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.19420.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">VPGS-SLAM: Voxel-based Progressive 3D Gaussian SLAM in Large-Scale Scenes</span>
        <span class="paper-authors">Tianchen Deng et.al.</span>
        <span class="paper-meta">Updated 2025-05-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.18992">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.18992.pdf">PDF</a>
          <a class="chip" href="https://github.com/dtc111111/vpgs-slam">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.18992.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">CU-Multi: A Dataset for Multi-Robot Data Association</span>
        <span class="paper-authors">Doncey Albin et.al.</span>
        <span class="paper-meta">Updated 2025-05-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.17576">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.17576.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.17576.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">VGGT-SLAM: Dense RGB SLAM Optimized on the SL(4) Manifold</span>
        <span class="paper-authors">Dominic Maggio et.al.</span>
        <span class="paper-meta">Updated 2025-05-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.12549">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.12549.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.12549.pdf">
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
        <span class="paper-title">Place Recognition: A Comprehensive Review, Current Challenges and Future Directions</span>
        <span class="paper-authors">Zhenyu Li et.al.</span>
        <span class="paper-meta">Updated 2025-05-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.14068">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.14068.pdf">PDF</a>
          <a class="chip" href="https://github.com/cv4ra/sota-place-recognitioner">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.14068.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A Methodological Framework for Measuring Spatial Labeling Similarity</span>
        <span class="paper-authors">Yihang Du et.al.</span>
        <span class="paper-meta">Updated 2025-05-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.14128">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.14128.pdf">PDF</a>
          <a class="chip" href="https://github.com/yihdu/slam">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.14128.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">eStonefish-scenes: A synthetically generated dataset for underwater event-based optical flow prediction tasks</span>
        <span class="paper-authors">Jad Mansour et.al.</span>
        <span class="paper-meta">Updated 2025-05-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.13309">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.13309.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.13309.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey</span>
        <span class="paper-authors">Calvin Galagain et.al.</span>
        <span class="paper-meta">Updated 2025-05-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.12384">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.12384.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.12384.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Structureless VIO</span>
        <span class="paper-authors">Junlin Song et.al.</span>
        <span class="paper-meta">Updated 2025-05-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.12337">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.12337.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.12337.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video</span>
        <span class="paper-authors">Ryan Hoque et.al.</span>
        <span class="paper-meta">Updated 2025-05-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.11709">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.11709.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.11709.pdf">
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
        <span class="paper-title">Robust 2D lidar-based SLAM in arboreal environments without IMU/GNSS</span>
        <span class="paper-authors">Paola Nazate-Burgos et.al.</span>
        <span class="paper-meta">Updated 2025-05-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.10847">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.10847.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.10847.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">TartanGround: A Large-Scale Dataset for Ground Robot Perception and Navigation</span>
        <span class="paper-authors">Manthan Patel et.al.</span>
        <span class="paper-meta">Updated 2025-05-15</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.10696">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.10696.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.10696.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A hybrid SLAM-Payne framework for atmospheric parameter and abundance determination of early-type Stars from LAMOST DR9 low-resolution Spectra</span>
        <span class="paper-authors">Weijia Sun et.al.</span>
        <span class="paper-meta">Updated 2025-05-15</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.10310">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.10310.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.10310.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Large-Scale Gaussian Splatting SLAM</span>
        <span class="paper-authors">Zhe Xin et.al.</span>
        <span class="paper-meta">Updated 2025-05-15</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.09915">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.09915.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.09915.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Automated Meta Prompt Engineering for Alignment with the Theory of Mind</span>
        <span class="paper-authors">Aaron Baughman et.al.</span>
        <span class="paper-meta">Updated 2025-05-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.09024">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.09024.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.09024.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MDF: Multi-Modal Data Fusion with CNN-Based Object Detection for Enhanced Indoor Localization Using LiDAR-SLAM</span>
        <span class="paper-authors">Saqi Hussain Kalan et.al.</span>
        <span class="paper-meta">Updated 2025-05-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.08388">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.08388.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.08388.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SKiD-SLAM: Robust, Lightweight, and Distributed Multi-Robot LiDAR SLAM in Resource-Constrained Field Environments</span>
        <span class="paper-authors">Hogyun Kim et.al.</span>
        <span class="paper-meta">Updated 2025-05-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.08230">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.08230.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.08230.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Ranking-aware Continual Learning for LiDAR Place Recognition</span>
        <span class="paper-authors">Xufei Wang et.al.</span>
        <span class="paper-meta">Updated 2025-05-12</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.07198">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.07198.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.07198.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Scalable Aerial GNSS Localization for Marine Robots</span>
        <span class="paper-authors">Shuo Wen et.al.</span>
        <span class="paper-meta">Updated 2025-05-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.04095">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.04095.pdf">PDF</a>
          <a class="chip" href="https://github.com/stevvwen/aerial_gnss">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.04095.pdf">
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
        <span class="paper-title">AquaticVision: Benchmarking Visual SLAM in Underwater Environment with Events and Frames</span>
        <span class="paper-authors">Yifan Peng et.al.</span>
        <span class="paper-meta">Updated 2025-05-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.03448">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.03448.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.03448.pdf">
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
        <span class="paper-title">LiDAR-Inertial SLAM-Based Navigation and Safety-Oriented AI-Driven Control System for Skid-Steer Robots</span>
        <span class="paper-authors">Mehdi Heydari Shahna et.al.</span>
        <span class="paper-meta">Updated 2025-05-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.02598">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.02598.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.02598.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Robust Localization, Mapping, and Navigation for Quadruped Robots</span>
        <span class="paper-authors">Dyuman Aditya et.al.</span>
        <span class="paper-meta">Updated 2025-05-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.02272">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.02272.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.02272.pdf">
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
        <span class="paper-meta">Updated 2025-05-04</span>
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
        <span class="paper-title">GauS-SLAM: Dense RGB-D SLAM with Gaussian Surfels</span>
        <span class="paper-authors">Yongxin Su et.al.</span>
        <span class="paper-meta">Updated 2025-05-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.01934">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.01934.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.01934.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Tightly Coupled Range Inertial Odometry and Mapping with Exact Point Cloud Downsampling</span>
        <span class="paper-authors">Kenji Koide et.al.</span>
        <span class="paper-meta">Updated 2025-05-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.01017">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.01017.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.01017.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">An Underwater, Fault-Tolerant, Laser-Aided Robotic Multi-Modal Dense SLAM System for Continuous Underwater In-Situ Observation</span>
        <span class="paper-authors">Yaming Ou et.al.</span>
        <span class="paper-meta">Updated 2025-04-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.21826">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.21826.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.21826.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">eNCApsulate: NCA for Precision Diagnosis on Capsule Endoscopes</span>
        <span class="paper-authors">Henry John Krumb et.al.</span>
        <span class="paper-meta">Updated 2025-04-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.21562">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.21562.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.21562.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Transformation &amp; Translation Occupancy Grid Mapping: 2-Dimensional Deep Learning Refined SLAM</span>
        <span class="paper-authors">Leon Davies et.al.</span>
        <span class="paper-meta">Updated 2025-04-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.19654">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.19654.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.19654.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GAN-SLAM: Real-Time GAN Aided Floor Plan Creation Through SLAM</span>
        <span class="paper-authors">Leon Davies et.al.</span>
        <span class="paper-meta">Updated 2025-04-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.19653">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.19653.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.19653.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GSFF-SLAM: 3D Semantic Gaussian Splatting SLAM via Feature Field</span>
        <span class="paper-authors">Zuxing Lu et.al.</span>
        <span class="paper-meta">Updated 2025-04-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.19409">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.19409.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.19409.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Beyond Physical Reach: Comparing Head- and Cane-Mounted Cameras for Last-Mile Navigation by Blind Users</span>
        <span class="paper-authors">Apurv Varshney et.al.</span>
        <span class="paper-meta">Updated 2025-04-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.19345">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.19345.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.19345.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">NANO-SLAM : Natural Gradient Gaussian Approximation for Vehicle SLAM</span>
        <span class="paper-authors">Tianyi Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-04-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.19195">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.19195.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.19195.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MISO: Multiresolution Submap Optimization for Efficient Globally Consistent Neural Implicit Reconstruction</span>
        <span class="paper-authors">Yulun Tian et.al.</span>
        <span class="paper-meta">Updated 2025-04-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.19104">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.19104.pdf">PDF</a>
          <a class="chip" href="https://github.com/ExistentialRobotics/MISO">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.19104.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Certifiably-Correct Mapping for Safe Navigation Despite Odometry Drift</span>
        <span class="paper-authors">Devansh R. Agrawal et.al.</span>
        <span class="paper-meta">Updated 2025-04-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.18713">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.18713.pdf">PDF</a>
          <a class="chip" href="https://github.com/dasc-lab/certifiably-correct-mapping">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.18713.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Range-based 6-DoF Monte Carlo SLAM with Gradient-guided Particle Filter on GPU</span>
        <span class="paper-authors">Takumi Nakao et.al.</span>
        <span class="paper-meta">Updated 2025-04-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.18056">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.18056.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.18056.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Autonomous Navigation Of Quadrupeds Using Coverage Path Planning</span>
        <span class="paper-authors">Alexander James Becoy et.al.</span>
        <span class="paper-meta">Updated 2025-04-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.17880">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.17880.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.17880.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">BIM-Constrained Optimization for Accurate Localization and Deviation Correction in Construction Monitoring</span>
        <span class="paper-authors">Asier Bikandi et.al.</span>
        <span class="paper-meta">Updated 2025-04-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.17693">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.17693.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.17693.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Occlusion-Aware Self-Supervised Monocular Depth Estimation for Weak-Texture Endoscopic Images</span>
        <span class="paper-authors">Zebo Huang et.al.</span>
        <span class="paper-meta">Updated 2025-04-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.17582">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.17582.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.17582.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Bias-Eliminated PnP for Stereo Visual Odometry: Provably Consistent and Large-Scale Localization</span>
        <span class="paper-authors">Guangyang Zeng et.al.</span>
        <span class="paper-meta">Updated 2025-04-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.17410">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.17410.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.17410.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ToF-Splatting: Dense SLAM using Sparse Time-of-Flight Depth and Multi-Frame Integration</span>
        <span class="paper-authors">Andrea Conti et.al.</span>
        <span class="paper-meta">Updated 2025-04-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.16545">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.16545.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.16545.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SLAM-Based Navigation and Fault Resilience in a Surveillance Quadcopter with Embedded Vision Systems</span>
        <span class="paper-authors">Abhishek Tyagi et.al.</span>
        <span class="paper-meta">Updated 2025-04-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.15305">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.15305.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.15305.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DERD-Net: Learning Depth from Event-based Ray Densities</span>
        <span class="paper-authors">Diego de Oliveira Hitzges et.al.</span>
        <span class="paper-meta">Updated 2025-04-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.15863">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.15863.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.15863.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Back on Track: Bundle Adjustment for Dynamic Scene Reconstruction</span>
        <span class="paper-authors">Weirong Chen et.al.</span>
        <span class="paper-meta">Updated 2025-04-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.14516">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.14516.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.14516.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SG-Reg: Generalizable and Efficient Scene Graph Registration</span>
        <span class="paper-authors">Chuhao Liu et.al.</span>
        <span class="paper-meta">Updated 2025-04-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.14440">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.14440.pdf">PDF</a>
          <a class="chip" href="https://github.com/hkust-aerial-robotics/sg-reg">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.14440.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Unreal Robotics Lab: A High-Fidelity Robotics Simulator with Advanced Physics and Rendering</span>
        <span class="paper-authors">Jonathan Embley-Riches et.al.</span>
        <span class="paper-meta">Updated 2025-04-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.14135">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.14135.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.14135.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Doppler-SLAM: Doppler-Aided Radar-Inertial and LiDAR-Inertial Simultaneous Localization and Mapping</span>
        <span class="paper-authors">Dong Wang et.al.</span>
        <span class="paper-meta">Updated 2025-04-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.11634">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.11634.pdf">PDF</a>
          <a class="chip" href="https://github.com/wayne-dwa/doppler-slam">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.11634.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">An Online Adaptation Method for Robust Depth Estimation and Visual Odometry in the Open World</span>
        <span class="paper-authors">Xingwu Ji et.al.</span>
        <span class="paper-meta">Updated 2025-04-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.11698">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.11698.pdf">PDF</a>
          <a class="chip" href="https://github.com/jixingwu/sol-slam">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.11698.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Region Based SLAM-Aware Exploration: Efficient and Robust Autonomous Mapping Strategy That Can Scale</span>
        <span class="paper-authors">Megha Maheshwari et.al.</span>
        <span class="paper-meta">Updated 2025-04-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.10416">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.10416.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.10416.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">RoboCup Rescue 2025 Team Description Paper UruBots</span>
        <span class="paper-authors">Kevin Farias et.al.</span>
        <span class="paper-meta">Updated 2025-04-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.09778">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.09778.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.09778.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FindAnything: Open-Vocabulary and Object-Centric Mapping for Robot Exploration in Any Environment</span>
        <span class="paper-authors">Sebastián Barbas Laina et.al.</span>
        <span class="paper-meta">Updated 2025-04-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.08603">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.08603.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.08603.pdf">
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
        <span class="paper-title">II-NVM: Enhancing Map Accuracy and Consistency with Normal Vector-Assisted Mapping</span>
        <span class="paper-authors">Chengwei Zhao et.al.</span>
        <span class="paper-meta">Updated 2025-04-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.08204">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.08204.pdf">PDF</a>
          <a class="chip" href="https://github.com/chengwei0427/ii-nvm">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.08204.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">UWB Anchor Based Localization of a Planetary Rover</span>
        <span class="paper-authors">Andreas Nüchter et.al.</span>
        <span class="paper-meta">Updated 2025-04-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.07658">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.07658.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.07658.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Event Signal Filtering via Probability Flux Estimation</span>
        <span class="paper-authors">Jinze Chen et.al.</span>
        <span class="paper-meta">Updated 2025-04-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.07503">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.07503.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.07503.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Embracing Dynamics: Dynamics-aware 4D Gaussian Splatting SLAM</span>
        <span class="paper-authors">Zhicong Sun et.al.</span>
        <span class="paper-meta">Updated 2025-04-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.04844">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.04844.pdf">PDF</a>
          <a class="chip" href="https://github.com/zhicongsun/d4dgs-slam">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.04844.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SELC: Self-Supervised Efficient Local Correspondence Learning for Low Quality Images</span>
        <span class="paper-authors">Yuqing Wang et.al.</span>
        <span class="paper-meta">Updated 2025-04-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.04497">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.04497.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.04497.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">VSLAM-LAB: A Comprehensive Framework for Visual SLAM Methods and Datasets</span>
        <span class="paper-authors">Alejandro Fontan et.al.</span>
        <span class="paper-meta">Updated 2025-04-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.04457">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.04457.pdf">PDF</a>
          <a class="chip" href="https://github.com/alejandrofontan/vslam-lab">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.04457.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Nonlinear Observer Design for Landmark-Inertial Simultaneous Localization and Mapping</span>
        <span class="paper-authors">Mouaad Boughellaba et.al.</span>
        <span class="paper-meta">Updated 2025-04-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.04239">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.04239.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.04239.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">WildGS-SLAM: Monocular Gaussian Splatting SLAM in Dynamic Environments</span>
        <span class="paper-authors">Jianhao Zheng et.al.</span>
        <span class="paper-meta">Updated 2025-04-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.03886">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.03886.pdf">PDF</a>
          <a class="chip" href="https://github.com/GradientSpaces/WildGS-SLAM">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.03886.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SLACK: Attacking LiDAR-based SLAM with Adversarial Point Injections</span>
        <span class="paper-authors">Prashant Kumar et.al.</span>
        <span class="paper-meta">Updated 2025-04-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.03089">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.03089.pdf">PDF</a>
          <a class="chip" href="https://github.com/Kunaldargan/slack_attack_ICIP">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.03089.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Multimodal Fusion and Vision-Language Models: A Survey for Robot Vision</span>
        <span class="paper-authors">Xiaofeng Han et.al.</span>
        <span class="paper-meta">Updated 2025-04-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.02477">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.02477.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.02477.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MonoGS++: Fast and Accurate Monocular RGB Gaussian SLAM</span>
        <span class="paper-authors">Renwu Li et.al.</span>
        <span class="paper-meta">Updated 2025-04-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.02437">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.02437.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.02437.pdf">
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
        <span class="paper-title">Strengthening Multi-Robot Systems for SAR: Co-Designing Robotics and Communication Towards 6G</span>
        <span class="paper-authors">Juan Bravo-Arrabal et.al.</span>
        <span class="paper-meta">Updated 2025-04-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.01940">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.01940.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.01940.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Dynamic Initialization for LiDAR-inertial SLAM</span>
        <span class="paper-authors">Jie Xu et.al.</span>
        <span class="paper-meta">Updated 2025-04-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.01451">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.01451.pdf">PDF</a>
          <a class="chip" href="https://github.com/lian-yue0515/d-li-init">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.01451.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ForestVO: Enhancing Visual Odometry in Forest Environments through ForestGlue</span>
        <span class="paper-authors">Thomas Pritchard et.al.</span>
        <span class="paper-meta">Updated 2025-04-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.01261">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.01261.pdf">PDF</a>
          <a class="chip" href="https://github.com/aerialroboticsgroup/forest-vo">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.01261.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Semantic SLAM with Rolling-Shutter Cameras and Low-Precision INS in Outdoor Environments</span>
        <span class="paper-authors">Yuchen Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-04-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.01997">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.01997.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.01997.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SuperEvent: Cross-Modal Learning of Event-based Keypoint Detection</span>
        <span class="paper-authors">Yannick Burkhardt et.al.</span>
        <span class="paper-meta">Updated 2025-03-31</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.00139">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.00139.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.00139.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A Visual-Inertial Motion Prior SLAM for Dynamic Environments</span>
        <span class="paper-authors">Weilong Sun et.al.</span>
        <span class="paper-meta">Updated 2025-03-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.23429">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.23429.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.23429.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">HS-SLAM: Hybrid Representation with Structural Supervision for Improved Dense SLAM</span>
        <span class="paper-authors">Ziren Gong et.al.</span>
        <span class="paper-meta">Updated 2025-03-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.21778">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.21778.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.21778.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">STAMICS: Splat, Track And Map with Integrated Consistency and Semantics for Dense RGB-D SLAM</span>
        <span class="paper-authors">Yongxu Wang et.al.</span>
        <span class="paper-meta">Updated 2025-03-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.21425">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.21425.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.21425.pdf">
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
          <span class="chip ghost">Code: N/A</span>
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
        <span class="paper-title">First Results on UAV-aided User Localization Using ToA and OpenAirInterface in 5G NR</span>
        <span class="paper-authors">Omid Esrafilian et.al.</span>
        <span class="paper-meta">Updated 2025-03-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.19529">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.19529.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.19529.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MM-LINS: a Multi-Map LiDAR-Inertial System for Over-Degenerate Environments</span>
        <span class="paper-authors">Yongxin Ma et.al.</span>
        <span class="paper-meta">Updated 2025-03-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.19506">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.19506.pdf">PDF</a>
          <a class="chip" href="https://github.com/lian-yue0515/MM-LINS">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.19506.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Cooperative Control of Multi-Quadrotors for Transporting Cable-Suspended Payloads: Obstacle-Aware Planning and Event-Based Nonlinear Model Predictive Control</span>
        <span class="paper-authors">Tohid Kargar Tasooji et.al.</span>
        <span class="paper-meta">Updated 2025-03-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.19135">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.19135.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.19135.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GI-SLAM: Gaussian-Inertial SLAM</span>
        <span class="paper-authors">Xulang Liu et.al.</span>
        <span class="paper-meta">Updated 2025-03-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.18275">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.18275.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.18275.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LightLoc: Learning Outdoor LiDAR Localization at Light Speed</span>
        <span class="paper-authors">Wen Li et.al.</span>
        <span class="paper-meta">Updated 2025-03-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.17814">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.17814.pdf">PDF</a>
          <a class="chip" href="https://github.com/liw95/lightloc">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.17814.pdf">
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
        <span class="paper-title">4D Gaussian Splatting SLAM</span>
        <span class="paper-authors">Yanyan Li et.al.</span>
        <span class="paper-meta">Updated 2025-03-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.16710">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.16710.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.16710.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Speeding up design and making to reduce time-to-project and time-to-market: an AI-Enhanced approach in engineering education</span>
        <span class="paper-authors">Giovanni Adorni et.al.</span>
        <span class="paper-meta">Updated 2025-03-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.16307">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.16307.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.16307.pdf">
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
        <span class="paper-title">A Sigma Point-based Low Complexity Algorithm for Multipath-based SLAM in MIMO Systems</span>
        <span class="paper-authors">Anna Masiero et.al.</span>
        <span class="paper-meta">Updated 2025-03-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.15286">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.15286.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.15286.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ChatStitch: Visualizing Through Structures via Surround-View Unsupervised Deep Image Stitching with Collaborative LLM-Agents</span>
        <span class="paper-authors">Hao Liang et.al.</span>
        <span class="paper-meta">Updated 2025-03-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.14948">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.14948.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.14948.pdf">
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
        <span class="paper-title">GeoFlow-SLAM: A Robust Tightly-Coupled RGBD-Inertial Fusion SLAM for Dynamic Legged Robotics</span>
        <span class="paper-authors">Tingyang Xiao et.al.</span>
        <span class="paper-meta">Updated 2025-03-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.14247">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.14247.pdf">PDF</a>
          <a class="chip" href="https://github.com/nsn-hello/geoflow-slam">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.14247.pdf">
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
        <span class="paper-title">Digital Beamforming Enhanced Radar Odometry</span>
        <span class="paper-authors">Jingqi Jiang et.al.</span>
        <span class="paper-meta">Updated 2025-03-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.13252">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.13252.pdf">PDF</a>
          <a class="chip" href="https://github.com/SenseRoboticsLab/DBE-Radar">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.13252.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Dynamic-Dark SLAM: RGB-Thermal Cooperative Robot Vision Strategy for Multi-Person Tracking in Both Well-Lit and Low-Light Scenes</span>
        <span class="paper-authors">Tatsuro Sakai et.al.</span>
        <span class="paper-meta">Updated 2025-03-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.12768">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.12768.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.12768.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">KISS-SLAM: A Simple, Robust, and Accurate 3D LiDAR SLAM System With Enhanced Generalization Capabilities</span>
        <span class="paper-authors">Tiziano Guadagnino et.al.</span>
        <span class="paper-meta">Updated 2025-03-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.12660">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.12660.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.12660.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Deblur Gaussian Splatting SLAM</span>
        <span class="paper-authors">Francesco Girlanda et.al.</span>
        <span class="paper-meta">Updated 2025-03-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.12572">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.12572.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.12572.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">M2UD: A Multi-model, Multi-scenario, Uneven-terrain Dataset for Ground Robot with Localization and Mapping Evaluation</span>
        <span class="paper-authors">Yanpeng Jia et.al.</span>
        <span class="paper-meta">Updated 2025-03-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.12387">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.12387.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.12387.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">OSMa-Bench: Evaluating Open Semantic Mapping Under Varying Lighting Conditions</span>
        <span class="paper-authors">Maxim Popov et.al.</span>
        <span class="paper-meta">Updated 2025-03-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.10331">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.10331.pdf">PDF</a>
          <a class="chip" href="https://github.com/be2rlab/OSMa-Bench">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.10331.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Online Language Splatting</span>
        <span class="paper-authors">Saimouli Katragadda et.al.</span>
        <span class="paper-meta">Updated 2025-03-12</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.09447">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.09447.pdf">PDF</a>
          <a class="chip" href="https://github.com/rpng/online_lang_splatting">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.09447.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MonoSLAM: Robust Monocular SLAM with Global Structure Optimization</span>
        <span class="paper-authors">Bingzheng Jiang et.al.</span>
        <span class="paper-meta">Updated 2025-03-12</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.09296">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.09296.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.09296.pdf">
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
        <span class="paper-title">GigaSLAM: Large-Scale Monocular SLAM with Hierachical Gaussian Splats</span>
        <span class="paper-authors">Kai Deng et.al.</span>
        <span class="paper-meta">Updated 2025-03-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.08071">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.08071.pdf">PDF</a>
          <a class="chip" href="https://github.com/DengKaiCQ/GigaSLAM">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.08071.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">POp-GS: Next Best View in 3D-Gaussian Splatting with P-Optimality</span>
        <span class="paper-authors">Joey Wilson et.al.</span>
        <span class="paper-meta">Updated 2025-03-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.07819">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.07819.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.07819.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">AirSwarm: Enabling Cost-Effective Multi-UAV Research with COTS drones</span>
        <span class="paper-authors">Xiaowei Li et.al.</span>
        <span class="paper-meta">Updated 2025-03-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.06890">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.06890.pdf">PDF</a>
          <a class="chip" href="https://github.com/vvEverett/tello_ros">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.06890.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">HIPPO-MAT: Decentralized Task Allocation Using GraphSAGE and Multi-Agent Deep Reinforcement Learning</span>
        <span class="paper-authors">Lavanya Ratnabala et.al.</span>
        <span class="paper-meta">Updated 2025-03-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.07662">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.07662.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.07662.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">InfoFusion Controller: Informed TRRT Star with Mutual Information based on Fusion of Pure Pursuit and MPC for Enhanced Path Planning</span>
        <span class="paper-authors">Seongjun Choi et.al.</span>
        <span class="paper-meta">Updated 2025-03-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.06010">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.06010.pdf">PDF</a>
          <a class="chip" href="https://github.com/drawingprocess/infofusioncontroller">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.06010.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">THE-SEAN: A Heart Rate Variation-Inspired Temporally High-Order Event-Based Visual Odometry with Self-Supervised Spiking Event Accumulation Networks</span>
        <span class="paper-authors">Chaoran Xiong et.al.</span>
        <span class="paper-meta">Updated 2025-03-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.05112">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.05112.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.05112.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
</section>
