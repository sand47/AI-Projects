# GAN

This blog post on GANs gives overview of some associated papers.

Generative adversarial networks (GANs) are one of the hottest topics in deep learning. From a high level, GANs are composed of two components, a generator and a discriminator. The discriminator has the task of determining whether a given image looks natural (ie, is an image from the dataset) or looks like it has been artificially created. The task of the generator is to create natural looking images that are similar to the original data distribution, images that look natural enough to fool the discriminator network.

The analogy used in the paper is that the generative model is like “a team of counterfeiters, trying to produce and use fake currency” while the discriminative model is like “the police, trying to detect the counterfeit currency”. The generator is trying to fool the discriminator while the discriminator is trying to not get fooled by the generator.

As the models train through alternating optimization, both methods are improved until a point where the “counterfeits are indistinguishable from the genuine articles”.

The tutorial is written in Python, with the Tensorflow library, so it would be good to have familiarity with Tensorflow before taking a look at this tutorial.

# How to Use Jupyter Notebooks

1. First step is always to clone the repository.
```
git clone https://github.com/sand47/Machine-learning-and-deep-learning-/tree/master/Deep-learning/Unsupervised/GAN
```
2.Next, we want to make sure we have Jupyter Notebook installed. You can either follow one of two paths. You can either install Anaconda (which installs Python, Jupyter Notebook, and a bunch of other useful computing libraries) or use pip.
To install Anaconda, take a look at their website, which has some pretty great documentation.

If you want to install using pip, you'll need to update pip with the following code (Replace pip with pip3 if using Python 3).

On Linux/Mac OS:
```
pip install -U pip setuptools
```
On Windows:
```
python -m pip install -U pip setuptools
```
Next, you should be able to run the following.
```
pip install jupyter
```
Finally, run the following command and a new tab in your browser with the Jupyter Notebook should come up
jupyter notebook

#More GAN Resources
-The original [paper](https://arxiv.org/pdf/1406.2661.pdf) written by Ian Goodfellow in 2014.
- Siraj Raval's [video](https://www.youtube.com/watch?v=deyOX6Mt_As) tutorial on GANs (Really fun video)
- Ian Godfellow's [keynote](https://channel9.msdn.com/Events/Neural-Information-Processing-Systems-Conference/Neural-Information-Processing-Systems-Conference-NIPS-2016/Generative-Adversarial-Networks) on GANs (More of a technical video)
- Brandon Amos's image completion [blog](https://bamos.github.io/2016/08/09/deep-completion/) post
- [Blog](https://medium.com/@ageitgey/abusing-generative-adversarial-networks-to-make-8-bit-pixel-art-e45d9b96cee7) post on using GANs in video games.
- Andrej Karpathy's [blog](https://cs.stanford.edu/people/karpathy/gan/) post with GAN visualizations.

