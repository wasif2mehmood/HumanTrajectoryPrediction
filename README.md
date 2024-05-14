# SimAug

This repository contains the code and models for the following ECCV'20 paper:

**[SimAug: Learning Robust Representations from Simulation for Trajectory Prediction](https://arxiv.org/abs/2004.02022)** \
[Junwei Liang](https://www.cs.cmu.edu/~junweil/),
[Lu Jiang](http://www.lujiang.info/),
[Alexander Hauptmann](https://www.cs.cmu.edu/~alex/)

You can find more information at our [Project Page](https://precognition.team/next/simaug/).

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

## Dataset and Testing

For testing, you can download the dataset from [here](https://www.kaggle.com/datasets/aryashah2k/stanford-drone-dataset).

To test on a video, place the video file in the `video` directory and the corresponding `annotations.txt` file in the `annotations` directory.

After setting up the dataset and video, you can start testing and visualizing the multi-future trajectory of people by running the following command:

```bash
bash test.sh
```
The output videos and frames will be stored in the vis_heatmap directory. Please ensure that you have correctly installed all the necessary dependencies and followed the setup instructions before running the test script.

