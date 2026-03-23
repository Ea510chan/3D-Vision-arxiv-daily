---
layout: default
title: NeRF
---

<section class="topic-hero" style="--accent: #00ffa3;">
  <div>
    <p class="eyebrow">Topic</p>
    <h1>NeRF</h1>
    <p class="topic-lede">Updated 2026.03.23 · 318 papers</p>
  </div>
  <a class="btn ghost" href="../index.html#topics">← Back to topics</a>
</section>

<section class="paper-grid">
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Neural Radiance Maps for Extraterrestrial Navigation and Path Planning</span>
        <span class="paper-authors">Adam Dai, Shubh Gupta, Grace Gao</span>
        <span class="paper-meta">Updated 2026-03-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Autonomous vehicles such as the Mars rovers currently lead the vanguard of surface exploration on extraterrestrial planets and moons. In order to accelerate the pace of exploration and science objectives, it is critical to plan safe and efficient paths for these vehicles. However, current rover autonomy is limited by a lack of global maps which can be easily constructed and stored for onboard re-planning. Recently, Neural Radiance Fields (NeRFs) have been introduced as a detailed 3D scene representation which can be trained from sparse 2D images and efficiently stored. We propose to use NeRFs to construct maps for online use in autonomous navigation, and present a planning framework which leverages the NeRF map to integrate local and global information. Our approach interpolates local cost observations across global regions using kernel ridge regression over terrain features extracted from the NeRF map, allowing the rover to re-route itself around untraversable areas discovered during online operation. We validate our approach in high-fidelity simulation and demonstrate lower cost and higher percentage success rate path planning compared to various baselines.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.17236">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.17236.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.17236.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">E2EGS: Event-to-Edge Gaussian Splatting for Pose-Free 3D Reconstruction</span>
        <span class="paper-authors">Yunsoo Kim, Changki Sung, Dasol Hong, Hyun Myung</span>
        <span class="paper-meta">Updated 2026-03-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">The emergence of neural radiance fields (NeRF) and 3D Gaussian splatting (3DGS) has advanced novel view synthesis (NVS). These methods, however, require high-quality RGB inputs and accurate corresponding poses, limiting robustness under real-world conditions such as fast camera motion or adverse lighting. Event cameras, which capture brightness changes at each pixel with high temporal resolution and wide dynamic range, enable precise sensing of dynamic scenes and offer a promising solution. However, existing event-based NVS methods either assume known poses or rely on depth estimation models that are bounded by their initial observations, failing to generalize as the camera traverses previously unseen regions. We present E2EGS, a pose-free framework operating solely on event streams. Our key insight is that edge information provides rich structural cues essential for accurate trajectory estimation and high-quality NVS. To extract edges from noisy event streams, we exploit the distinct spatio-temporal characteristics of edges and non-edge regions. The event camera&#x27;s movement induces consistent events along edges, while non-edge regions produce sparse noise. We leverage this through a patch-based temporal coherence analysis that measures local variance to extract edges while robustly suppressing noise. The extracted edges guide structure-aware Gaussian initialization and enable edge-weighted losses throughout initialization, tracking, and bundle adjustment. Extensive experiments on both synthetic and real datasets demonstrate that E2EGS achieves superior reconstruction quality and trajectory accuracy, establishing a fully pose-free paradigm for event-based 3D reconstruction.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.14684">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.14684.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.14684.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Spectral-Geometric Neural Fields for Pose-Free LiDAR View Synthesis</span>
        <span class="paper-authors">Yinuo Jiang, Jun Cheng, Yiran Wang, Cheng Cheng</span>
        <span class="paper-meta">Updated 2026-03-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Neural Radiance Fields (NeRF) have shown remarkable success in image novel view synthesis (NVS), inspiring extensions to LiDAR NVS. However, most methods heavily rely on accurate camera poses for scene reconstruction. The sparsity and textureless nature of LiDAR data also present distinct challenges, leading to geometric holes and discontinuous surfaces. To address these issues, we propose SG-NLF, a pose-free LiDAR NeRF framework that integrates spectral information with geometric consistency. Specifically, we design a hybrid representation based on spectral priors to reconstruct smooth geometry. For pose optimization, we construct a confidence-aware graph based on feature compatibility to achieve global alignment. In addition, an adversarial learning strategy is introduced to enforce cross-frame consistency, thereby enhancing reconstruction quality. Comprehensive experiments demonstrate the effectiveness of our framework, especially in challenging low-frequency scenarios. Compared to previous state-of-the-art methods, SG-NLF improves reconstruction quality and pose accuracy by over 35.8% and 68.8%. Our work can provide a novel perspective for LiDAR view synthesis.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.12903">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.12903.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.12903.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Catalyst4D: High-Fidelity 3D-to-4D Scene Editing via Dynamic Propagation</span>
        <span class="paper-authors">Shifeng Chen, Yihui Li, Jun Liao, Hongyu Yang, Di Huang</span>
        <span class="paper-meta">Updated 2026-03-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Recent advances in 3D scene editing using NeRF and 3DGS enable high-quality static scene editing. In contrast, dynamic scene editing remains challenging, as methods that directly extend 2D diffusion models to 4D often produce motion artifacts, temporal flickering, and inconsistent style propagation. We introduce Catalyst4D, a framework that transfers high-quality 3D edits to dynamic 4D Gaussian scenes while maintaining spatial and temporal coherence. At its core, Anchor-based Motion Guidance (AMG) builds a set of structurally stable and spatially representative anchors from both original and edited Gaussians. These anchors serve as robust region-level references, and their correspondences are established via optimal transport to enable consistent deformation propagation without cross-region interference or motion drift. Complementarily, Color Uncertainty-guided Appearance Refinement (CUAR) preserves temporal appearance consistency by estimating per-Gaussian color uncertainty and selectively refining regions prone to occlusion-induced artifacts. Extensive experiments demonstrate that Catalyst4D achieves temporally stable, high-fidelity dynamic scene editing and outperforms existing methods in both visual quality and motion coherence.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.12766">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.12766.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.12766.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Node-RF: Learning Generalized Continuous Space-Time Scene Dynamics with Neural ODE-based NeRFs</span>
        <span class="paper-authors">Hiran Sarkar, Liming Kuang, Yordanka Velikova, Benjamin Busam</span>
        <span class="paper-meta">Updated 2026-03-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Predicting scene dynamics from visual observations is challenging. Existing methods capture dynamics only within observed boundaries failing to extrapolate far beyond the training sequence. Node-RF (Neural ODE-based NeRF) overcomes this limitation by integrating Neural Ordinary Differential Equations (NODEs) with dynamic Neural Radiance Fields (NeRFs), enabling a continuous-time, spatiotemporal representation that generalizes beyond observed trajectories at constant memory cost. From visual input, Node-RF learns an implicit scene state that evolves over time via an ODE solver, propagating feature embeddings via differential calculus. A NeRF-based renderer interprets calculated embeddings to synthesize arbitrary views for long-range extrapolation. Training on multiple motion sequences with shared dynamics allows for generalization to unseen conditions. Our experiments demonstrate that Node-RF can characterize abstract system behavior without explicit model to identify critical points for future predictions.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.12078">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.12078.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.12078.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DenoiseSplat: Feed-Forward Gaussian Splatting for Noisy 3D Scene Reconstruction</span>
        <span class="paper-authors">Fuzhen Jiang, Zhuoran Li, Yinlin Zhang</span>
        <span class="paper-meta">Updated 2026-03-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">3D scene reconstruction and novel-view synthesis are fundamental for VR, robotics, and content creation. However, most NeRF and 3D Gaussian Splatting pipelines assume clean inputs and degrade under real noise and artifacts. We therefore propose DenoiseSplat, a feed-forward 3D Gaussian splatting method for noisy multi-view images. We build a large-scale, scene-consistent noisy--clean benchmark on RE10K by injecting Gaussian, Poisson, speckle, and salt-and-pepper noise with controlled intensities. With a lightweight MVSplat-style feed-forward backbone, we train end-to-end using only clean 2D renderings as supervision and no 3D ground truth. On noisy RE10K, DenoiseSplat outperforms vanilla MVSplat and a strong two-stage baseline (IDF + MVSplat) in PSNR/SSIM and LPIPS across noise types and levels.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.09291">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.09291.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.09291.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Speeding Up the Learning of 3D Gaussians with Much Shorter Gaussian Lists</span>
        <span class="paper-authors">Jiaqi Liu, Zhizhong Han</span>
        <span class="paper-meta">Updated 2026-03-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">3D Gaussian splatting (3DGS) has become a vital tool for learning a radiance field from multiple posed images. Although 3DGS shows great advantages over NeRF in terms of rendering quality and efficiency, it remains a research challenge to further improve the efficiency of learning 3D Gaussians. To overcome this challenge, we propose novel training strategies and losses to shorten each Gaussian list used to render a pixel, which speeds up the splatting by involving fewer Gaussians along a ray. Specifically, we shrink the size of each Gaussian by resetting their scales regularly, encouraging smaller Gaussians to cover fewer nearby pixels, which shortens the Gaussian lists of pixels. Additionally, we introduce an entropy constraint on the alpha blending procedure to sharpen the weight distribution of Gaussians along each ray, which drives dominant weights larger while making minor weights smaller. As a result, each Gaussian becomes more focused on the pixels where it is dominant, which reduces its impact on nearby pixels, leading to even shorter Gaussian lists. Eventually, we integrate our method into a rendering resolution scheduler which further improves efficiency through progressive resolution increase. We evaluate our method by comparing it with state-of-the-art methods on widely used benchmarks. Our results show significant advantages over others in efficiency without sacrificing rendering quality.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.09277">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.09277.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.09277.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SkipGS: Post-Densification Backward Skipping for Efficient 3DGS Training</span>
        <span class="paper-authors">Jingxing Li, Yongjae Leeand, Deliang Fan</span>
        <span class="paper-meta">Updated 2026-03-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">3D Gaussian Splatting (3DGS) achieves real-time novel-view synthesis by optimizing millions of anisotropic Gaussians, yet its training remains expensive, with the backward pass dominating runtime in the post-densification refinement phase. We observe substantial update redundancy in this phase: many sampled views have near-plateaued losses and provide diminishing gradient benefits, but standard training still runs full backpropagation. We propose SkipGS with a novel view-adaptive backward gating mechanism for efficient post-densification training. SkipGS always performs the forward pass to update per-view loss statistics, and selectively skips backward passes when the sampled view&#x27;s loss is consistent with its recent per-view baseline, while enforcing a minimum backward budget for stable optimization. On Mip-NeRF 360, compared to 3DGS, SkipGS reduces end-to-end training time by 23.1%, driven by a 42.0% reduction in post-densification time, with comparable reconstruction quality. Because it only changes when to backpropagate -- without modifying the renderer, representation, or loss -- SkipGS is plug-and-play and compatible with other complementary efficiency strategies for additive speedups.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.08997">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.08997.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.08997.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Fast Low-light Enhancement and Deblurring for 3D Dark Scenes</span>
        <span class="paper-authors">Feng Zhang, Jinglong Wang, Ze Li, Yanghong Zhou, Yang Chen, Lei Chen, Xiatian Zhu</span>
        <span class="paper-meta">Updated 2026-03-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Novel view synthesis from low-light, noisy, and motion-blurred imagery remains a valuable and challenging task. Current volumetric rendering methods struggle with compound degradation, and sequential 2D preprocessing introduces artifacts due to interdependencies. In this work, we introduce FLED-GS, a fast low-light enhancement and deblurring framework that reformulates 3D scene restoration as an alternating cycle of enhancement and reconstruction. Specifically, FLED-GS inserts several intermediate brightness anchors to enable progressive recovery, preventing noise blow-up from harming deblurring or geometry. Each iteration sharpens inputs with an off-the-shelf 2D deblurrer and then performs noise-aware 3DGS reconstruction that estimates and suppresses noise while producing clean priors for the next level. Experiments show FLED-GS outperforms state-of-the-art LuSh-NeRF, achieving 21$\times$ faster training and 11$\times$ faster rendering.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.08133">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.08133.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.08133.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FTSplat: Feed-forward Triangle Splatting Network</span>
        <span class="paper-authors">Xiong Jinlin, Li Can, Shen Jiawei, Qi Zhigang, Sun Lei, Zhao Dongyang</span>
        <span class="paper-meta">Updated 2026-03-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">High-fidelity three-dimensional (3D) reconstruction is essential for robotics and simulation. While Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) achieve impressive rendering quality, their reliance on time-consuming per-scene optimization limits real-time deployment. Emerging feed-forward Gaussian splatting methods improve efficiency but often lack explicit, manifold geometry required for direct simulation. To address these limitations, we propose a feed-forward framework for triangle primitive generation that directly predicts continuous triangle surfaces from calibrated multi-view images. Our method produces simulation-ready models in a single forward pass, obviating the need for per-scene optimization or post-processing. We introduce a pixel-aligned triangle generation module and incorporate relative 3D point cloud supervision to enhance geometric learning stability and consistency. Experiments demonstrate that our method achieves efficient reconstruction while maintaining seamless compatibility with standard graphics and robotic simulators.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.05932">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.05932.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.05932.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Towards 3D Scene Understanding of Gas Plumes in LWIR Hyperspectral Images Using Neural Radiance Fields</span>
        <span class="paper-authors">Scout Jarman, Zigfried Hampel-Arias, Adra Carr, Kevin R. Moon</span>
        <span class="paper-meta">Updated 2026-03-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Hyperspectral images (HSI) have many applications, ranging from environmental monitoring to national security, and can be used for material detection and identification. Longwave infrared (LWIR) HSI can be used for gas plume detection and analysis. Oftentimes, only a few images of a scene of interest are available and are analyzed individually. The ability to combine information from multiple images into a single, cohesive representation could enhance analysis by providing more context on the scene&#x27;s geometry and spectral properties. Neural radiance fields (NeRFs) create a latent neural representation of volumetric scene properties that enable novel-view rendering and geometry reconstruction, offering a promising avenue for hyperspectral 3D scene reconstruction. We explore the possibility of using NeRFs to create 3D scene reconstructions from LWIR HSI and demonstrate that the model can be used for the basic downstream analysis task of gas plume detection. The physics-based DIRSIG software suite was used to generate a synthetic multi-view LWIR HSI dataset of a simple facility with a strong sulfur hexafluoride gas plume. Our method, built on the standard Mip-NeRF architecture, combines state-of-the-art methods for hyperspectral NeRFs and sparse-view NeRFs, along with a novel adaptive weighted MSE loss. Our final NeRF method requires around 50% fewer training images than the standard Mip-NeRF and achieves an average PSNR of 39.8 dB with as few as 30 training images. Gas plume detection applied to NeRF-rendered test images using the adaptive coherence estimator achieves an average AUC of 0.821 when compared with detection masks generated from ground-truth test images.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.05473">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.05473.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.05473.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GloSplat: Joint Pose-Appearance Optimization for Faster and More Accurate 3D Reconstruction</span>
        <span class="paper-authors">Tianyu Xiong, Rui Li, Linjie Li, Jiaqi Yang</span>
        <span class="paper-meta">Updated 2026-03-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Feature extraction, matching, structure from motion (SfM), and novel view synthesis (NVS) have traditionally been treated as separate problems with independent optimization objectives. We present GloSplat, a framework that performs \emph{joint pose-appearance optimization} during 3D Gaussian Splatting training. Unlike prior joint optimization methods (BARF, NeRF--, 3RGS) that rely purely on photometric gradients for pose refinement, GloSplat preserves \emph{explicit SfM feature tracks} as first-class entities throughout training: track 3D points are maintained as separate optimizable parameters from Gaussian primitives, providing persistent geometric anchors via a reprojection loss that operates alongside photometric supervision. This architectural choice prevents early-stage pose drift while enabling fine-grained refinement -- a capability absent in photometric-only approaches. We introduce two pipeline variants: (1) \textbf{GloSplat-F}, a COLMAP-free variant using retrieval-based pair selection for efficient reconstruction, and (2) \textbf{GloSplat-A}, an exhaustive matching variant for maximum quality. Both employ global SfM initialization followed by joint photometric-geometric optimization during 3DGS training. Experiments demonstrate that GloSplat-F achieves state-of-the-art among COLMAP-free methods while GloSplat-A surpasses all COLMAP-based baselines.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.04847">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.04847.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.04847.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">R3GW: Relightable 3D Gaussians for Outdoor Scenes in the Wild</span>
        <span class="paper-authors">Margherita Lea Corona, Wieland Morgenstern, Peter Eisert, Anna Hilsmann</span>
        <span class="paper-meta">Updated 2026-03-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">3D Gaussian Splatting (3DGS) has established itself as a leading technique for 3D reconstruction and novel view synthesis of static scenes, achieving outstanding rendering quality and fast training. However, the method does not explicitly model the scene illumination, making it unsuitable for relighting tasks. Furthermore, 3DGS struggles to reconstruct scenes captured in the wild by unconstrained photo collections featuring changing lighting conditions. In this paper, we present R3GW, a novel method that learns a relightable 3DGS representation of an outdoor scene captured in the wild. Our approach separates the scene into a relightable foreground and a non-reflective background (the sky), using two distinct sets of Gaussians. R3GW models view-dependent lighting effects in the foreground reflections by combining Physically Based Rendering with the 3DGS scene representation in a varying illumination setting. We evaluate our method quantitatively and qualitatively on the NeRF-OSR dataset, offering state-of-the-art performance and enhanced support for physically-based relighting of unconstrained scenes. Our method synthesizes photorealistic novel views under arbitrary illumination conditions. Additionally, our representation of the sky mitigates depth reconstruction artifacts, improving rendering quality at the sky-foreground boundary</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.02801">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.02801.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.02801.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Neural Electromagnetic Fields for High-Resolution Material Parameter Reconstruction</span>
        <span class="paper-authors">Zhe Chen, Peilin Zheng, Wenshuo Chen, Xiucheng Wang, Yutao Yue, Nan Cheng</span>
        <span class="paper-meta">Updated 2026-03-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Creating functional Digital Twins, simulatable 3D replicas of the real world, is a central challenge in computer vision. Current methods like NeRF produce visually rich but functionally incomplete twins. The key barrier is the lack of underlying material properties (e.g., permittivity, conductivity). Acquiring this information for every point in a scene via non-contact, non-invasive sensing is a primary goal, but it demands solving a notoriously ill-posed physical inversion problem. Standard remote signals, like images and radio frequencies (RF), deeply entangle the unknown geometry, ambient field, and target materials. We introduce NEMF, a novel framework for dense, non-invasive physical inversion designed to build functional digital twins. Our key insight is a systematic disentanglement strategy. NEMF leverages high-fidelity geometry from images as a powerful anchor, which first enables the resolution of the ambient field. By constraining both geometry and field using only non-invasive data, the original ill-posed problem transforms into a well-posed, physics-supervised learning task. This transformation unlocks our core inversion module: a decoder. Guided by ambient RF signals and a differentiable layer incorporating physical reflection models, it learns to explicitly output a continuous, spatially-varying field of the scene&#x27;s underlying material parameters. We validate our framework on high-fidelity synthetic datasets. Experiments show our non-invasive inversion reconstructs these material maps with high accuracy, and the resulting functional twin enables high-fidelity physical simulation. This advance moves beyond passive visual replicas, enabling the creation of truly functional and simulatable models of the physical world.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2603.02582">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2603.02582.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2603.02582.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Event-Aided Sharp Radiance Field Reconstruction for Fast-Flying Drones</span>
        <span class="paper-authors">Rong Zou, Marco Cannici, Davide Scaramuzza</span>
        <span class="paper-meta">Updated 2026-02-26</span>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Lie Flow: Video Dynamic Fields Modeling and Predicting with Lie Algebra as Geometric Physics Principle</span>
        <span class="paper-authors">Weidong Qiao, Wangmeng Zuo, Hui Li</span>
        <span class="paper-meta">Updated 2026-02-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Modeling 4D scenes requires capturing both spatial structure and temporal motion, which is challenging due to the need for physically consistent representations of complex rigid and non-rigid motions. Existing approaches mainly rely on translational displacements, which struggle to represent rotations, articulated transformations, often leading to spatial inconsistency and physically implausible motion. LieFlow, a dynamic radiance representation framework that explicitly models motion within the SE(3) Lie group, enabling coherent learning of translation and rotation in a unified geometric space. The SE(3) transformation field enforces physically inspired constraints to maintain motion continuity and geometric consistency. The evaluation includes a synthetic dataset with rigid-body trajectories and two real-world datasets capturing complex motion under natural lighting and occlusions. Across all datasets, LieFlow consistently improves view-synthesis fidelity, temporal coherence, and physical realism over NeRF-based baselines. These results confirm that SE(3)-based motion modeling offers a robust and physically grounded framework for representing dynamic 4D scenes.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.21645">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.21645.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.21645.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Augmented Radiance Field: A General Framework for Enhanced Gaussian Splatting</span>
        <span class="paper-authors">Yixin Yang, Bojian Wu, Yang Zhou, Hui Huang</span>
        <span class="paper-meta">Updated 2026-02-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Due to the real-time rendering performance, 3D Gaussian Splatting (3DGS) has emerged as the leading method for radiance field reconstruction. However, its reliance on spherical harmonics for color encoding inherently limits its ability to separate diffuse and specular components, making it challenging to accurately represent complex reflections. To address this, we propose a novel enhanced Gaussian kernel that explicitly models specular effects through view-dependent opacity. Meanwhile, we introduce an error-driven compensation strategy to improve rendering quality in existing 3DGS scenes. Our method begins with 2D Gaussian initialization and then adaptively inserts and optimizes enhanced Gaussian kernels, ultimately producing an augmented radiance field. Experiments demonstrate that our method not only surpasses state-of-the-art NeRF methods in rendering performance but also achieves greater parameter efficiency. Project page at: https://xiaoxinyyx.github.io/augs.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.19916">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.19916.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.19916.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">PhysConvex: Physics-Informed 3D Dynamic Convex Radiance Fields for Reconstruction and Simulation</span>
        <span class="paper-authors">Dan Wang, Xinrui Cui, Serge Belongie, Ravi Ramamoorthi</span>
        <span class="paper-meta">Updated 2026-02-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Reconstructing and simulating dynamic 3D scenes with both visual realism and physical consistency remains a fundamental challenge. Existing neural representations, such as NeRFs and 3DGS, excel in appearance reconstruction but struggle to capture complex material deformation and dynamics. We propose PhysConvex, a Physics-informed 3D Dynamic Convex Radiance Field that unifies visual rendering and physical simulation. PhysConvex represents deformable radiance fields using physically grounded convex primitives governed by continuum mechanics. We introduce a boundary-driven dynamic convex representation that models deformation through vertex and surface dynamics, capturing spatially adaptive, non-uniform deformation, and evolving boundaries. To efficiently simulate complex geometries and heterogeneous materials, we further develop a reduced-order convex simulation that advects dynamic convex fields using neural skinning eigenmodes as shape- and material-aware deformation bases with time-varying reduced DOFs under Newtonian dynamics. Convex dynamics also offers compact, gap-free volumetric coverage, enhancing both geometric efficiency and simulation fidelity. Experiments demonstrate that PhysConvex achieves high-fidelity reconstruction of geometry, appearance, and physical properties from videos, outperforming existing methods.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.18886">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.18886.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.18886.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Unifying Color and Lightness Correction with View-Adaptive Curve Adjustment for Robust 3D Novel View Synthesis</span>
        <span class="paper-authors">Ziteng Cui, Shuhong Liu, Xiaoyu Dong, Xuangeng Chu, Lin Gu, Ming-Hsuan Yang, Tatsuya Harada</span>
        <span class="paper-meta">Updated 2026-02-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">High-quality image acquisition in real-world environments remains challenging due to complex illumination variations and inherent limitations of camera imaging pipelines. These issues are exacerbated in multi-view capture, where differences in lighting, sensor responses, and image signal processor (ISP) configurations introduce photometric and chromatic inconsistencies that violate the assumptions of photometric consistency underlying modern 3D novel view synthesis (NVS) methods, including Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS), leading to degraded reconstruction and rendering quality. We propose Luminance-GS++, a 3DGS-based framework for robust NVS under diverse illumination conditions. Our method combines a globally view-adaptive lightness adjustment with a local pixel-wise residual refinement for precise color correction. We further design unsupervised objectives that jointly enforce lightness correction and multi-view geometric and photometric consistency. Extensive experiments demonstrate state-of-the-art performance across challenging scenarios, including low-light, overexposure, and complex luminance and chromatic variations. Unlike prior approaches that modify the underlying representation, our method preserves the explicit 3DGS formulation, improving reconstruction fidelity while maintaining real-time rendering efficiency.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.18322">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.18322.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.18322.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">HS-3D-NeRF: 3D Surface and Hyperspectral Reconstruction From Stationary Hyperspectral Images Using Multi-Channel NeRFs</span>
        <span class="paper-authors">Kibon Ku, Talukder Z. Jubery, Adarsh Krishnamurthy, Baskar Ganapathysubramanian</span>
        <span class="paper-meta">Updated 2026-02-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Advances in hyperspectral imaging (HSI) and 3D reconstruction have enabled accurate, high-throughput characterization of agricultural produce quality and plant phenotypes, both essential for advancing agricultural sustainability and breeding programs. HSI captures detailed biochemical features of produce, while 3D geometric data substantially improves morphological analysis. However, integrating these two modalities at scale remains challenging, as conventional approaches involve complex hardware setups incompatible with automated phenotyping systems. Recent advances in neural radiance fields (NeRF) offer computationally efficient 3D reconstruction but typically require moving-camera setups, limiting throughput and reproducibility in standard indoor agricultural environments. To address these challenges, we introduce HSI-SC-NeRF, a stationary-camera multi-channel NeRF framework for high-throughput hyperspectral 3D reconstruction targeting postharvest inspection of agricultural produce. Multi-view hyperspectral data is captured using a stationary camera while the object rotates within a custom-built Teflon imaging chamber providing diffuse, uniform illumination. Object poses are estimated via ArUco calibration markers and transformed to the camera frame of reference through simulated pose transformations, enabling standard NeRF training on stationary-camera data. A multi-channel NeRF formulation optimizes reconstruction across all hyperspectral bands jointly using a composite spectral loss, supported by a two-stage training protocol that decouples geometric initialization from radiometric refinement. Experiments on three agricultural produce samples demonstrate high spatial reconstruction accuracy and strong spectral fidelity across the visible and near-infrared spectrum, confirming the suitability of HSI-SC-NeRF for integration into automated agricultural workflows.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.16950">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.16950.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.16950.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Subtractive Modulative Network with Learnable Periodic Activations</span>
        <span class="paper-authors">Tiou Wang, Zhuoqian Yang, Markus Flierl, Mathieu Salzmann, Sabine Süsstrunk</span>
        <span class="paper-meta">Updated 2026-02-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We propose the Subtractive Modulative Network (SMN), a novel, parameter-efficient Implicit Neural Representation (INR) architecture inspired by classical subtractive synthesis. The SMN is designed as a principled signal processing pipeline, featuring a learnable periodic activation layer (Oscillator) that generates a multi-frequency basis, and a series of modulative mask modules (Filters) that actively generate high-order harmonics. We provide both theoretical analysis and empirical validation for our design. Our SMN achieves a PSNR of $40+$ dB on two image datasets, comparing favorably against state-of-the-art methods in terms of both reconstruction accuracy and parameter efficiency. Furthermore, consistent advantage is observed on the challenging 3D NeRF novel view synthesis task. Supplementary materials are available at https://inrainbws.github.io/smn/.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.16337">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.16337.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.16337.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">High-fidelity 3D reconstruction for planetary exploration</span>
        <span class="paper-authors">Alfonso Martínez-Petersen, Levin Gerdes, David Rodríguez-Martínez, C. J. Pérez-del-Pulgar</span>
        <span class="paper-meta">Updated 2026-02-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Planetary exploration increasingly relies on autonomous robotic systems capable of perceiving, interpreting, and reconstructing their surroundings in the absence of global positioning or real-time communication with Earth. Rovers operating on planetary surfaces must navigate under sever environmental constraints, limited visual redundancy, and communication delays, making onboard spatial awareness and visual localization key components for mission success. Traditional techniques based on Structure-from-Motion (SfM) and Simultaneous Localization and Mapping (SLAM) provide geometric consistency but struggle to capture radiometric detail or to scale efficiently in unstructured, low-texture terrains typical of extraterrestrial environments. This work explores the integration of radiance field-based methods - specifically Neural Radiance Fields (NeRF) and Gaussian Splatting - into a unified, automated environment reconstruction pipeline for planetary robotics. Our system combines the Nerfstudio and COLMAP frameworks with a ROS2-compatible workflow capable of processing raw rover data directly from rosbag recordings. This approach enables the generation of dense, photorealistic, and metrically consistent 3D representations from minimal visual input, supporting improved perception and planning for autonomous systems operating in planetary-like conditions. The resulting pipeline established a foundation for future research in radiance field-based mapping, bridging the gap between geometric and neural representations in planetary exploration.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.13909">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.13909.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.13909.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Nighttime Autonomous Driving Scene Reconstruction with Physically-Based Gaussian Splatting</span>
        <span class="paper-authors">Tae-Kyeong Kim, Xingxin Chen, Guile Wu, Chengjie Huang, Dongfeng Bai, Bingbing Liu</span>
        <span class="paper-meta">Updated 2026-02-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">This paper focuses on scene reconstruction under nighttime conditions in autonomous driving simulation. Recent methods based on Neural Radiance Fields (NeRFs) and 3D Gaussian Splatting (3DGS) have achieved photorealistic modeling in autonomous driving scene reconstruction, but they primarily focus on normal-light conditions. Low-light driving scenes are more challenging to model due to their complex lighting and appearance conditions, which often causes performance degradation of existing methods. To address this problem, this work presents a novel approach that integrates physically based rendering into 3DGS to enhance nighttime scene reconstruction for autonomous driving. Specifically, our approach integrates physically based rendering into composite scene Gaussian representations and jointly optimizes Bidirectional Reflectance Distribution Function (BRDF) based material properties. We explicitly model diffuse components through a global illumination module and specular components by anisotropic spherical Gaussians. As a result, our approach improves reconstruction quality for outdoor nighttime driving scenes, while maintaining real-time rendering. Extensive experiments across diverse nighttime scenarios on two real-world autonomous driving datasets, including nuScenes and Waymo, demonstrate that our approach outperforms the state-of-the-art methods both quantitatively and qualitatively.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.13549">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.13549.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.13549.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">From Implicit Ambiguity to Explicit Solidity: Diagnosing Interior Geometric Degradation in Neural Radiance Fields for Dense 3D Scene Understanding</span>
        <span class="paper-authors">Jiangsan Zhao, Jakob Geipel, Kryzysztof Kusnierek</span>
        <span class="paper-meta">Updated 2026-02-12</span>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Deepfake Synthesis vs. Detection: An Uneven Contest</span>
        <span class="paper-authors">Md. Tarek Hasan, Sanjay Saha, Shaojing Fan, Swakkhar Shatabda, Terence Sim</span>
        <span class="paper-meta">Updated 2026-02-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">The rapid advancement of deepfake technology has significantly elevated the realism and accessibility of synthetic media. Emerging techniques, such as diffusion-based models and Neural Radiance Fields (NeRF), alongside enhancements in traditional Generative Adversarial Networks (GANs), have contributed to the sophisticated generation of deepfake videos. Concurrently, deepfake detection methods have seen notable progress, driven by innovations in Transformer architectures, contrastive learning, and other machine learning approaches. In this study, we conduct a comprehensive empirical analysis of state-of-the-art deepfake detection techniques, including human evaluation experiments against cutting-edge synthesis methods. Our findings highlight a concerning trend: many state-of-the-art detection models exhibit markedly poor performance when challenged with deepfakes produced by modern synthesis techniques, including poor performance by human participants against the best quality deepfakes. Through extensive experimentation, we provide evidence that underscores the urgent need for continued refinement of detection models to keep pace with the evolving capabilities of deepfake generation technologies. This research emphasizes the critical gap between current detection methodologies and the sophistication of new generation techniques, calling for intensified efforts in this crucial area of study.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.07986">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.07986.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.07986.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">NVS-HO: A Benchmark for Novel View Synthesis of Handheld Objects</span>
        <span class="paper-authors">Musawar Ali, Manuel Carranza-García, Nicola Fioraio, Samuele Salti, Luigi Di Stefano</span>
        <span class="paper-meta">Updated 2026-02-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We propose NVS-HO, the first benchmark designed for novel view synthesis of handheld objects in real-world environments using only RGB inputs. Each object is recorded in two complementary RGB sequences: (1) a handheld sequence, where the object is manipulated in front of a static camera, and (2) a board sequence, where the object is fixed on a ChArUco board to provide accurate camera poses via marker detection. The goal of NVS-HO is to learn a NVS model that captures the full appearance of an object from (1), whereas (2) provides the ground-truth images used for evaluation. To establish baselines, we consider both a classical SfM pipeline and a state-of-the-art pre-trained feed-forward neural network (VGGT) as pose estimators, and train NVS models based on NeRF and Gaussian Splatting. Our experiments reveal significant performance gaps in current methods under unconstrained handheld conditions, highlighting the need for more robust approaches. NVS-HO thus offers a challenging real-world benchmark to drive progress in RGB-based novel view synthesis of handheld objects.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.05822">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.05822.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.05822.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">NeVStereo: A NeRF-Driven NVS-Stereo Architecture for High-Fidelity 3D Tasks</span>
        <span class="paper-authors">Pengcheng Chen, Yue Hu, Wenhao Li, Nicole M Gunderson, Andrew Feng, Zhenglong Sun, Peter Beerel, Eric J Seibel</span>
        <span class="paper-meta">Updated 2026-02-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">In modern dense 3D reconstruction, feed-forward systems (e.g., VGGT, pi3) focus on end-to-end matching and geometry prediction but do not explicitly output the novel view synthesis (NVS). Neural rendering-based approaches offer high-fidelity NVS and detailed geometry from posed images, yet they typically assume fixed camera poses and can be sensitive to pose errors. As a result, it remains non-trivial to obtain a single framework that can offer accurate poses, reliable depth, high-quality rendering, and accurate 3D surfaces from casually captured views. We present NeVStereo, a NeRF-driven NVS-stereo architecture that aims to jointly deliver camera poses, multi-view depth, novel view synthesis, and surface reconstruction from multi-view RGB-only inputs. NeVStereo combines NeRF-based NVS for stereo-friendly renderings, confidence-guided multi-view depth estimation, NeRF-coupled bundle adjustment for pose refinement, and an iterative refinement stage that updates both depth and the radiance field to improve geometric consistency. This design mitigated the common NeRF-based issues such as surface stacking, artifacts, and pose-depth coupling. Across indoor, outdoor, tabletop, and aerial benchmarks, our experiments indicate that NeVStereo achieves consistently strong zero-shot performance, with up to 36% lower depth error, 10.4% improved pose accuracy, 4.5% higher NVS fidelity, and state-of-the-art mesh quality (F1 91.93%, Chamfer 4.35 mm) compared to existing prestigious methods.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.05423">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.05423.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.05423.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Beyond Cropping and Rotation: Automated Evolution of Powerful Task-Specific Augmentations with Generative Models</span>
        <span class="paper-authors">Judah Goldfeder, Shreyes Kaliyur, Vaibhav Sourirajan, Patrick Minwan Puma, Philippe Martin Wyder, Yuhang Hu, Jiong Lin, Hod Lipson</span>
        <span class="paper-meta">Updated 2026-02-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Data augmentation has long been a cornerstone for reducing overfitting in vision models, with methods like AutoAugment automating the design of task-specific augmentations. Recent advances in generative models, such as conditional diffusion and few-shot NeRFs, offer a new paradigm for data augmentation by synthesizing data with significantly greater diversity and realism. However, unlike traditional augmentations like cropping or rotation, these methods introduce substantial changes that enhance robustness but also risk degrading performance if the augmentations are poorly matched to the task. In this work, we present EvoAug, an automated augmentation learning pipeline, which leverages these generative models alongside an efficient evolutionary algorithm to learn optimal task-specific augmentations. Our pipeline introduces a novel approach to image augmentation that learns stochastic augmentation trees that hierarchically compose augmentations, enabling more structured and adaptive transformations. We demonstrate strong performance across fine-grained classification and few-shot learning tasks. Notably, our pipeline discovers augmentations that align with domain knowledge, even in low-data settings. These results highlight the potential of learned generative augmentations, unlocking new possibilities for robust model training.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2602.03123">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2602.03123.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2602.03123.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Under-Canopy Terrain Reconstruction in Dense Forests Using RGB Imaging and Neural 3D Reconstruction</span>
        <span class="paper-authors">Refael Sheffer, Chen Pinchover, Haim Zisman, Dror Ozeri, Roee Litman</span>
        <span class="paper-meta">Updated 2026-02-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Mapping the terrain and understory hidden beneath dense forest canopies is of great interest for numerous applications such as search and rescue, trail mapping, forest inventory tasks, and more. Existing solutions rely on specialized sensors: either heavy, costly airborne LiDAR, or Airborne Optical Sectioning (AOS), which uses thermal synthetic aperture photography and is tailored for person detection.   We introduce a novel approach for the reconstruction of canopy-free, photorealistic ground views using only conventional RGB images. Our solution is based on the celebrated Neural Radiance Fields (NeRF), a recent 3D reconstruction method. Additionally, we include specific image capture considerations, which dictate the needed illumination to successfully expose the scene beneath the canopy. To better cope with the poorly lit understory, we employ a low light loss. Finally, we propose two complementary approaches to remove occluding canopy elements by controlling per-ray integration procedure.   To validate the value of our approach, we present two possible downstream tasks. For the task of search and rescue (SAR), we demonstrate that our method enables person detection which achieves promising results compared to thermal AOS (using only RGB images). Additionally, we show the potential of our approach for forest inventory tasks like tree counting. These results position our approach as a cost-effective, high-resolution alternative to specialized sensors for SAR, trail mapping, and forest-inventory tasks.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.22861">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.22861.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.22861.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">EAG-PT: Emission-Aware Gaussians and Path Tracing for Indoor Scene Reconstruction and Editing</span>
        <span class="paper-authors">Xijie Yang, Mulin Yu, Changjian Jiang, Kerui Ren, Tao Lu, Jiangmiao Pang, Dahua Lin, Bo Dai, Linning Xu</span>
        <span class="paper-meta">Updated 2026-01-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Recent reconstruction methods based on radiance field such as NeRF and 3DGS reproduce indoor scenes with high visual fidelity, but break down under scene editing due to baked illumination and the lack of explicit light transport. In contrast, physically based inverse rendering relies on mesh representations and path tracing, which enforce correct light transport but place strong requirements on geometric fidelity, becoming a practical bottleneck for real indoor scenes. In this work, we propose Emission-Aware Gaussians and Path Tracing (EAG-PT), aiming for physically based light transport with a unified 2D Gaussian representation. Our design is based on three cores: (1) using 2D Gaussians as a unified scene representation and transport-friendly geometry proxy that avoids reconstructed mesh, (2) explicitly separating emissive and non-emissive components during reconstruction for further scene editing, and (3) decoupling reconstruction from final rendering by using efficient single-bounce optimization and high-quality multi-bounce path tracing after scene editing. Experiments on synthetic and real indoor scenes show that EAG-PT produces more natural and physically consistent renders after editing than radiant scene reconstructions, while preserving finer geometric detail and avoiding mesh-induced artifacts compared to mesh-based inverse path tracing. These results suggest promising directions for future use in interior design, XR content creation, and embodied AI.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.23065">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.23065.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.23065.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Diachronic Stereo Matching for Multi-Date Satellite Imagery</span>
        <span class="paper-authors">Elías Masquil, Luca Savant Aira, Roger Marí, Thibaud Ehret, Pablo Musé, Gabriele Facciolo</span>
        <span class="paper-meta">Updated 2026-01-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Recent advances in image-based satellite 3D reconstruction have progressed along two complementary directions. On one hand, multi-date approaches using NeRF or Gaussian-splatting jointly model appearance and geometry across many acquisitions, achieving accurate reconstructions on opportunistic imagery with numerous observations. On the other hand, classical stereoscopic reconstruction pipelines deliver robust and scalable results for simultaneous or quasi-simultaneous image pairs. However, when the two images are captured months apart, strong seasonal, illumination, and shadow changes violate standard stereoscopic assumptions, causing existing pipelines to fail. This work presents the first Diachronic Stereo Matching method for satellite imagery, enabling reliable 3D reconstruction from temporally distant pairs. Two advances make this possible: (1) fine-tuning a state-of-the-art deep stereo network that leverages monocular depth priors, and (2) exposing it to a dataset specifically curated to include a diverse set of diachronic image pairs. In particular, we start from a pretrained MonSter model, trained initially on a mix of synthetic and real datasets such as SceneFlow and KITTI, and fine-tune it on a set of stereo pairs derived from the DFC2019 remote sensing challenge. This dataset contains both synchronic and diachronic pairs under diverse seasonal and illumination conditions. Experiments on multi-date WorldView-3 imagery demonstrate that our approach consistently surpasses classical pipelines and unadapted deep stereo models on both synchronic and diachronic settings. Fine-tuning on temporally diverse images, together with monocular priors, proves essential for enabling 3D reconstruction from previously incompatible acquisition dates. Left image (winter) Right image (autumn) DSM geometry Ours (1.23 m) Zero-shot (3.99 m) LiDAR GT Figure 1. Output geometry for a winter-autumn image pair from Omaha (OMA 331 test scene). Our method recovers accurate geometry despite the diachronic nature of the pair, exhibiting strong appearance changes, which cause existing zero-shot methods to fail. Missing values due to perspective shown in black.  Mean altitude error in parentheses; lower is better.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.22808">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.22808.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.22808.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Lightweight High-Fidelity Low-Bitrate Talking Face Compression for 3D Video Conference</span>
        <span class="paper-authors">Jianglong Li, Jun Xu, Bingcong Lu, Zhengxue Cheng, Hongwei Hu, Ronghua Wu, Li Song</span>
        <span class="paper-meta">Updated 2026-01-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">The demand for immersive and interactive communication has driven advancements in 3D video conferencing, yet achieving high-fidelity 3D talking face representation at low bitrates remains a challenge. Traditional 2D video compression techniques fail to preserve fine-grained geometric and appearance details, while implicit neural rendering methods like NeRF suffer from prohibitive computational costs. To address these challenges, we propose a lightweight, high-fidelity, low-bitrate 3D talking face compression framework that integrates FLAME-based parametric modeling with 3DGS neural rendering. Our approach transmits only essential facial metadata in real time, enabling efficient reconstruction with a Gaussian-based head model. Additionally, we introduce a compact representation and compression scheme, including Gaussian attribute compression and MLP optimization, to enhance transmission efficiency. Experimental results demonstrate that our method achieves superior rate-distortion performance, delivering high-quality facial rendering at extremely low bitrates, making it well-suited for real-time 3D video conferencing applications.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.21269">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.21269.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.21269.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Bridging Visual and Wireless Sensing: A Unified Radiation Field for 3D Radio Map Construction</span>
        <span class="paper-authors">Chaozheng Wen, Jingwen Tong, Zehong Lin, Chenghong Bian, Jun Zhang</span>
        <span class="paper-meta">Updated 2026-01-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">The emerging applications of next-generation wireless networks (e.g., immersive 3D communication, low-altitude networks, and integrated sensing and communication) necessitate high-fidelity environmental intelligence. 3D radio maps have emerged as a critical tool for this purpose, enabling spectrum-aware planning and environment-aware sensing by bridging the gap between physical environments and electromagnetic signal propagation. However, constructing accurate 3D radio maps requires fine-grained 3D geometric information and a profound understanding of electromagnetic wave propagation. Existing approaches typically treat optical and wireless knowledge as distinct modalities, failing to exploit the fundamental physical principles governing both light and electromagnetic propagation. To bridge this gap, we propose URF-GS, a unified radio-optical radiation field representation framework for accurate and generalizable 3D radio map construction based on 3D Gaussian splatting (3D-GS) and inverse rendering. By fusing visual and wireless sensing observations, URF-GS recovers scene geometry and material properties while accurately predicting radio signal behavior at arbitrary transmitter-receiver (Tx-Rx) configurations. Experimental results demonstrate that URF-GS achieves up to a 24.7% improvement in spatial spectrum prediction accuracy and a 10x increase in sample efficiency for 3D radio map construction compared with neural radiance field (NeRF)-based methods. This work establishes a foundation for next-generation wireless networks by integrating perception, interaction, and communication through holistic radiation field reconstruction.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.19216">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.19216.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.19216.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Audio-Driven Talking Face Generation with Blink Embedding and Hash Grid Landmarks Encoding</span>
        <span class="paper-authors">Yuhui Zhang, Hui Yu, Wei Liang, Sunjie Zhang</span>
        <span class="paper-meta">Updated 2026-01-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Dynamic Neural Radiance Fields (NeRF) have demonstrated considerable success in generating high-fidelity 3D models of talking portraits. Despite significant advancements in the rendering speed and generation quality, challenges persist in accurately and efficiently capturing mouth movements in talking portraits. To tackle this challenge, we propose an automatic method based on blink embedding and hash grid landmarks encoding in this study, which can substantially enhance the fidelity of talking faces. Specifically, we leverage facial features encoded as conditional features and integrate audio features as residual terms into our model through a Dynamic Landmark Transformer. Furthermore, we employ neural radiance fields to model the entire face, resulting in a lifelike face representation. Experimental evaluations have validated the superiority of our approach to existing methods.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.18849">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.18849.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.18849.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MV-SAM: Multi-view Promptable Segmentation using Pointmap Guidance</span>
        <span class="paper-authors">Yoonwoo Jeong, Cheng Sun, Yu-Chiang Frank Wang, Minsu Cho, Jaesung Choe</span>
        <span class="paper-meta">Updated 2026-01-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Promptable segmentation has emerged as a powerful paradigm in computer vision, enabling users to guide models in parsing complex scenes with prompts such as clicks, boxes, or textual cues. Recent advances, exemplified by the Segment Anything Model (SAM), have extended this paradigm to videos and multi-view images. However, the lack of 3D awareness often leads to inconsistent results, necessitating costly per-scene optimization to enforce 3D consistency. In this work, we introduce MV-SAM, a framework for multi-view segmentation that achieves 3D consistency using pointmaps -- 3D points reconstructed from unposed images by recent visual geometry models. Leveraging the pixel-point one-to-one correspondence of pointmaps, MV-SAM lifts images and prompts into 3D space, eliminating the need for explicit 3D networks or annotated 3D data. Specifically, MV-SAM extends SAM by lifting image embeddings from its pretrained encoder into 3D point embeddings, which are decoded by a transformer using cross-attention with 3D prompt embeddings. This design aligns 2D interactions with 3D geometry, enabling the model to implicitly learn consistent masks across views through 3D positional embeddings. Trained on the SA-1B dataset, our method generalizes well across domains, outperforming SAM2-Video and achieving comparable performance with per-scene optimization baselines on NVOS, SPIn-NeRF, ScanNet++, uCo3D, and DL3DV benchmarks. Code will be released.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.17866">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.17866.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.17866.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">NeRF-MIR: Towards High-Quality Restoration of Masked Images with Neural Radiance Fields</span>
        <span class="paper-authors">Xianliang Huang, Zhizhou Zhong, Shuhang Chen, Yi Xu, Juhong Guan, Shuigeng Zhou</span>
        <span class="paper-meta">Updated 2026-01-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Neural Radiance Fields (NeRF) have demonstrated remarkable performance in novel view synthesis. However, there is much improvement room on restoring 3D scenes based on NeRF from corrupted images, which are common in natural scene captures and can significantly impact the effectiveness of NeRF. This paper introduces NeRF-MIR, a novel neural rendering approach specifically proposed for the restoration of masked images, demonstrating the potential of NeRF in this domain. Recognizing that randomly emitting rays to pixels in NeRF may not effectively learn intricate image textures, we propose a \textbf{P}atch-based \textbf{E}ntropy for \textbf{R}ay \textbf{E}mitting (\textbf{PERE}) strategy to distribute emitted rays properly. This enables NeRF-MIR to fuse comprehensive information from images of different views. Additionally, we introduce a \textbf{P}rogressively \textbf{I}terative \textbf{RE}storation (\textbf{PIRE}) mechanism to restore the masked regions in a self-training process. Furthermore, we design a dynamically-weighted loss function that automatically recalibrates the loss weights for masked regions. As existing datasets do not support NeRF-based masked image restoration, we construct three masked datasets to simulate corrupted scenarios. Extensive experiments on real data and constructed datasets demonstrate the superiority of NeRF-MIR over its counterparts in masked image restoration.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.17350">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.17350.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.17350.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Multi-View Consistent Wound Segmentation With Neural Fields</span>
        <span class="paper-authors">Remi Chierchia, Léo Lebrat, David Ahmedt-Aristizabal, Yulia Arzhaeva, Olivier Salvado, Clinton Fookes, Rodrigo Santa Cruz</span>
        <span class="paper-meta">Updated 2026-01-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Wound care is often challenged by the economic and logistical burdens that consistently afflict patients and hospitals worldwide. In recent decades, healthcare professionals have sought support from computer vision and machine learning algorithms. In particular, wound segmentation has gained interest due to its ability to provide professionals with fast, automatic tissue assessment from standard RGB images. Some approaches have extended segmentation to 3D, enabling more complete and precise healing progress tracking. However, inferring multi-view consistent 3D structures from 2D images remains a challenge. In this paper, we evaluate WoundNeRF, a NeRF SDF-based method for estimating robust wound segmentations from automatically generated annotations. We demonstrate the potential of this paradigm in recovering accurate segmentations by comparing it against state-of-the-art Vision Transformer networks and conventional rasterisation-based algorithms. The code will be released to facilitate further development in this promising paradigm.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.16487">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.16487.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.16487.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Seeing through Light and Darkness: Sensor-Physics Grounded Deblurring HDR NeRF from Single-Exposure Images and Events</span>
        <span class="paper-authors">Yunshan Qi, Lin Zhu, Nan Bao, Yifan Zhao, Jia Li</span>
        <span class="paper-meta">Updated 2026-01-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Novel view synthesis from low dynamic range (LDR) blurry images, which are common in the wild, struggles to recover high dynamic range (HDR) and sharp 3D representations in extreme lighting conditions. Although existing methods employ event data to address this issue, they ignore the sensor-physics mismatches between the camera output and physical world radiance, resulting in suboptimal HDR and deblurring results. To cope with this problem, we propose a unified sensor-physics grounded NeRF framework for sharp HDR novel view synthesis from single-exposure blurry LDR images and corresponding events. We employ NeRF to directly represent the actual radiance of the 3D scene in the HDR domain and model raw HDR scene rays hitting the sensor pixels as in the physical world. A pixel-wise RGB mapping field is introduced to align the above rendered pixel values with the sensor-recorded LDR pixel values of the input images. A novel event mapping field is also designed to bridge the physical scene dynamics and actual event sensor output. The two mapping fields are jointly optimized with the NeRF network, leveraging the spatial and temporal dynamic information in events to enhance the sharp HDR 3D representation learning. Experiments on the collected and public datasets demonstrate that our method can achieve state-of-the-art deblurring HDR novel view synthesis results with single-exposure blurry LDR images and corresponding events.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.15475">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.15475.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.15475.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GAT-NeRF: Geometry-Aware-Transformer Enhanced Neural Radiance Fields for High-Fidelity 4D Facial Avatars</span>
        <span class="paper-authors">Zhe Chang, Haodong Jin, Ying Sun, Yan Song, Hui Yu</span>
        <span class="paper-meta">Updated 2026-01-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">High-fidelity 4D dynamic facial avatar reconstruction from monocular video is a critical yet challenging task, driven by increasing demands for immersive virtual human applications. While Neural Radiance Fields (NeRF) have advanced scene representation, their capacity to capture high-frequency facial details, such as dynamic wrinkles and subtle textures from information-constrained monocular streams, requires significant enhancement. To tackle this challenge, we propose a novel hybrid neural radiance field framework, called Geometry-Aware-Transformer Enhanced NeRF (GAT-NeRF) for high-fidelity and controllable 4D facial avatar reconstruction, which integrates the Transformer mechanism into the NeRF pipeline. GAT-NeRF synergistically combines a coordinate-aligned Multilayer Perceptron (MLP) with a lightweight Transformer module, termed as Geometry-Aware-Transformer (GAT) due to its processing of multi-modal inputs containing explicit geometric priors. The GAT module is enabled by fusing multi-modal input features, including 3D spatial coordinates, 3D Morphable Model (3DMM) expression parameters, and learnable latent codes to effectively learn and enhance feature representations pertinent to fine-grained geometry. The Transformer&#x27;s effective feature learning capabilities are leveraged to significantly augment the modeling of complex local facial patterns like dynamic wrinkles and acne scars. Comprehensive experiments unequivocally demonstrate GAT-NeRF&#x27;s state-of-the-art performance in visual fidelity and high-frequency detail recovery, forging new pathways for creating realistic dynamic digital humans for multimedia applications.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.14875">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.14875.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.14875.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">POTR: Post-Training 3DGS Compression</span>
        <span class="paper-authors">Bert Ramlot, Martijn Courteaux, Peter Lambert, Glenn Van Wallendael</span>
        <span class="paper-meta">Updated 2026-01-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">3D Gaussian Splatting (3DGS) has recently emerged as a promising contender to Neural Radiance Fields (NeRF) in 3D scene reconstruction and real-time novel view synthesis. 3DGS outperforms NeRF in training and inference speed but has substantially higher storage requirements. To remedy this downside, we propose POTR, a post-training 3DGS codec built on two novel techniques. First, POTR introduces a novel pruning approach that uses a modified 3DGS rasterizer to efficiently calculate every splat&#x27;s individual removal effect simultaneously. This technique results in 2-4x fewer splats than other post-training pruning techniques and as a result also significantly accelerates inference with experiments demonstrating 1.5-2x faster inference than other compressed models. Second, we propose a novel method to recompute lighting coefficients, significantly reducing their entropy without using any form of training. Our fast and highly parallel approach especially increases AC lighting coefficient sparsity, with experiments demonstrating increases from 70% to 97%, with minimal loss in quality. Finally, we extend POTR with a simple fine-tuning scheme to further enhance pruning, inference, and rate-distortion performance. Experiments demonstrate that POTR, even without fine-tuning, consistently outperforms all other post-training compression techniques in both rate-distortion performance and inference speed.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.14821">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.14821.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.14821.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">TreeDGS: Aerial Gaussian Splatting for Distant DBH Measurement</span>
        <span class="paper-authors">Belal Shaheen, Minh-Hieu Nguyen, Bach-Thuan Bui, Shubham, Tim Wu, Michael Fairley, Matthew David Zane, Michael Wu, James Tompkin</span>
        <span class="paper-meta">Updated 2026-01-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Aerial remote sensing enables efficient large-area surveying, but accurate direct object-level measurement remains difficult in complex natural scenes. Recent advancements in 3D vision, particularly learned radiance-field representations such as NeRF and 3D Gaussian Splatting, have begun to raise the ceiling on reconstruction fidelity and densifiable geometry from posed imagery. Nevertheless, direct aerial measurement of important natural attributes such as tree diameter at breast height (DBH) remains challenging. Trunks in aerial forest scans are distant and sparsely observed in image views: at typical operating altitudes, stems may span only a few pixels. With these constraints, conventional reconstruction methods leave breast-height trunk geometry weakly constrained. We present TreeDGS, an aerial image reconstruction method that leverages 3D Gaussian Splatting as a continuous, densifiable scene representation for trunk measurement. After SfM-MVS initialization and Gaussian optimization, we extract a dense point set from the Gaussian field using RaDe-GS&#x27;s depth-aware cumulative-opacity integration and associate each sample with a multi-view opacity reliability score. We then estimate DBH from trunk-isolated points using opacity-weighted solid-circle fitting. Evaluated on 10 plots with field-measured DBH, TreeDGS reaches 4.79,cm RMSE (about 2.6 pixels at this GSD) and outperforms a state-of-the-art LiDAR baseline (7.91,cm RMSE), demonstrating that densified splat-based geometry can enable accurate, low-cost aerial DBH measurement.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.12823">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.12823.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.12823.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Bayesian Monocular Depth Refinement via Neural Radiance Fields</span>
        <span class="paper-authors">Arun Muthukkumar</span>
        <span class="paper-meta">Updated 2026-01-15</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Monocular depth estimation has applications in many fields, such as autonomous navigation and extended reality, making it an essential computer vision task. However, current methods often produce smooth depth maps that lack the fine geometric detail needed for accurate scene understanding. We propose MDENeRF, an iterative framework that refines monocular depth estimates using depth information from Neural Radiance Fields (NeRFs). MDENeRF consists of three components: (1) an initial monocular estimate for global structure, (2) a NeRF trained on perturbed viewpoints, with per-pixel uncertainty, and (3) Bayesian fusion of the noisy monocular and NeRF depths. We derive NeRF uncertainty from the volume rendering process to iteratively inject high-frequency fine details. Meanwhile, our monocular prior maintains global structure. We demonstrate improvements on key metrics and experiments using indoor scenes from the SUN RGB-D dataset.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.03869">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.03869.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.03869.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Radiant Foam Rendering on a Graph Processor</span>
        <span class="paper-authors">Zulkhuu Tuya, Ignacio Alzugaray, Nicholas Fry, Andrew J. Davison</span>
        <span class="paper-meta">Updated 2026-01-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Many emerging many-core accelerators replace a single large device memory with hundreds to thousands of lightweight cores, each owning only a small local SRAM and exchanging data via explicit on-chip communication. This organization offers high aggregate bandwidth, but it breaks a key assumption behind many volumetric rendering techniques: that rays can randomly access a large, unified scene representation. Rendering efficiently on such hardware therefore requires distributing both data and computation, keeping ray traversal mostly local, and structuring communication into predictable routes.   We present a fully in-SRAM, distributed renderer for the Radiant Foam Voronoi-cell volumetric representation on the Graphcore Mk2 IPU(Intelligence Processing Unit), a many-core accelerator with tile-local SRAM and explicit inter-tile communication. Our system shards the scene across tiles and forwards rays between shards through a hierarchical routing overlay, enabling ray marching entirely from on-chip SRAM with predictable communication. On Mip-NeRF~360 scenes, the system attains near-interactive throughput of approximately 1 fps at 640x480 with image and depth map quality close to the original GPU-based Radiant Foam implementation, while keeping all scene data and ray state in on-chip SRAM. Beyond demonstrating feasibility, we analyze routing, memory, and scheduling bottlenecks that inform how future distributed-memory accelerators can better support irregular, data-movement-heavy rendering workloads.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.04382">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.04382.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.04382.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">HOSC: A Periodic Activation with Saturation Control for High-Fidelity Implicit Neural Representations</span>
        <span class="paper-authors">Michal Jan Wlodarczyk, Danzel Serrano, Przemyslaw Musialski</span>
        <span class="paper-meta">Updated 2026-01-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Periodic activations such as sine preserve high-frequency information in implicit neural representations (INRs) through their oscillatory structure, but often suffer from gradient instability and limited control over multi-scale behavior. We introduce the Hyperbolic Oscillator with Saturation Control (HOSC) activation, $\text{HOSC}(x) = \tanh\bigl(β\sin(ω_0 x)\bigr)$, which exposes an explicit parameter $β$ that controls the Lipschitz bound of the activation by $βω_0$. This provides a direct mechanism to tune gradient magnitudes while retaining a periodic carrier. We provide a mathematical analysis and conduct a comprehensive empirical study across images, audio, video, NeRFs, and SDFs using standardized training protocols. Comparative analysis against SIREN, FINER, and related methods shows where HOSC provides substantial benefits and where it achieves competitive parity. Results establish HOSC as a practical periodic activation for INR applications, with domain-specific guidance on hyperparameter selection. For code visit the project page https://hosc-nn.github.io/ .</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.07870">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.07870.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.07870.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">QNeRF: Neural Radiance Fields on a Simulated Gate-Based Quantum Computer</span>
        <span class="paper-authors">Daniele Lizzio Bosco, Shuteng Wang, Giuseppe Serra, Vladislav Golyanik</span>
        <span class="paper-meta">Updated 2026-01-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Recently, Quantum Visual Fields (QVFs) have shown promising improvements in model compactness and convergence speed for learning the provided 2D or 3D signals. Meanwhile, novel-view synthesis has seen major advances with Neural Radiance Fields (NeRFs), where models learn a compact representation from 2D images to render 3D scenes, albeit at the cost of larger models and intensive training. In this work, we extend the approach of QVFs by introducing QNeRF, the first hybrid quantum-classical model designed for novel-view synthesis from 2D images. QNeRF leverages parameterised quantum circuits to encode spatial and view-dependent information via quantum superposition and entanglement, resulting in more compact models compared to the classical counterpart. We present two architectural variants. Full QNeRF maximally exploits all quantum amplitudes to enhance representational capabilities. In contrast, Dual-Branch QNeRF introduces a task-informed inductive bias by branching spatial and view-dependent quantum state preparations, drastically reducing the complexity of this operation and ensuring scalability and potential hardware compatibility. Our experiments demonstrate that -- when trained on images of moderate resolution -- QNeRF matches or outperforms classical NeRF baselines while using less than half the number of parameters. These results suggest that quantum machine learning can serve as a competitive alternative for continuous signal representation in mid-level tasks in computer vision, such as 3D representation learning from 2D observations.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.05250">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.05250.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.05250.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DivAS: Interactive 3D Segmentation of NeRFs via Depth-Weighted Voxel Aggregation</span>
        <span class="paper-authors">Ayush Pande</span>
        <span class="paper-meta">Updated 2026-01-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Existing methods for segmenting Neural Radiance Fields (NeRFs) are often optimization-based, requiring slow per-scene training that sacrifices the zero-shot capabilities of 2D foundation models. We introduce DivAS (Depth-interactive Voxel Aggregation Segmentation), an optimization-free, fully interactive framework that addresses these limitations. Our method operates via a fast GUI-based workflow where 2D SAM masks, generated from user point prompts, are refined using NeRF-derived depth priors to improve geometric accuracy and foreground-background separation. The core of our contribution is a custom CUDA kernel that aggregates these refined multi-view masks into a unified 3D voxel grid in under 200ms, enabling real-time visual feedback. This optimization-free design eliminates the need for per-scene training. Experiments on Mip-NeRF 360° and LLFF show that DivAS achieves segmentation quality comparable to optimization-based methods, while being 2-2.5x faster end-to-end, and up to an order of magnitude faster when excluding user prompting time.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.04860">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.04860.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.04860.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">CropNeRF: A Neural Radiance Field-Based Framework for Crop Counting</span>
        <span class="paper-authors">Md Ahmed Al Muzaddid, William J. Beksi</span>
        <span class="paper-meta">Updated 2026-01-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Rigorous crop counting is crucial for effective agricultural management and informed intervention strategies. However, in outdoor field environments, partial occlusions combined with inherent ambiguity in distinguishing clustered crops from individual viewpoints poses an immense challenge for image-based segmentation methods. To address these problems, we introduce a novel crop counting framework designed for exact enumeration via 3D instance segmentation. Our approach utilizes 2D images captured from multiple viewpoints and associates independent instance masks for neural radiance field (NeRF) view synthesis. We introduce crop visibility and mask consistency scores, which are incorporated alongside 3D information from a NeRF model. This results in an effective segmentation of crop instances in 3D and highly-accurate crop counts. Furthermore, our method eliminates the dependence on crop-specific parameter tuning. We validate our framework on three agricultural datasets consisting of cotton bolls, apples, and pears, and demonstrate consistent counting performance despite major variations in crop color, shape, and size. A comparative analysis against the state of the art highlights superior performance on crop counting tasks. Lastly, we contribute a cotton plant dataset to advance further research on this topic.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.00207">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.00207.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.00207.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">UniC-Lift: Unified 3D Instance Segmentation via Contrastive Learning</span>
        <span class="paper-authors">Ankit Dhiman, Srinath R, Jaswanth Reddy, Lokesh R Boregowda, Venkatesh Babu Radhakrishnan</span>
        <span class="paper-meta">Updated 2025-12-31</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">3D Gaussian Splatting (3DGS) and Neural Radiance Fields (NeRF) have advanced novel-view synthesis. Recent methods extend multi-view 2D segmentation to 3D, enabling instance/semantic segmentation for better scene understanding. A key challenge is the inconsistency of 2D instance labels across views, leading to poor 3D predictions. Existing methods use a two-stage approach in which some rely on contrastive learning with hyperparameter-sensitive clustering, while others preprocess labels for consistency. We propose a unified framework that merges these steps, reducing training time and improving performance by introducing a learnable feature embedding for segmentation in Gaussian primitives. This embedding is then efficiently decoded into instance labels through a novel &quot;Embedding-to-Label&quot; process, effectively integrating the optimization. While this unified framework offers substantial benefits, we observed artifacts at the object boundaries. To address the object boundary issues, we propose hard-mining samples along these boundaries. However, directly applying hard mining to the feature embeddings proved unstable. Therefore, we apply a linear layer to the rasterized feature embeddings before calculating the triplet loss, which stabilizes training and significantly improves performance. Our method outperforms baselines qualitatively and quantitatively on the ScanNet, Replica3D, and Messy-Rooms datasets.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.24763">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.24763.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.24763.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ShinyNeRF: Digitizing Anisotropic Appearance in Neural Radiance Fields</span>
        <span class="paper-authors">Albert Barreiro, Roger Marí, Rafael Redondo, Gloria Haro, Carles Bosch</span>
        <span class="paper-meta">Updated 2025-12-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Recent advances in digitization technologies have transformed the preservation and dissemination of cultural heritage. In this vein, Neural Radiance Fields (NeRF) have emerged as a leading technology for 3D digitization, delivering representations with exceptional realism. However, existing methods struggle to accurately model anisotropic specular surfaces, typically observed, for example, on brushed metals. In this work, we introduce ShinyNeRF, a novel framework capable of handling both isotropic and anisotropic reflections. Our method is capable of jointly estimating surface normals, tangents, specular concentration, and anisotropy magnitudes of an Anisotropic Spherical Gaussian (ASG) distribution, by learning an approximation of the outgoing radiance as an encoded mixture of isotropic von Mises-Fisher (vMF) distributions. Experimental results show that ShinyNeRF not only achieves state-of-the-art performance on digitizing anisotropic specular reflections, but also offers plausible physical interpretations and editing of material properties compared to existing methods.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.21692">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.21692.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.21692.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Dreamcrafter: Immersive Editing of 3D Radiance Fields Through Flexible, Generative Inputs and Outputs</span>
        <span class="paper-authors">Cyrus Vachha, Yixiao Kang, Zach Dive, Ashwat Chidambaram, Anik Gupta, Eunice Jun, Bjoern Hartmann</span>
        <span class="paper-meta">Updated 2025-12-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Authoring 3D scenes is a central task for spatial computing applications. Competing visions for lowering existing barriers are (1) focus on immersive, direct manipulation of 3D content or (2) leverage AI techniques that capture real scenes (3D Radiance Fields such as, NeRFs, 3D Gaussian Splatting) and modify them at a higher level of abstraction, at the cost of high latency. We unify the complementary strengths of these approaches and investigate how to integrate generative AI advances into real-time, immersive 3D Radiance Field editing. We introduce Dreamcrafter, a VR-based 3D scene editing system that: (1) provides a modular architecture to integrate generative AI algorithms; (2) combines different levels of control for creating objects, including natural language and direct manipulation; and (3) introduces proxy representations that support interaction during high-latency operations. We contribute empirical findings on control preferences and discuss how generative AI interfaces beyond text input enhance creativity in scene editing and world building.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.20129">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.20129.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.20129.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Neural Brain Fields: A NeRF-Inspired Approach for Generating Nonexistent EEG Electrodes</span>
        <span class="paper-authors">Shahar Ain Kedem, Itamar Zimerman, Eliya Nachmani</span>
        <span class="paper-meta">Updated 2025-12-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Electroencephalography (EEG) data present unique modeling challenges because recordings vary in length, exhibit very low signal to noise ratios, differ significantly across participants, drift over time within sessions, and are rarely available in large and clean datasets. Consequently, developing deep learning methods that can effectively process EEG signals remains an open and important research problem. To tackle this problem, this work presents a new method inspired by Neural Radiance Fields (NeRF). In computer vision, NeRF techniques train a neural network to memorize the appearance of a 3D scene and then uses its learned parameters to render and edit the scene from any viewpoint. We draw an analogy between the discrete images captured from different viewpoints used to learn a continuous 3D scene in NeRF, and EEG electrodes positioned at different locations on the scalp, which are used to infer the underlying representation of continuous neural activity. Building on this connection, we show that a neural network can be trained on a single EEG sample in a NeRF style manner to produce a fixed size and informative weight vector that encodes the entire signal. Moreover, via this representation we can render the EEG signal at previously unseen time steps and spatial electrode positions. We demonstrate that this approach enables continuous visualization of brain activity at any desired resolution, including ultra high resolution, and reconstruction of raw EEG signals. Finally, our empirical analysis shows that this method can effectively simulate nonexistent electrodes data in EEG recordings, allowing the reconstructed signal to be fed into standard EEG processing networks to improve performance.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2601.00012">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2601.00012.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2601.00012.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Joint Learning of Depth, Pose, and Local Radiance Field for Large Scale Monocular 3D Reconstruction</span>
        <span class="paper-authors">Shahram Najam Syed, Yitian Hu, Yuchao Yao</span>
        <span class="paper-meta">Updated 2025-12-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Photorealistic 3-D reconstruction from monocular video collapses in large-scale scenes when depth, pose, and radiance are solved in isolation: scale-ambiguous depth yields ghost geometry, long-horizon pose drift corrupts alignment, and a single global NeRF cannot model hundreds of metres of content. We introduce a joint learning framework that couples all three factors and demonstrably overcomes each failure case. Our system begins with a Vision-Transformer (ViT) depth network trained with metric-scale supervision, giving globally consistent depths despite wide field-of-view variations. A multi-scale feature bundle-adjustment (BA) layer refines camera poses directly in feature space--leveraging learned pyramidal descriptors instead of brittle keypoints--to suppress drift on unconstrained trajectories. For scene representation, we deploy an incremental local-radiance-field hierarchy: new hash-grid NeRFs are allocated and frozen on-the-fly when view overlap falls below a threshold, enabling city-block-scale coverage on a single GPU. Evaluated on the Tanks and Temples benchmark, our method reduces Absolute Trajectory Error to 0.001-0.021 m across eight indoor-outdoor sequences--up to 18x lower than BARF and 2x lower than NoPe-NeRF--while maintaining sub-pixel Relative Pose Error. These results demonstrate that metric-scale, drift-free 3-D reconstruction and high-fidelity novel-view synthesis are achievable from a single uncalibrated RGB camera.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.18237">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.18237.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.18237.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SDFoam: Signed-Distance Foam for explicit surface reconstruction</span>
        <span class="paper-authors">Antonella Rech, Nicola Conci, Nicola Garau</span>
        <span class="paper-meta">Updated 2025-12-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Neural radiance fields (NeRF) have driven impressive progress in view synthesis by using ray-traced volumetric rendering. Splatting-based methods such as 3D Gaussian Splatting (3DGS) provide faster rendering by rasterizing 3D primitives. RadiantFoam (RF) brought ray tracing back, achieving throughput comparable to Gaussian Splatting by organizing radiance with an explicit Voronoi Diagram (VD). Yet, all the mentioned methods still struggle with precise mesh reconstruction. We address this gap by jointly learning an explicit VD with an implicit Signed Distance Field (SDF). The scene is optimized via ray tracing and regularized by an Eikonal objective. The SDF introduces metric-consistent isosurfaces, which, in turn, bias near-surface Voronoi cell faces to align with the zero level set. The resulting model produces crisper, view-consistent surfaces with fewer floaters and improved topology, while preserving photometric quality and maintaining training speed on par with RadiantFoam. Across diverse scenes, our hybrid implicit-explicit formulation, which we name SDFoam, substantially improves mesh reconstruction accuracy (Chamfer distance) with comparable appearance (PSNR, SSIM), without sacrificing efficiency.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.16706">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.16706.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.16706.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Using Gaussian Splats to Create High-Fidelity Facial Geometry and Texture</span>
        <span class="paper-authors">Haodi He, Jihun Yu, Ronald Fedkiw</span>
        <span class="paper-meta">Updated 2025-12-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">We leverage increasingly popular three-dimensional neural representations in order to construct a unified and consistent explanation of a collection of uncalibrated images of the human face. Our approach utilizes Gaussian Splatting, since it is more explicit and thus more amenable to constraints than NeRFs. We leverage segmentation annotations to align the semantic regions of the face, facilitating the reconstruction of a neutral pose from only 11 images (as opposed to requiring a long video). We soft constrain the Gaussians to an underlying triangulated surface in order to provide a more structured Gaussian Splat reconstruction, which in turn informs subsequent perturbations to increase the accuracy of the underlying triangulated surface. The resulting triangulated surface can then be used in a standard graphics pipeline. In addition, and perhaps most impactful, we show how accurate geometry enables the Gaussian Splats to be transformed into texture space where they can be treated as a view-dependent neural texture. This allows one to use high visual fidelity Gaussian Splatting on any asset in a scene without the need to modify any other asset or any other aspect (geometry, lighting, renderer, etc.) of the graphics pipeline. We utilize a relightable Gaussian model to disentangle texture from lighting in order to obtain a delit high-resolution albedo texture that is also readily usable in a standard graphics pipeline. The flexibility of our system allows for training with disparate images, even with incompatible lighting, facilitating robust regularization. Finally, we demonstrate the efficacy of our approach by illustrating its use in a text-driven asset creation pipeline.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.16397">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.16397.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.16397.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">NAP3D: NeRF Assisted 3D-3D Pose Alignment for Autonomous Vehicles</span>
        <span class="paper-authors">Gaurav Bansal</span>
        <span class="paper-meta">Updated 2025-12-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Accurate localization is essential for autonomous vehicles, yet sensor noise and drift over time can lead to significant pose estimation errors, particularly in long-horizon environments. A common strategy for correcting accumulated error is visual loop closure in SLAM, which adjusts the pose graph when the agent revisits previously mapped locations. These techniques typically rely on identifying visual mappings between the current view and previously observed scenes and often require fusing data from multiple sensors.   In contrast, this work introduces NeRF-Assisted 3D-3D Pose Alignment (NAP3D), a complementary approach that leverages 3D-3D correspondences between the agent&#x27;s current depth image and a pre-trained Neural Radiance Field (NeRF). By directly aligning 3D points from the observed scene with synthesized points from the NeRF, NAP3D refines the estimated pose even from novel viewpoints, without relying on revisiting previously observed locations.   This robust 3D-3D formulation provides advantages over conventional 2D-3D localization methods while remaining comparable in accuracy and applicability. Experiments demonstrate that NAP3D achieves camera pose correction within 5 cm on a custom dataset, robustly outperforming a 2D-3D Perspective-N-Point baseline. On TUM RGB-D, NAP3D consistently improves 3D alignment RMSE by approximately 6 cm compared to this baseline given varying noise, despite PnP achieving lower raw rotation and translation parameter error in some regimes, highlighting NAP3D&#x27;s improved geometric consistency in 3D space. By providing a lightweight, dataset-agnostic tool, NAP3D complements existing SLAM and localization pipelines when traditional loop closure is unavailable.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.15080">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.15080.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.15080.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Broadening View Synthesis of Dynamic Scenes from Constrained Monocular Videos</span>
        <span class="paper-authors">Le Jiang et.al.</span>
        <span class="paper-meta">Updated 2025-12-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.14406">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.14406.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.14406.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">HGS: Hybrid Gaussian Splatting with Static-Dynamic Decomposition for Compact Dynamic View Synthesis</span>
        <span class="paper-authors">Kaizhe Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-12-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.14352">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.14352.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.14352.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">AnchorHOI: Zero-shot Generation of 4D Human-Object Interaction via Anchor-based Prior Distillation</span>
        <span class="paper-authors">Sisi Dai et.al.</span>
        <span class="paper-meta">Updated 2025-12-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.14095">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.14095.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.14095.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Quantum Implicit Neural Representations for 3D Scene Reconstruction and Novel View Synthesis</span>
        <span class="paper-authors">Yeray Cordero et.al.</span>
        <span class="paper-meta">Updated 2025-12-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.12683">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.12683.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.12683.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Physically Aware 360$^\circ$ View Generation from a Single Image using Disentangled Scene Embeddings</span>
        <span class="paper-authors">Karthikeya KV et.al.</span>
        <span class="paper-meta">Updated 2025-12-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.10293">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.10293.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.10293.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Relightable and Dynamic Gaussian Avatar Reconstruction from Monocular Video</span>
        <span class="paper-authors">Seonghwa Choi et.al.</span>
        <span class="paper-meta">Updated 2025-12-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.09335">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.09335.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.09335.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Log NeRF: Comparing Spaces for Learning Radiance Fields</span>
        <span class="paper-authors">Sihe Chen et.al.</span>
        <span class="paper-meta">Updated 2025-12-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.09375">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.09375.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.09375.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">AGORA: Adversarial Generation Of Real-time Animatable 3D Gaussian Head Avatars</span>
        <span class="paper-authors">Ramazan Fazylov et.al.</span>
        <span class="paper-meta">Updated 2025-12-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.06438">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.06438.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.06438.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">HybridSplat: Fast Reflection-baked Gaussian Tracing using Hybrid Splatting</span>
        <span class="paper-authors">Chang Liu et.al.</span>
        <span class="paper-meta">Updated 2025-12-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.08334">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.08334.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.08334.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Blur2Sharp: Human Novel Pose and View Synthesis with Generative Prior Refinement</span>
        <span class="paper-authors">Chia-Hern Lai et.al.</span>
        <span class="paper-meta">Updated 2025-12-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.08215">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.08215.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.08215.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">From Orbit to Ground: Generative City Photogrammetry from Extreme Off-Nadir Satellite Images</span>
        <span class="paper-authors">Fei Yu et.al.</span>
        <span class="paper-meta">Updated 2025-12-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.07527">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.07527.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.07527.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Radiance-Field Reinforced Pretraining: Scaling Localization Models with Unlabeled Wireless Signals</span>
        <span class="paper-authors">Guosheng Wang et.al.</span>
        <span class="paper-meta">Updated 2025-12-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.07309">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.07309.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.07309.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Gaussian Entropy Fields: Driving Adaptive Sparsity in 3D Gaussian Optimization</span>
        <span class="paper-authors">Hong Kuang et.al.</span>
        <span class="paper-meta">Updated 2025-12-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.04542">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.04542.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.04542.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Radiance Meshes for Volumetric Reconstruction</span>
        <span class="paper-authors">Alexander Mai et.al.</span>
        <span class="paper-meta">Updated 2025-12-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.04076">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.04076.pdf">PDF</a>
          <a class="chip" href="https://github.com/half-potato/radiance_meshes">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.04076.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">What Is The Best 3D Scene Representation for Robotics? From Geometric to Foundation Models</span>
        <span class="paper-authors">Tianchen Deng et.al.</span>
        <span class="paper-meta">Updated 2025-12-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.03422">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.03422.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.03422.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Flux4D: Flow-based Unsupervised 4D Reconstruction</span>
        <span class="paper-authors">Jingkang Wang et.al.</span>
        <span class="paper-meta">Updated 2025-12-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.03210">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.03210.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.03210.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">PolarGuide-GSDR: 3D Gaussian Splatting Driven by Polarization Priors and Deferred Reflection for Real-World Reflective Scenes</span>
        <span class="paper-authors">Derui Shan et.al.</span>
        <span class="paper-meta">Updated 2025-12-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.02664">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.02664.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.02664.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SplatSuRe: Selective Super-Resolution for Multi-view Consistent 3D Gaussian Splatting</span>
        <span class="paper-authors">Pranav Asthana et.al.</span>
        <span class="paper-meta">Updated 2025-12-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.02172">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.02172.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.02172.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">EGG-Fusion: Efficient 3D Reconstruction with Geometry-aware Gaussian Surfel on the Fly</span>
        <span class="paper-authors">Xiaokun Pan et.al.</span>
        <span class="paper-meta">Updated 2025-12-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.01296">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.01296.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.01296.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Dynamic-eDiTor: Training-Free Text-Driven 4D Scene Editing with Multimodal Diffusion Transformer</span>
        <span class="paper-authors">Dong In Lee et.al.</span>
        <span class="paper-meta">Updated 2025-11-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.00677">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.00677.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.00677.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SplatFont3D: Structure-Aware Text-to-3D Artistic Font Generation with Part-Level Style Control</span>
        <span class="paper-authors">Ji Gan et.al.</span>
        <span class="paper-meta">Updated 2025-11-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2512.00413">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2512.00413.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2512.00413.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Image Valuation in NeRF-based 3D reconstruction</span>
        <span class="paper-authors">Grigorios Aris Cheimariotis et.al.</span>
        <span class="paper-meta">Updated 2025-11-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.23052">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.23052.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.23052.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">$Δ$-NeRF: Incremental Refinement of Neural Radiance Fields through Residual Control and Knowledge Transfer</span>
        <span class="paper-authors">Kriti Ghosh et.al.</span>
        <span class="paper-meta">Updated 2025-11-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.20804">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.20804.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.20804.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Proxy-Free Gaussian Splats Deformation with Splat-Based Surface Estimation</span>
        <span class="paper-authors">Jaeyeong Kim et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.19542">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.19542.pdf">PDF</a>
          <a class="chip" href="https://github.com/kjae0/SpLap">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.19542.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MapRF: Weakly Supervised Online HD Map Construction via NeRF-Guided Self-Training</span>
        <span class="paper-authors">Hongyu Lyu et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.19527">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.19527.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.19527.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">TPG-INR: Target Prior-Guided Implicit 3D CT Reconstruction for Enhanced Sparse-view Imaging</span>
        <span class="paper-authors">Qinglei Cao et.al.</span>
        <span class="paper-meta">Updated 2025-11-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.18806">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.18806.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.18806.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ReCoGS: Real-time ReColoring for Gaussian Splatting scenes</span>
        <span class="paper-authors">Lorenzo Rutayisire et.al.</span>
        <span class="paper-meta">Updated 2025-11-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.18441">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.18441.pdf">PDF</a>
          <a class="chip" href="https://github.com/loryruta/ReCoGS">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.18441.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">AIA-UltraNeRF:Acoustic-Impedance-Aware Neural Radiance Field with Hash Encodings for Robotic Ultrasound Reconstruction and Localization</span>
        <span class="paper-authors">Shuai Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-11-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.18293">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.18293.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.18293.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">NoPe-NeRF++: Local-to-Global Optimization of NeRF with No Pose Prior</span>
        <span class="paper-authors">Dongbo Shi et.al.</span>
        <span class="paper-meta">Updated 2025-11-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.17322">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.17322.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.17322.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">EOGS++: Earth Observation Gaussian Splatting with Internal Camera Refinement and Direct Panchromatic Rendering</span>
        <span class="paper-authors">Pierrick Bournez et.al.</span>
        <span class="paper-meta">Updated 2025-11-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.16542">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.16542.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.16542.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">iGaussian: Real-Time Camera Pose Estimation via Feed-Forward 3D Gaussian Splatting Inversion</span>
        <span class="paper-authors">Hao Wang et.al.</span>
        <span class="paper-meta">Updated 2025-11-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.14149">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.14149.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.14149.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">PFAvatar: Pose-Fusion 3D Personalized Avatar Reconstruction from Real-World Outfit-of-the-Day Photos</span>
        <span class="paper-authors">Dianbing Xi et.al.</span>
        <span class="paper-meta">Updated 2025-11-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.12935">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.12935.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.12935.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">OPFormer: Object Pose Estimation leveraging foundation model with geometric encoding</span>
        <span class="paper-authors">Artem Moroz et.al.</span>
        <span class="paper-meta">Updated 2025-11-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.12614">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.12614.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.12614.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LiDAR-GS++:Improving LiDAR Gaussian Reconstruction via Diffusion Priors</span>
        <span class="paper-authors">Qifeng Chen et.al.</span>
        <span class="paper-meta">Updated 2025-11-15</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.12304">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.12304.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.12304.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">RePose-NeRF: Robust Radiance Fields for Mesh Reconstruction under Noisy Camera Poses</span>
        <span class="paper-authors">Sriram Srinivasan et.al.</span>
        <span class="paper-meta">Updated 2025-11-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.08545">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.08545.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.08545.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Is It Truly Necessary to Process and Fit Minutes-Long Reference Videos for Personalized Talking Face Generation?</span>
        <span class="paper-authors">Rui-Qing Sun et.al.</span>
        <span class="paper-meta">Updated 2025-11-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.07940">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.07940.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.07940.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Sparse4DGS: 4D Gaussian Splatting for Sparse-Frame Dynamic Scene Reconstruction</span>
        <span class="paper-authors">Changyue Shi et.al.</span>
        <span class="paper-meta">Updated 2025-11-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.07122">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.07122.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.07122.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Inpaint360GS: Efficient Object-Aware 3D Inpainting via Gaussian Splatting for 360° Scenes</span>
        <span class="paper-authors">Shaoxiang Wang et.al.</span>
        <span class="paper-meta">Updated 2025-11-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.06457">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.06457.pdf">PDF</a>
          <a class="chip" href="https://github.com/dfki-av/Inpaint360GS">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.06457.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">VDNeRF: Vision-only Dynamic Neural Radiance Field for Urban Scenes</span>
        <span class="paper-authors">Zhengyu Zou et.al.</span>
        <span class="paper-meta">Updated 2025-11-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.06408">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.06408.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.06408.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">4D3R: Motion-Aware Neural Reconstruction and Rendering of Dynamic Scenes from Monocular Videos</span>
        <span class="paper-authors">Mengqi Guo et.al.</span>
        <span class="paper-meta">Updated 2025-11-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.05229">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.05229.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.05229.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Efficient representation of 3D spatial data for defense-related applications</span>
        <span class="paper-authors">Benjamin Kahl et.al.</span>
        <span class="paper-meta">Updated 2025-11-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.05109">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.05109.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.05109.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">3D Gaussian Point Encoders</span>
        <span class="paper-authors">Jim James et.al.</span>
        <span class="paper-meta">Updated 2025-11-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.04797">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.04797.pdf">PDF</a>
          <a class="chip" href="https://github.com/asalarpour/Point_GN">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.04797.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FastGS: Training 3D Gaussian Splatting in 100 Seconds</span>
        <span class="paper-authors">Shiwei Ren et.al.</span>
        <span class="paper-meta">Updated 2025-11-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.04283">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.04283.pdf">PDF</a>
          <a class="chip" href="https://github.com/fastgs/FastGS">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.04283.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LiteVoxel: Low-memory Intelligent Thresholding for Efficient Voxel Rasterization</span>
        <span class="paper-authors">Jee Won Lee et.al.</span>
        <span class="paper-meta">Updated 2025-11-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.02510">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.02510.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.02510.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Object-Centric 3D Gaussian Splatting for Strawberry Plant Reconstruction and Phenotyping</span>
        <span class="paper-authors">Jiajia Li et.al.</span>
        <span class="paper-meta">Updated 2025-11-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2511.02207">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2511.02207.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2511.02207.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GauSSmart: Enhanced 3D Reconstruction through 2D Foundation Models and Geometric Filtering</span>
        <span class="paper-authors">Alexander Valverde et.al.</span>
        <span class="paper-meta">Updated 2025-11-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.14270">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.14270.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.14270.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SAGS: Self-Adaptive Alias-Free Gaussian Splatting for Dynamic Surgical Endoscopic Reconstruction</span>
        <span class="paper-authors">Wenfeng Huang et.al.</span>
        <span class="paper-meta">Updated 2025-10-31</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.27318">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.27318.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.27318.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">4-Doodle: Text to 3D Sketches that Move!</span>
        <span class="paper-authors">Hao Chen et.al.</span>
        <span class="paper-meta">Updated 2025-10-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.25319">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.25319.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.25319.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">I2-NeRF: Learning Neural Radiance Fields Under Physically-Grounded Media Interactions</span>
        <span class="paper-authors">Shuhong Liu et.al.</span>
        <span class="paper-meta">Updated 2025-10-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.22161">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.22161.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.22161.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">From Far and Near: Perceptual Evaluation of Crowd Representations Across Levels of Detail</span>
        <span class="paper-authors">Xiaohan Sun et.al.</span>
        <span class="paper-meta">Updated 2025-10-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.20558">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.20558.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.20558.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Extreme Views: 3DGS Filter for Novel View Synthesis from Out-of-Distribution Camera Poses</span>
        <span class="paper-authors">Damian Bowness et.al.</span>
        <span class="paper-meta">Updated 2025-10-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.20027">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.20027.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.20027.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">AegisRF: Adversarial Perturbations Guided with Sensitivity for Protecting Intellectual Property of Neural Radiance Fields</span>
        <span class="paper-authors">Woo Jae Kim et.al.</span>
        <span class="paper-meta">Updated 2025-10-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.19371">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.19371.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.19371.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Advances in 4D Representation: Geometry, Motion, and Interaction</span>
        <span class="paper-authors">Mingrui Zhao et.al.</span>
        <span class="paper-meta">Updated 2025-10-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.19255">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.19255.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.19255.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SimULi: Real-Time LiDAR and Camera Simulation with Unscented Transforms</span>
        <span class="paper-authors">Haithem Turki et.al.</span>
        <span class="paper-meta">Updated 2025-10-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.12901">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.12901.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.12901.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Perspective-aware 3D Gaussian Inpainting with Multi-view Consistency</span>
        <span class="paper-authors">Yuxin Cheng et.al.</span>
        <span class="paper-meta">Updated 2025-10-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.10993">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.10993.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.10993.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Opacity-Gradient Driven Density Control for Compact and Efficient Few-Shot 3D Gaussian Splatting</span>
        <span class="paper-authors">Abdelrhman Elrawy et.al.</span>
        <span class="paper-meta">Updated 2025-10-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.10257">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.10257.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.10257.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Gesplat: Robust Pose-Free 3D Reconstruction via Geometry-Guided Gaussian Splatting</span>
        <span class="paper-authors">Jiahui Lu et.al.</span>
        <span class="paper-meta">Updated 2025-10-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.10097">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.10097.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.10097.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Geometry-Aware Scene Configurations for Novel View Synthesis</span>
        <span class="paper-authors">Minkwan Kim et.al.</span>
        <span class="paper-meta">Updated 2025-10-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.09880">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.09880.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.09880.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Vision Language Models: A Survey of 26K Papers</span>
        <span class="paper-authors">Fengming Lin et.al.</span>
        <span class="paper-meta">Updated 2025-10-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.09586">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.09586.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.09586.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">HERO: Hardware-Efficient RL-based Optimization Framework for NeRF Quantization</span>
        <span class="paper-authors">Yipu Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-10-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.09010">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.09010.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.09010.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">An Energy-Efficient Edge Coprocessor for Neural Rendering with Explicit Data Reuse Strategies</span>
        <span class="paper-authors">Binzhe Yuan et.al.</span>
        <span class="paper-meta">Updated 2025-10-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.07667">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.07667.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.07667.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.25191.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">OracleGS: Grounding Generative Priors for Sparse-View Gaussian Splatting</span>
        <span class="paper-authors">Atakan Topaloglu et.al.</span>
        <span class="paper-meta">Updated 2025-10-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.23258">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.23258.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.23258.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ROGR: Relightable 3D Objects using Generative Relighting</span>
        <span class="paper-authors">Jiapeng Tang et.al.</span>
        <span class="paper-meta">Updated 2025-10-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.03163">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.03163.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.03163.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">StealthAttack: Robust 3D Gaussian Splatting Poisoning via Density-Guided Illusions</span>
        <span class="paper-authors">Bo-Hsu Ke et.al.</span>
        <span class="paper-meta">Updated 2025-10-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.02314">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.02314.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.02314.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GEM: 3D Gaussian Splatting for Efficient and Accurate Cryo-EM Reconstruction</span>
        <span class="paper-authors">Huaizhi Qu et.al.</span>
        <span class="paper-meta">Updated 2025-10-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.25075">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.25075.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.25075.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Multi-level Dynamic Style Transfer for NeRFs</span>
        <span class="paper-authors">Zesheng Li et.al.</span>
        <span class="paper-meta">Updated 2025-10-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2510.00592">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2510.00592.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2510.00592.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FM-SIREN &amp; FM-FINER: Nyquist-Informed Frequency Multiplier for Implicit Neural Representation with Periodic Activation</span>
        <span class="paper-authors">Mohammed Alsakabi et.al.</span>
        <span class="paper-meta">Updated 2025-09-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.23438">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.23438.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.23438.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene Representations</span>
        <span class="paper-authors">Javed Ahmad et.al.</span>
        <span class="paper-meta">Updated 2025-09-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.23555">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.23555.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.23555.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">WaveletGaussian: Wavelet-domain Diffusion for Sparse-view 3D Gaussian Object Reconstruction</span>
        <span class="paper-authors">Hung Nguyen et.al.</span>
        <span class="paper-meta">Updated 2025-09-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.19073">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.19073.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.19073.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Seeing Through Reflections: Advancing 3D Scene Reconstruction in Mirror-Containing Environments with Gaussian Splatting</span>
        <span class="paper-authors">Zijing Guo et.al.</span>
        <span class="paper-meta">Updated 2025-09-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.18956">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.18956.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.18956.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">HyRF: Hybrid Radiance Fields for Memory-efficient and High-quality Novel View Synthesis</span>
        <span class="paper-authors">Zipeng Wang et.al.</span>
        <span class="paper-meta">Updated 2025-09-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.17083">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.17083.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.17083.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">From Restoration to Reconstruction: Rethinking 3D Gaussian Splatting for Underwater Scenes</span>
        <span class="paper-authors">Guoxi Huang et.al.</span>
        <span class="paper-meta">Updated 2025-09-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.17789">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.17789.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.17789.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild</span>
        <span class="paper-authors">Deming Li et.al.</span>
        <span class="paper-meta">Updated 2025-09-22</span>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DT-NeRF: A Diffusion and Transformer-Based Optimization Approach for Neural Radiance Fields in 3D Reconstruction</span>
        <span class="paper-authors">Bo Liu et.al.</span>
        <span class="paper-meta">Updated 2025-09-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.17232">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.17232.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.17232.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">PGSTalker: Real-Time Audio-Driven Talking Head Generation via 3D Gaussian Splatting with Pixel-Aware Density Control</span>
        <span class="paper-authors">Tianheng Zhu et.al.</span>
        <span class="paper-meta">Updated 2025-09-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.16922">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.16922.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.16922.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">RGB-Only Supervised Camera Parameter Optimization in Dynamic Scenes</span>
        <span class="paper-authors">Fang Li et.al.</span>
        <span class="paper-meta">Updated 2025-09-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.15123">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.15123.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.15123.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">NeRF-based Visualization of 3D Cues Supporting Data-Driven Spacecraft Pose Estimation</span>
        <span class="paper-authors">Antoine Legrand et.al.</span>
        <span class="paper-meta">Updated 2025-09-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.14890">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.14890.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.14890.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ProFusion: 3D Reconstruction of Protein Complex Structures from Multi-view AFM Images</span>
        <span class="paper-authors">Jaydeep Rade et.al.</span>
        <span class="paper-meta">Updated 2025-09-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.15242">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.15242.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.15242.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SuNeRF-CME: Physics-Informed Neural Radiance Fields for Tomographic Reconstruction of Coronal Mass Ejections</span>
        <span class="paper-authors">Robert Jarolim et.al.</span>
        <span class="paper-meta">Updated 2025-09-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.13571">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.13571.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.13571.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Exploring Metric Fusion for Evaluation of NeRFs</span>
        <span class="paper-authors">Shreyas Shivakumara et.al.</span>
        <span class="paper-meta">Updated 2025-09-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.12836">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.12836.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.12836.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ROSGS: Relightable Outdoor Scenes With Gaussian Splatting</span>
        <span class="paper-authors">Lianjun Liao et.al.</span>
        <span class="paper-meta">Updated 2025-09-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.11275">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.11275.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.11275.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SPHERE: Semantic-PHysical Engaged REpresentation for 3D Semantic Scene Completion</span>
        <span class="paper-authors">Zhiwen Yang et.al.</span>
        <span class="paper-meta">Updated 2025-09-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.11171">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.11171.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.11171.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Multispectral-NeRF:a multispectral modeling approach based on neural radiance fields</span>
        <span class="paper-authors">Hong Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-09-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.11169">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.11169.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.11169.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SplatFill: 3D Scene Inpainting via Depth-Guided Gaussian Splatting</span>
        <span class="paper-authors">Mahtab Dahaghin et.al.</span>
        <span class="paper-meta">Updated 2025-09-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.07809">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.07809.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.07809.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DiGS: Accurate and Complete Surface Reconstruction from 3D Gaussians via Direct SDF Learning</span>
        <span class="paper-authors">Wenzhi Guo et.al.</span>
        <span class="paper-meta">Updated 2025-09-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.07493">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.07493.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.07493.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GS-TG: 3D Gaussian Splatting Accelerator with Tile Grouping for Reducing Redundant Sorting while Preserving Rasterization Efficiency</span>
        <span class="paper-authors">Joongho Jo et.al.</span>
        <span class="paper-meta">Updated 2025-09-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.00911">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.00911.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.00911.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SWAGSplatting: Semantic-guided Water-scene Augmented Gaussian Splatting</span>
        <span class="paper-authors">Zhuodong Jiang et.al.</span>
        <span class="paper-meta">Updated 2025-08-31</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2509.00800">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2509.00800.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2509.00800.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Adam SLAM - the last mile of camera calibration with 3DGS</span>
        <span class="paper-authors">Matthieu Gendrin et.al.</span>
        <span class="paper-meta">Updated 2025-08-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2508.20526">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2508.20526.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2508.20526.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Generating Human-AI Collaborative Design Sequence for 3D Assets via Differentiable Operation Graph</span>
        <span class="paper-authors">Xiaoyang Huang et.al.</span>
        <span class="paper-meta">Updated 2025-08-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2508.17645">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2508.17645.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2508.17645.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Can we make NeRF-based visual localization privacy-preserving?</span>
        <span class="paper-authors">Maxime Pietrantoni et.al.</span>
        <span class="paper-meta">Updated 2025-08-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2508.18971">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2508.18971.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2508.18971.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Real-time 3D Visualization of Radiance Fields on Light Field Displays</span>
        <span class="paper-authors">Jonghyun Kim et.al.</span>
        <span class="paper-meta">Updated 2025-08-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2508.18540">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2508.18540.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2508.18540.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Align 3D Representation and Text Embedding for 3D Content Personalization</span>
        <span class="paper-authors">Qi Song et.al.</span>
        <span class="paper-meta">Updated 2025-08-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2508.16932">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2508.16932.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2508.16932.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via Gaussian Surfels</span>
        <span class="paper-authors">Xingyuan Yang et.al.</span>
        <span class="paper-meta">Updated 2025-08-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2508.14563">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2508.14563.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2508.14563.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DoRF: Doppler Radiance Fields for Robust Human Activity Recognition Using Wi-Fi</span>
        <span class="paper-authors">Navid Hasanzadeh et.al.</span>
        <span class="paper-meta">Updated 2025-07-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.12132">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.12132.pdf">PDF</a>
          <a class="chip" href="https://github.com/navidhasanzadeh/dorf">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.12132.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">HPR3D: Hierarchical Proxy Representation for High-Fidelity 3D Reconstruction and Controllable Editing</span>
        <span class="paper-authors">Tielong Wang et.al.</span>
        <span class="paper-meta">Updated 2025-07-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.11971">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.11971.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.11971.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">VoxelRF: Voxelized Radiance Field for Fast Wireless Channel Modeling</span>
        <span class="paper-authors">Zihang Zeng et.al.</span>
        <span class="paper-meta">Updated 2025-07-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.09987">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.09987.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.09987.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">BayesSDF: Surface-Based Laplacian Uncertainty Estimation for 3D Geometry with Neural Signed Distance Fields</span>
        <span class="paper-authors">Rushil Desai et.al.</span>
        <span class="paper-meta">Updated 2025-07-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.06269">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.06269.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.06269.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Stable Score Distillation</span>
        <span class="paper-authors">Haiming Zhu et.al.</span>
        <span class="paper-meta">Updated 2025-07-12</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.09168">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.09168.pdf">PDF</a>
          <a class="chip" href="https://github.com/nicolasdaire/diffusion-nerf">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.09168.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">From images to properties: a NeRF-driven framework for granular material parameter inversion</span>
        <span class="paper-authors">Cheng-Hsi Hsiao et.al.</span>
        <span class="paper-meta">Updated 2025-07-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.09005">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.09005.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.09005.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MUVOD: A Novel Multi-view Video Object Segmentation Dataset and A Benchmark for 3D Segmentation</span>
        <span class="paper-authors">Bangning Wei et.al.</span>
        <span class="paper-meta">Updated 2025-07-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.07519">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.07519.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.07519.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Reflections Unlock: Geometry-Aware Reflection Disentanglement in 3D Gaussian Splatting for Photorealistic Scenes Rendering</span>
        <span class="paper-authors">Jiayi Song et.al.</span>
        <span class="paper-meta">Updated 2025-07-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.06103">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.06103.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.06103.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DreamArt: Generating Interactable Articulated Objects from a Single Image</span>
        <span class="paper-authors">Ruijie Lu et.al.</span>
        <span class="paper-meta">Updated 2025-07-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.05763">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.05763.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.05763.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A View-consistent Sampling Method for Regularized Training of Neural Radiance Fields</span>
        <span class="paper-authors">Aoxiang Fan et.al.</span>
        <span class="paper-meta">Updated 2025-07-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.04408">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.04408.pdf">PDF</a>
          <a class="chip" href="https://github.com/AoxiangFan/VS-NeRF">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.04408.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Tile and Slide : A New Framework for Scaling NeRF from Local to Global 3D Earth Observation</span>
        <span class="paper-authors">Camille Billouard et.al.</span>
        <span class="paper-meta">Updated 2025-07-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.01631">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.01631.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.01631.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Surgical Neural Radiance Fields from One Image</span>
        <span class="paper-authors">Alberto Neri et.al.</span>
        <span class="paper-meta">Updated 2025-07-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.00969">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.00969.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.00969.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">PlantSegNeRF: A few-shot, cross-dataset method for plant 3D instance point cloud reconstruction via joint-channel NeRF with multi-view image instance matching</span>
        <span class="paper-authors">Xin Yang et.al.</span>
        <span class="paper-meta">Updated 2025-07-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2507.00371">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2507.00371.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2507.00371.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Dynamic View Synthesis from Small Camera Motion Videos</span>
        <span class="paper-authors">Huiqiang Sun et.al.</span>
        <span class="paper-meta">Updated 2025-06-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.23153">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.23153.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.23153.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">UnMix-NeRF: Spectral Unmixing Meets Neural Radiance Fields</span>
        <span class="paper-authors">Fabian Perez et.al.</span>
        <span class="paper-meta">Updated 2025-06-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.21884">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.21884.pdf">PDF</a>
          <a class="chip" href="https://github.com/Factral/UnMix-NeRF">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.21884.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">PanSt3R: Multi-view Consistent Panoptic Segmentation</span>
        <span class="paper-authors">Lojze Zust et.al.</span>
        <span class="paper-meta">Updated 2025-06-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.21348">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.21348.pdf">PDF</a>
          <a class="chip" href="https://github.com/naver/panst3r">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.21348.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">2D Triangle Splatting for Direct Differentiable Mesh Training</span>
        <span class="paper-authors">Kaifeng Sheng et.al.</span>
        <span class="paper-meta">Updated 2025-06-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.18575">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.18575.pdf">PDF</a>
          <a class="chip" href="https://github.com/GaodeRender/triangle-splatting">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.18575.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Joint attitude estimation and 3D neural reconstruction of non-cooperative space objects</span>
        <span class="paper-authors">Clément Forray et.al.</span>
        <span class="paper-meta">Updated 2025-06-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.20638">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.20638.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.20638.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Self-Supervised Multimodal NeRF for Autonomous Driving</span>
        <span class="paper-authors">Gaurav Sharma et.al.</span>
        <span class="paper-meta">Updated 2025-06-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.19615">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.19615.pdf">PDF</a>
          <a class="chip" href="https://github.com/gaurav00700/ProjectPage-Selfsupervised-NVSF">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.19615.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">NeRF-based CBCT Reconstruction needs Normalization and Initialization</span>
        <span class="paper-authors">Zhuowei Xu et.al.</span>
        <span class="paper-meta">Updated 2025-06-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.19742">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.19742.pdf">PDF</a>
          <a class="chip" href="https://github.com/iddifficult/NI_NeRF">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.19742.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">HoliGS: Holistic Gaussian Splatting for Embodied View Synthesis</span>
        <span class="paper-authors">Xiaoyuan Wang et.al.</span>
        <span class="paper-meta">Updated 2025-06-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.19291">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.19291.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.19291.pdf">
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
        <span class="paper-title">R3eVision: A Survey on Robust Rendering, Restoration, and Enhancement for 3D Low-Level Vision</span>
        <span class="paper-authors">Weeyoung Kwon et.al.</span>
        <span class="paper-meta">Updated 2025-06-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.16262">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.16262.pdf">PDF</a>
          <a class="chip" href="https://github.com/cmlab-korea/awesome-3d-low-level-vision">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.16262.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Limitations of NERF with pre-trained Vision Features for Few-Shot 3D Reconstruction</span>
        <span class="paper-authors">Ankit Sanjyal et.al.</span>
        <span class="paper-meta">Updated 2025-06-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.18208">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.18208.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.18208.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in Large-Scale Scene</span>
        <span class="paper-authors">Shihan Chen et.al.</span>
        <span class="paper-meta">Updated 2025-06-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.17636">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.17636.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.17636.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Rasterizing Wireless Radiance Field via Deformable 2D Gaussian Splatting</span>
        <span class="paper-authors">Mufan Liu et.al.</span>
        <span class="paper-meta">Updated 2025-06-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.12787">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.12787.pdf">PDF</a>
          <a class="chip" href="https://github.com/Evan-sudo/Swift_WRF">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.12787.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Peering into the Unknown: Active View Selection with Neural Uncertainty Maps for 3D Reconstruction</span>
        <span class="paper-authors">Zhengquan Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-06-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.14856">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.14856.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.14856.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Efficient multi-view training for 3D Gaussian Splatting</span>
        <span class="paper-authors">Minhyuk Choi et.al.</span>
        <span class="paper-meta">Updated 2025-06-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.12727">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.12727.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.12727.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Genesis: Multimodal Driving Scene Generation with Spatio-Temporal and Cross-Modal Consistency</span>
        <span class="paper-authors">Xiangyu Guo et.al.</span>
        <span class="paper-meta">Updated 2025-06-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.07497">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.07497.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.07497.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">PointGS: Point Attention-Aware Sparse View Synthesis with Gaussian Splatting</span>
        <span class="paper-authors">Lintao Xiang et.al.</span>
        <span class="paper-meta">Updated 2025-06-12</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.10335">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.10335.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.10335.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">The Less You Depend, The More You Learn: Synthesizing Novel Views from Sparse, Unposed Images without Any 3D Knowledge</span>
        <span class="paper-authors">Haoru Wang et.al.</span>
        <span class="paper-meta">Updated 2025-06-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.09885">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.09885.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.09885.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">A Probability-guided Sampler for Neural Implicit Surface Rendering</span>
        <span class="paper-authors">Gonçalo Dias Pais et.al.</span>
        <span class="paper-meta">Updated 2025-06-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.08619">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.08619.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.08619.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Speedy Deformable 3D Gaussian Splatting: Fast Rendering and Compression of Dynamic Scenes</span>
        <span class="paper-authors">Allen Tu et.al.</span>
        <span class="paper-meta">Updated 2025-06-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.07917">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.07917.pdf">PDF</a>
          <a class="chip" href="https://github.com/tuallen/speede3dgs">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.07917.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SPC to 3D: Novel View Synthesis from Binary SPC via I2I translation</span>
        <span class="paper-authors">Sumit Sharma et.al.</span>
        <span class="paper-meta">Updated 2025-06-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.06890">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.06890.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.06890.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Splat and Replace: 3D Reconstruction with Repetitive Elements</span>
        <span class="paper-authors">Nicolás Violante et.al.</span>
        <span class="paper-meta">Updated 2025-06-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.06462">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.06462.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.06462.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">NeurNCD: Novel Class Discovery via Implicit Neural Representation</span>
        <span class="paper-authors">Junming Wang et.al.</span>
        <span class="paper-meta">Updated 2025-06-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.06412">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.06412.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.06412.pdf">
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
        <span class="paper-title">ProJo4D: Progressive Joint Optimization for Sparse-View Inverse Physics Estimation</span>
        <span class="paper-authors">Daniel Rho et.al.</span>
        <span class="paper-meta">Updated 2025-06-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.05317">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.05317.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.05317.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Unifying Appearance Codes and Bilateral Grids for Driving Scene Gaussian Splatting</span>
        <span class="paper-authors">Nan Wang et.al.</span>
        <span class="paper-meta">Updated 2025-06-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.05280">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.05280.pdf">PDF</a>
          <a class="chip" href="https://github.com/bigcileng/bilateral-driving">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.05280.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Generating Synthetic Stereo Datasets using 3D Gaussian Splatting and Expert Knowledge Transfer</span>
        <span class="paper-authors">Filip Slezak et.al.</span>
        <span class="paper-meta">Updated 2025-06-05</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.04908">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.04908.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.04908.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Hi-Dyna Graph: Hierarchical Dynamic Scene Graph for Robotic Autonomy in Human-Centric Environments</span>
        <span class="paper-authors">Jiawei Hou et.al.</span>
        <span class="paper-meta">Updated 2025-05-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2506.00083">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2506.00083.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2506.00083.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ErpGS: Equirectangular Image Rendering enhanced with 3D Gaussian Regularization</span>
        <span class="paper-authors">Shintaro Ito et.al.</span>
        <span class="paper-meta">Updated 2025-05-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.19883">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.19883.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.19883.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">PhysicsNeRF: Physics-Guided 3D Reconstruction from Sparse Views</span>
        <span class="paper-authors">Mohamed Rayan Barhdadi et.al.</span>
        <span class="paper-meta">Updated 2025-05-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.23481">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.23481.pdf">PDF</a>
          <a class="chip" href="https://github.com/anonymous-researcher-01/physicsnerf">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.23481.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LODGE: Level-of-Detail Large-Scale Gaussian Splatting with Efficient Rendering</span>
        <span class="paper-authors">Jonas Kulhanek et.al.</span>
        <span class="paper-meta">Updated 2025-05-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.23158">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.23158.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.23158.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Can NeRFs See without Cameras?</span>
        <span class="paper-authors">Chaitanya Amballa et.al.</span>
        <span class="paper-meta">Updated 2025-05-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.22441">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.22441.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.22441.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Learning Fine-Grained Geometry for Sparse-View Splatting via Cascade Depth Loss</span>
        <span class="paper-authors">Wenjun Lu et.al.</span>
        <span class="paper-meta">Updated 2025-05-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.22279">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.22279.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.22279.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Hyperspectral Gaussian Splatting</span>
        <span class="paper-authors">Sunil Kumar Narayanan et.al.</span>
        <span class="paper-meta">Updated 2025-05-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.21890">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.21890.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.21890.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Structure from Collision</span>
        <span class="paper-authors">Takuhiro Kaneko et.al.</span>
        <span class="paper-meta">Updated 2025-05-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.21335">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.21335.pdf">PDF</a>
          <a class="chip" href="https://github.com/Aryia-Behroziuan/neurons">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.21335.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">OB3D: A New Dataset for Benchmarking Omnidirectional 3D Reconstruction Using Blender</span>
        <span class="paper-authors">Shintaro Ito et.al.</span>
        <span class="paper-meta">Updated 2025-05-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.20126">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.20126.pdf">PDF</a>
          <a class="chip" href="https://github.com/gsisaoki/omnidirectional_blender_3d_dataset">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.20126.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GoLF-NRT: Integrating Global Context and Local Geometry for Few-Shot View Synthesis</span>
        <span class="paper-authors">You Wang et.al.</span>
        <span class="paper-meta">Updated 2025-05-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.19813">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.19813.pdf">PDF</a>
          <a class="chip" href="https://github.com/klmav-cuc/golf-nrt">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.19813.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Depth-Guided Bundle Sampling for Efficient Generalizable Neural Radiance Field Reconstruction</span>
        <span class="paper-authors">Li Fang et.al.</span>
        <span class="paper-meta">Updated 2025-05-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.19793">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.19793.pdf">PDF</a>
          <a class="chip" href="https://github.com/klmav-cuc/gdb-nerf">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.19793.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">UAV See, UGV Do: Aerial Imagery and Virtual Teach Enabling Zero-Shot Ground Vehicle Repeat</span>
        <span class="paper-authors">Desiree Fisker et.al.</span>
        <span class="paper-meta">Updated 2025-05-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.16912">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.16912.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.16912.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">IPENS:Interactive Unsupervised Framework for Rapid Plant Phenotyping Extraction via NeRF-SAM2 Fusion</span>
        <span class="paper-authors">Wentao Song et.al.</span>
        <span class="paper-meta">Updated 2025-05-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.13633">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.13633.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.13633.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">3D Gaussian Adaptive Reconstruction for Fourier Light-Field Microscopy</span>
        <span class="paper-authors">Chenyu Xu et.al.</span>
        <span class="paper-meta">Updated 2025-05-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.12875">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.12875.pdf">PDF</a>
          <a class="chip" href="https://github.com/Chaos1025/3DGAT">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.12875.pdf">
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
        <span class="paper-title">MutualNeRF: Improve the Performance of NeRF under Limited Samples with Mutual Information Theory</span>
        <span class="paper-authors">Zifan Wang et.al.</span>
        <span class="paper-meta">Updated 2025-05-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.11386">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.11386.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.11386.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">EA-3DGS: Efficient and Adaptive 3D Gaussians with Highly Enhanced Quality for outdoor scenes</span>
        <span class="paper-authors">Jianlin Guo et.al.</span>
        <span class="paper-meta">Updated 2025-05-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.10787">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.10787.pdf">PDF</a>
          <a class="chip" href="https://github.com/scut-bip-lab/ea-3dgs">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.10787.pdf">
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
        <span class="paper-title">Sparse Point Cloud Patches Rendering via Splitting 2D Gaussians</span>
        <span class="paper-authors">Ma Changfeng et.al.</span>
        <span class="paper-meta">Updated 2025-05-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.09413">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.09413.pdf">PDF</a>
          <a class="chip" href="https://github.com/murcherful/gaupcrender">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.09413.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FreeDriveRF: Monocular RGB Dynamic NeRF without Poses for Autonomous Driving via Point-Level Dynamic-Static Decoupling</span>
        <span class="paper-authors">Yue Wen et.al.</span>
        <span class="paper-meta">Updated 2025-05-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.09406">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.09406.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.09406.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FOCI: Trajectory Optimization on Gaussian Splats</span>
        <span class="paper-authors">Mario Gomez Andreu et.al.</span>
        <span class="paper-meta">Updated 2025-05-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.08510">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.08510.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.08510.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">TUM2TWIN: Introducing the Large-Scale Multimodal Urban Digital Twin Benchmark Dataset</span>
        <span class="paper-authors">Olaf Wysocki et.al.</span>
        <span class="paper-meta">Updated 2025-05-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.07396">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.07396.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.07396.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">TUGS: Physics-based Compact Representation of Underwater Scenes by Tensorized Gaussian</span>
        <span class="paper-authors">Shijie Lian et.al.</span>
        <span class="paper-meta">Updated 2025-05-12</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.08811">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.08811.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.08811.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">NeuGen: Amplifying the &#x27;Neural&#x27; in Neural Radiance Fields for Domain Generalization</span>
        <span class="paper-authors">Ahmed Qazi et.al.</span>
        <span class="paper-meta">Updated 2025-05-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.06894">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.06894.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.06894.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">3D Characterization of Smoke Plume Dispersion Using Multi-View Drone Swarm</span>
        <span class="paper-authors">Nikil Krishnakumar et.al.</span>
        <span class="paper-meta">Updated 2025-05-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.06638">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.06638.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.06638.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FlexNeRFer: A Multi-Dataflow, Adaptive Sparsity-Aware Accelerator for On-Device NeRF Rendering</span>
        <span class="paper-authors">Seock-Hwan Noh et.al.</span>
        <span class="paper-meta">Updated 2025-05-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.06504">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.06504.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.06504.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">3D Scene Generation: A Survey</span>
        <span class="paper-authors">Beichen Wen et.al.</span>
        <span class="paper-meta">Updated 2025-05-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.05474">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.05474.pdf">PDF</a>
          <a class="chip" href="https://github.com/hzxie/awesome-3d-scene-generation">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.05474.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">HandOcc: NeRF-based Hand Rendering with Occupancy Networks</span>
        <span class="paper-authors">Maksym Ivashechkin et.al.</span>
        <span class="paper-meta">Updated 2025-05-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.02079">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.02079.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.02079.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Learning Heterogeneous Mixture of Scene Experts for Large-scale Neural Radiance Fields</span>
        <span class="paper-authors">Zhenxing Mi et.al.</span>
        <span class="paper-meta">Updated 2025-05-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.02005">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.02005.pdf">PDF</a>
          <a class="chip" href="https://github.com/MiZhenxing/Switch-NeRF">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.02005.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Unified Steganography via Implicit Neural Representation</span>
        <span class="paper-authors">Qi Song et.al.</span>
        <span class="paper-meta">Updated 2025-05-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.01749">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.01749.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.01749.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Cues3D: Unleashing the Power of Sole NeRF for Consistent and Unique Instances in Open-Vocabulary 3D Panoptic Segmentation</span>
        <span class="paper-authors">Feng Xue et.al.</span>
        <span class="paper-meta">Updated 2025-05-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.00378">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.00378.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.00378.pdf">
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
        <span class="paper-title">A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond</span>
        <span class="paper-authors">Jiajia Li et.al.</span>
        <span class="paper-meta">Updated 2025-04-30</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2505.00737">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2505.00737.pdf">PDF</a>
          <a class="chip" href="https://github.com/jiajiali04/3d-reconstruction-plants">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2505.00737.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GauSS-MI: Gaussian Splatting Shannon Mutual Information for Active 3D Reconstruction</span>
        <span class="paper-authors">Yuhan Xie et.al.</span>
        <span class="paper-meta">Updated 2025-04-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.21067">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.21067.pdf">PDF</a>
          <a class="chip" href="https://github.com/JohannaXie/GauSS-MI">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.21067.pdf">
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">IM-Portrait: Learning 3D-aware Video Diffusion for Photorealistic Talking Heads from Monocular Videos</span>
        <span class="paper-authors">Yuan Li et.al.</span>
        <span class="paper-meta">Updated 2025-04-29</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.19165">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.19165.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.19165.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Joint Optimization of Neural Radiance Fields and Continuous Camera Motion from a Monocular Video</span>
        <span class="paper-authors">Hoang Chuong Nguyen et.al.</span>
        <span class="paper-meta">Updated 2025-04-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.19819">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.19819.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.19819.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">RGS-DR: Reflective Gaussian Surfels with Deferred Rendering for Shiny Objects</span>
        <span class="paper-authors">Georgios Kouros et.al.</span>
        <span class="paper-meta">Updated 2025-04-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.18468">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.18468.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.18468.pdf">
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
        <span class="paper-title">CasualHDRSplat: Robust High Dynamic Range 3D Gaussian Splatting from Casually Captured Videos</span>
        <span class="paper-authors">Shucheng Gong et.al.</span>
        <span class="paper-meta">Updated 2025-04-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.17728">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.17728.pdf">PDF</a>
          <a class="chip" href="https://github.com/wu-cvgl/casualhdrsplat">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.17728.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Dual-Camera All-in-Focus Neural Radiance Fields</span>
        <span class="paper-authors">Xianrui Luo et.al.</span>
        <span class="paper-meta">Updated 2025-04-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.16636">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.16636.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.16636.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Beyond Anonymization: Object Scrubbing for Privacy-Preserving 2D and 3D Vision Tasks</span>
        <span class="paper-authors">Murat Bilgehan Ertan et.al.</span>
        <span class="paper-meta">Updated 2025-04-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.16557">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.16557.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.16557.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SaENeRF: Suppressing Artifacts in Event-based Neural Radiance Fields</span>
        <span class="paper-authors">Yuanjian Wang et.al.</span>
        <span class="paper-meta">Updated 2025-04-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.16389">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.16389.pdf">PDF</a>
          <a class="chip" href="https://github.com/mr-firework/saenerf">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.16389.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Pose Optimization for Autonomous Driving Datasets using Neural Rendering Models</span>
        <span class="paper-authors">Quentin Herau et.al.</span>
        <span class="paper-meta">Updated 2025-04-22</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.15776">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.15776.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.15776.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">StyleMe3D: Stylization with Disentangled Priors by Multiple Encoders on 3D Gaussians</span>
        <span class="paper-authors">Cailin Zhuang et.al.</span>
        <span class="paper-meta">Updated 2025-04-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.15281">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.15281.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.15281.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SLAM&amp;Render: A Benchmark for the Intersection Between Neural Rendering, Gaussian Splatting and SLAM</span>
        <span class="paper-authors">Samuel Cerezo et.al.</span>
        <span class="paper-meta">Updated 2025-04-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.13713">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.13713.pdf">PDF</a>
          <a class="chip" href="https://github.com/samuel-cerezo/SLAM-Render">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.13713.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Scaling LLaNA: Advancing NeRF-Language Understanding Through Large-Scale Training</span>
        <span class="paper-authors">Andrea Amaduzzi et.al.</span>
        <span class="paper-meta">Updated 2025-04-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.13995">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.13995.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.13995.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GSAC: Leveraging Gaussian Splatting for Photorealistic Avatar Creation with Unity Integration</span>
        <span class="paper-authors">Rendong Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-04-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.12999">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.12999.pdf">PDF</a>
          <a class="chip" href="https://github.com/VU-RASL/GSAC">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.12999.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">R-Meshfusion: Reinforcement Learning Powered Sparse-View Mesh Reconstruction with Diffusion Priors</span>
        <span class="paper-authors">Haoyang Wang et.al.</span>
        <span class="paper-meta">Updated 2025-04-16</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.11946">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.11946.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.11946.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LL-Gaussian: Low-Light Scene Reconstruction and Enhancement via Gaussian Splatting for Novel View Synthesis</span>
        <span class="paper-authors">Hao Sun et.al.</span>
        <span class="paper-meta">Updated 2025-04-15</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.10331">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.10331.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.10331.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MCBlock: Boosting Neural Radiance Field Training Speed by MCTS-based Dynamic-Resolution Ray Sampling</span>
        <span class="paper-authors">Yunpeng Tan et.al.</span>
        <span class="paper-meta">Updated 2025-04-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.09878">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.09878.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.09878.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">NeRF-Based Transparent Object Grasping Enhanced by Shape Priors</span>
        <span class="paper-authors">Yi Han et.al.</span>
        <span class="paper-meta">Updated 2025-04-14</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.09868">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.09868.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.09868.pdf">
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
        <span class="paper-title">Wheat3DGS: In-field 3D Reconstruction, Instance Segmentation and Phenotyping of Wheat Heads with Gaussian Splatting</span>
        <span class="paper-authors">Daiwei Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-04-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.06978">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.06978.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.06978.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">S-EO: A Large-Scale Dataset for Geometry-Aware Shadow Detection in Remote Sensing Applications</span>
        <span class="paper-authors">Masquil Elías et.al.</span>
        <span class="paper-meta">Updated 2025-04-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.06920">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.06920.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.06920.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SVG-IR: Spatially-Varying Gaussian Splatting for Inverse Rendering</span>
        <span class="paper-authors">Hanxiao Sun et.al.</span>
        <span class="paper-meta">Updated 2025-04-09</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.06815">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.06815.pdf">PDF</a>
          <a class="chip" href="https://github.com/learner-shx/svg-ir">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.06815.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Meta-Continual Learning of Neural Fields</span>
        <span class="paper-authors">Seungyoon Woo et.al.</span>
        <span class="paper-meta">Updated 2025-04-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.05806">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.05806.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.05806.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">SE4Lip: Speech-Lip Encoder for Talking Head Synthesis to Solve Phoneme-Viseme Alignment Ambiguity</span>
        <span class="paper-authors">Yihuan Huang et.al.</span>
        <span class="paper-meta">Updated 2025-04-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.05803">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.05803.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.05803.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">InvNeRF-Seg: Fine-Tuning a Pre-Trained NeRF for 3D Object Segmentation</span>
        <span class="paper-authors">Jiangsan Zhao et.al.</span>
        <span class="paper-meta">Updated 2025-04-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.05751">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.05751.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.05751.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DeclutterNeRF: Generative-Free 3D Scene Recovery for Occlusion Removal</span>
        <span class="paper-authors">Wanzhou Liu et.al.</span>
        <span class="paper-meta">Updated 2025-04-07</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.04679">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.04679.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.04679.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Thermoxels: a voxel-based method to generate simulation-ready 3D thermal models</span>
        <span class="paper-authors">Etienne Chassaing et.al.</span>
        <span class="paper-meta">Updated 2025-04-06</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.04448">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.04448.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.04448.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">NeRFlex: Resource-aware Real-time High-quality Rendering of Complex Scenes on Mobile Devices</span>
        <span class="paper-authors">Zhe Wang et.al.</span>
        <span class="paper-meta">Updated 2025-04-04</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.03415">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.03415.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.03415.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MultiNeRF: Multiple Watermark Embedding for Neural Radiance Fields</span>
        <span class="paper-authors">Yash Kulthe et.al.</span>
        <span class="paper-meta">Updated 2025-04-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.02517">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.02517.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.02517.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LPA3D: 3D Room-Level Scene Generation from In-the-Wild Images</span>
        <span class="paper-authors">Ming-Jia Yang et.al.</span>
        <span class="paper-meta">Updated 2025-04-03</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.02337">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.02337.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.02337.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Diffusion-Guided Gaussian Splatting for Large-Scale Unconstrained 3D Reconstruction and Novel View Synthesis</span>
        <span class="paper-authors">Niluthpol Chowdhury Mithun et.al.</span>
        <span class="paper-meta">Updated 2025-04-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.01960">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.01960.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.01960.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">BOGausS: Better Optimized Gaussian Splatting</span>
        <span class="paper-authors">Stéphane Pateux et.al.</span>
        <span class="paper-meta">Updated 2025-04-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.01844">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.01844.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.01844.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FIORD: A Fisheye Indoor-Outdoor Dataset with LIDAR Ground Truth for 3D Scene Reconstruction and Benchmarking</span>
        <span class="paper-authors">Ulas Gunes et.al.</span>
        <span class="paper-meta">Updated 2025-04-02</span>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">RealityAvatar: Towards Realistic Loose Clothing Modeling in Animatable 3D Gaussian Avatars</span>
        <span class="paper-authors">Yahui Li et.al.</span>
        <span class="paper-meta">Updated 2025-04-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.01559">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.01559.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.01559.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Luminance-GS: Adapting 3D Gaussian Splatting to Challenging Lighting Conditions with View-Adaptive Curve Adjustment</span>
        <span class="paper-authors">Ziteng Cui et.al.</span>
        <span class="paper-meta">Updated 2025-04-02</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.01503">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.01503.pdf">PDF</a>
          <a class="chip" href="https://github.com/cuiziteng/Luminance-GS">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.01503.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">OccludeNeRF: Geometric-aware 3D Scene Inpainting with Collaborative Score Distillation in NeRF</span>
        <span class="paper-authors">Jingyu Shi et.al.</span>
        <span class="paper-meta">Updated 2025-04-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.02007">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.02007.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.02007.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Neural Pruning for 3D Scene Reconstruction: Efficient NeRF Acceleration</span>
        <span class="paper-authors">Tianqi Ding et.al.</span>
        <span class="paper-meta">Updated 2025-04-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.00950">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.00950.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.00950.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">NeuRadar: Neural Radiance Fields for Automotive Radar Point Clouds</span>
        <span class="paper-authors">Mahan Rafidashti et.al.</span>
        <span class="paper-meta">Updated 2025-04-01</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2504.00859">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2504.00859.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2504.00859.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ABC-GS: Alignment-Based Controllable Style Transfer for 3D Gaussian Splatting</span>
        <span class="paper-authors">Wenjie Liu et.al.</span>
        <span class="paper-meta">Updated 2025-03-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.22218">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.22218.pdf">PDF</a>
          <a class="chip" href="https://github.com/vpx-ecnu/ABC-GS">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.22218.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LandMarkSystem Technical Report</span>
        <span class="paper-authors">Zhenxiang Ma et.al.</span>
        <span class="paper-meta">Updated 2025-03-28</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.21364">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.21364.pdf">PDF</a>
          <a class="chip" href="https://github.com/internlandmark/landmarksystem">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.21364.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">NeRF-based Point Cloud Reconstruction using a Stationary Camera for Agricultural Applications</span>
        <span class="paper-authors">Kibon Ku et.al.</span>
        <span class="paper-meta">Updated 2025-03-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.21958">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.21958.pdf">PDF</a>
          <a class="chip" href="https://github.com/kibonku/Stationary3DApp">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.21958.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Refined Geometry-guided Head Avatar Reconstruction from Monocular RGB Video</span>
        <span class="paper-authors">Pilseo Park et.al.</span>
        <span class="paper-meta">Updated 2025-03-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.21886">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.21886.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.21886.pdf">
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
        <span class="paper-title">RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting</span>
        <span class="paper-authors">Qiyu Dai et.al.</span>
        <span class="paper-meta">Updated 2025-03-27</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.21442">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.21442.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.21442.pdf">
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
        <span class="paper-title">AccidentSim: Generating Physically Realistic Vehicle Collision Videos from Real-World Accident Reports</span>
        <span class="paper-authors">Xiangwen Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-03-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.20654">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.20654.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.20654.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">EVolSplat: Efficient Volume-based Gaussian Splatting for Urban View Synthesis</span>
        <span class="paper-authors">Sheng Miao et.al.</span>
        <span class="paper-meta">Updated 2025-03-26</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.20168">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.20168.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.20168.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">CoMapGS: Covisibility Map-based Gaussian Splatting for Sparse Novel View Synthesis</span>
        <span class="paper-authors">Youngkyoon Jang et.al.</span>
        <span class="paper-meta">Updated 2025-03-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.20998">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.20998.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.20998.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Learning Scene-Level Signed Directional Distance Function with Ellipsoidal Priors and Neural Residuals</span>
        <span class="paper-authors">Zhirui Dai et.al.</span>
        <span class="paper-meta">Updated 2025-03-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.20066">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.20066.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.20066.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MultimodalStudio: A Heterogeneous Sensor Dataset and Framework for Neural Rendering across Multiple Imaging Modalities</span>
        <span class="paper-authors">Federico Lincetto et.al.</span>
        <span class="paper-meta">Updated 2025-03-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.19673">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.19673.pdf">PDF</a>
          <a class="chip" href="https://github.com/LTTM/MultimodalStudio">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.19673.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">LookCloser: Frequency-aware Radiance Field for Tiny-Detail Scene</span>
        <span class="paper-authors">Xiaoyu Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-03-25</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.18513">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.18513.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.18513.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">NexusGS: Sparse View Synthesis with Epipolar Depth Priors in 3D Gaussian Splatting</span>
        <span class="paper-authors">Yulong Zheng et.al.</span>
        <span class="paper-meta">Updated 2025-03-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.18794">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.18794.pdf">PDF</a>
          <a class="chip" href="https://github.com/USMizuki/NexusGS">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.18794.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">NeRFPrior: Learning Neural Radiance Field as a Prior for Indoor Scene Reconstruction</span>
        <span class="paper-authors">Wenyuan Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-03-24</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.18361">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.18361.pdf">PDF</a>
          <a class="chip" href="https://github.com/wen-yuan-zhang/NeRFPrior">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.18361.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">End-to-End Implicit Neural Representations for Classification</span>
        <span class="paper-authors">Alexander Gielisse et.al.</span>
        <span class="paper-meta">Updated 2025-03-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.18123">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.18123.pdf">PDF</a>
          <a class="chip" href="https://github.com/sandergielisse/mwt">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.18123.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Unraveling the Effects of Synthetic Data on End-to-End Autonomous Driving</span>
        <span class="paper-authors">Junhao Ge et.al.</span>
        <span class="paper-meta">Updated 2025-03-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.18108">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.18108.pdf">PDF</a>
          <a class="chip" href="https://github.com/cancaries/SceneCrafter">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.18108.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">PanopticSplatting: End-to-End Panoptic Gaussian Splatting</span>
        <span class="paper-authors">Yuxuan Xie et.al.</span>
        <span class="paper-meta">Updated 2025-03-23</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.18073">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.18073.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.18073.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Splat-LOAM: Gaussian Splatting LiDAR Odometry and Mapping</span>
        <span class="paper-authors">Emanuele Giacomini et.al.</span>
        <span class="paper-meta">Updated 2025-03-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.17491">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.17491.pdf">PDF</a>
          <a class="chip" href="https://github.com/rvp-group/Splat-LOAM">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.17491.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FFaceNeRF: Few-shot Face Editing in Neural Radiance Fields</span>
        <span class="paper-authors">Kwan Yun et.al.</span>
        <span class="paper-meta">Updated 2025-03-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.17095">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.17095.pdf">PDF</a>
          <a class="chip" href="https://github.com/kwanyun/FFaceNeRF">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.17095.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DroneSplat: 3D Gaussian Splatting for Robust 3D Reconstruction from In-the-Wild Drone Imagery</span>
        <span class="paper-authors">Jiadong Tang et.al.</span>
        <span class="paper-meta">Updated 2025-03-21</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.16964">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.16964.pdf">PDF</a>
          <a class="chip" href="https://github.com/BITyia/DroneSplat">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.16964.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Digitally Prototype Your Eye Tracker: Simulating Hardware Performance using 3D Synthetic Data</span>
        <span class="paper-authors">Esther Y. H. Lin et.al.</span>
        <span class="paper-meta">Updated 2025-03-20</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.16742">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.16742.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.16742.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GO-N3RDet: Geometry Optimized NeRF-enhanced 3D Object Detector</span>
        <span class="paper-authors">Zechuan Li et.al.</span>
        <span class="paper-meta">Updated 2025-03-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.15211">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.15211.pdf">PDF</a>
          <a class="chip" href="https://github.com/ZechuanLi/GO-N3RDet">Code</a>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.15211.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">MultiBARF: Integrating Imagery of Different Wavelength Regions by Using Neural Radiance Fields</span>
        <span class="paper-authors">Kana Kurata et.al.</span>
        <span class="paper-meta">Updated 2025-03-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.15070">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.15070.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.15070.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">3D Engine-ready Photorealistic Avatars via Dynamic Textures</span>
        <span class="paper-authors">Yifan Wang et.al.</span>
        <span class="paper-meta">Updated 2025-03-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.14943">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.14943.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.14943.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">ClimateGS: Real-Time Climate Simulation with 3D Gaussian Style Transfer</span>
        <span class="paper-authors">Yuezhen Xie et.al.</span>
        <span class="paper-meta">Updated 2025-03-19</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.14845">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.14845.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.14845.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Segmentation-Guided Neural Radiance Fields for Novel Street View Synthesis</span>
        <span class="paper-authors">Yizhou Li et.al.</span>
        <span class="paper-meta">Updated 2025-03-18</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.14219">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.14219.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.14219.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
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
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">TriDF: Triplane-Accelerated Density Fields for Few-Shot Remote Sensing Novel View Synthesis</span>
        <span class="paper-authors">Jiaming Kang et.al.</span>
        <span class="paper-meta">Updated 2025-03-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.13347">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.13347.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.13347.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DeGauss: Dynamic-Static Decomposition with Gaussian Splatting for Distractor-free 3D Reconstruction</span>
        <span class="paper-authors">Rui Wang et.al.</span>
        <span class="paper-meta">Updated 2025-03-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.13176">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.13176.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.13176.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">DivCon-NeRF: Generating Augmented Rays with Diversity and Consistency for Few-shot View Synthesis</span>
        <span class="paper-authors">Ingyun Lee et.al.</span>
        <span class="paper-meta">Updated 2025-03-17</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.12947">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.12947.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.12947.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">FA-BARF: Frequency Adapted Bundle-Adjusting Neural Radiance Fields</span>
        <span class="paper-authors">Rui Qian et.al.</span>
        <span class="paper-meta">Updated 2025-03-15</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.12086">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.12086.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.12086.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Flow-NeRF: Joint Learning of Geometry, Poses, and Dense Flow within Unified Neural Representations</span>
        <span class="paper-authors">Xunzhi Zheng et.al.</span>
        <span class="paper-meta">Updated 2025-03-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.10464">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.10464.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.10464.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">AI-assisted 3D Preservation and Reconstruction of Temple Arts</span>
        <span class="paper-authors">Naai-Jung Shih et.al.</span>
        <span class="paper-meta">Updated 2025-03-13</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.10031">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.10031.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.10031.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Hybrid Rendering for Multimodal Autonomous Driving: Merging Neural and Physics-Based Simulation</span>
        <span class="paper-authors">Máté Tóth et.al.</span>
        <span class="paper-meta">Updated 2025-03-12</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.09464">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.09464.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.09464.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">GAS-NeRF: Geometry-Aware Stylization of Dynamic Radiance Fields</span>
        <span class="paper-authors">Nhat Phuong Anh Vu et.al.</span>
        <span class="paper-meta">Updated 2025-03-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.08483">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.08483.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.08483.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Uni-Gaussians: Unifying Camera and Lidar Simulation with Gaussians for Dynamic Driving Scenarios</span>
        <span class="paper-authors">Zikang Yuan et.al.</span>
        <span class="paper-meta">Updated 2025-03-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.08317">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.08317.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.08317.pdf">
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
        <span class="paper-title">NeRF-VIO: Map-Based Visual-Inertial Odometry with Initialization Leveraging Neural Radiance Fields</span>
        <span class="paper-authors">Yanyu Zhang et.al.</span>
        <span class="paper-meta">Updated 2025-03-11</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.07952">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.07952.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.07952.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Neural Radiance and Gaze Fields for Visual Attention Modeling in 3D Environments</span>
        <span class="paper-authors">Andrei Chubarau et.al.</span>
        <span class="paper-meta">Updated 2025-03-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.07828">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.07828.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.07828.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">CATPlan: Loss-based Collision Prediction in End-to-End Autonomous Driving</span>
        <span class="paper-authors">Ziliang Xiong et.al.</span>
        <span class="paper-meta">Updated 2025-03-10</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.07425">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.07425.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.07425.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
  <article class="paper-card">
    <details class="paper-details">
      <summary>
        <span class="paper-title">Feature-EndoGaussian: Feature Distilled Gaussian Splatting in Surgical Deformable Scene Reconstruction</span>
        <span class="paper-authors">Kai Li et.al.</span>
        <span class="paper-meta">Updated 2025-03-08</span>
      </summary>
      <div class="paper-body">
        <p class="paper-abstract">Abstract unavailable in cached data. It will appear after the next refresh.</p>
        <div class="paper-links">
          <a class="chip" href="https://arxiv.org/abs/2503.06161">arXiv</a>
          <a class="chip" href="https://arxiv.org/pdf/2503.06161.pdf">PDF</a>
          <span class="chip ghost">Code: N/A</span>
        </div>
        <div class="paper-preview" data-pdf="https://arxiv.org/pdf/2503.06161.pdf">
          <div class="preview-placeholder">Preview loads on expand</div>
          <canvas class="preview-canvas" aria-hidden="true"></canvas>
        </div>
      </div>
    </details>
  </article>
</section>
