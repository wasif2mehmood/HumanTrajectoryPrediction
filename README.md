## Human Trajectory Prediction

Human trajectory prediction is a critical task in many applications such as autonomous driving, surveillance, and robotics. The goal is to predict the future locations of pedestrians based on their past movements.

Our method, SimAug, leverages robust representations learned from simulation data to improve the performance of trajectory prediction models. We use a two-stage training process. In the first stage, we train our model on a large amount of simulated data. In the second stage, we fine-tune the model on a small amount of real-world data.

SimAug addresses the domain gap between simulation and real-world data, which is a common challenge in learning from simulation. By learning robust representations from simulation, our model is able to generalize well to real-world data.

For more details about our method and its performance, please refer to our [paper](https://arxiv.org/abs/2004.02022).
This repository contains the code and models for the following ECCV'20 paper:

**[SimAug: Learning Robust Representations from Simulation for Trajectory Prediction](https://arxiv.org/abs/2004.02022)** \
[Junwei Liang](https://www.cs.cmu.edu/~junweil/),
[Lu Jiang](http://www.lujiang.info/),
[Alexander Hauptmann](https://www.cs.cmu.edu/~alex/)

You can find more information at our [Project Page](https://precognition.team/next/simaug/).

## Dataset and Testing

For testing, you can download the dataset from [here](https://www.kaggle.com/datasets/aryashah2k/stanford-drone-dataset).

To test on a video, place the video file in the `video` directory and the corresponding `annotations.txt` file in the `annotations` directory.

After setting up the dataset and video, you can start testing and visualizing the multi-future trajectory of people by running the following command:

```bash
bash test.sh
```
The output videos and frames will be stored in the vis_heatmap directory. Please ensure that you have correctly installed all the necessary dependencies and followed the setup instructions before running the test script.


If you find this code useful in your research then please cite

```
@inproceedings{liang2020simaug,
  title={SimAug: Learning Robust Representations from Simulation for Trajectory Prediction},
  author={Liang, Junwei and Jiang, Lu and Hauptmann, Alexander},
  booktitle={Proceedings of the European Conference on Computer Vision (ECCV)},
  month = {August},
  year={2020}
}
```
