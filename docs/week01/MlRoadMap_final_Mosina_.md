---
title: MLRoadMap from Nastya 
---

<h1 id="machine-learning-roadmap">2020 Machine Learning Roadmap</h1>
<blockquote>
<p><strong>Check out:</strong><br>
<a href="https://whimsical.com/CA7f3ykvXpnJ9Az32vYXva">Mind map</a> (a lot of useful materials, links, articles, comments &amp; definitions)  + <a href="https://www.youtube.com/watch?v=pHiMN_gy9mk&amp;feature=youtu.be">Video ML</a></p>
<blockquote>
<p>Tasya’s advice:<br>
Interactive Machine Learning Roadmap (if u are not a fan of 2-hours and a half long videos - better search for needed info here). Honestly - everything u need now is to wonder this map. I tried to take some notes about basic structure of the map, but honestly - this map in the best conspect.</p>
</blockquote>
</blockquote>
<h3 id="intro">Intro</h3>
<p><em>Machine learning</em> is turning things (data) into numbers and <ins>finding patterns</ins> in those numbers.<br>
ML requires traditional programming to exist to be put to practice.</p>
<p>What ML is good for:</p>
<ul>
<li>Problems with long lists of rules</li>
<li>Continually changing enivonments</li>
<li>Discovering insights within large collections of data</li>
</ul>
<p><em>Machine learning (2.0) vs. traditional programming(1.0):</em><br>
2.0 needs 1.0, but 1.0 does not need 2.0.<br>
1.0 = input - instructions - ideal output<br>
2.0 = input - ideal output - instructions</p>
<p><em>And we need ML when…</em></p>
<ul>
<li>when we do not know all the RULES (instructions) and our task is to figure it out</li>
<li>when environments continually change</li>
<li>discover insights within large collections of data</li>
</ul>
<h3 id="ml-problems">ML Problems</h3>
<p>Categories of learning:</p>
<ul>
<li>Supervised Learning - data and labels. <em>The model tries to learn the relationship between data and labels</em>. For example, you have 10,000 photos of cats and dogs (5,000 each) and the labels for which photo contains which animal (photo 1% 3D dog. Photo 2 cat). Works for numbers too, for example, 10,000 houses and their selling price. Use the information about the houses to try and predict the selling price)<br>
-   <strong>Classification.</strong>  Assigns labels to data (e.g. labeling email as spam)<br>
- Binary classification<br>
- Multi-class classification<br>
- Multi-label classification<br>
-   <strong>Regression.</strong>  Predicts tendencies for data (e.g. price of real estate).<br>
-   <strong>Sequence to Sequence.</strong>  Transforms one kind of data into another (e.g. sound into text).</li>
<li>Unsupervised Learning - data and no labels. <em>The model tries to find patterns in data without something to reference on</em>. For example, you’ve got 50,000 transactions and 49,997 of them are similar but 3 of them are completely outlandish, which 3? This kind of problem is.called anomaly detection. Other common problems include clustering and dimensionality reduction (PCA).<br>
-  <strong>Clustering.</strong>  Groups data in clusters according to some similarities. Clusters can then be labeled.<br>
-   <strong>Dimensionality reduction.</strong>  Points out the meaningful parameters in data and discards the ‘noise’.</li>
<li>Transfer Learning - adjust knowledge from one model to work on another. For example, take all of the text from Wikipedia, learn the relationships between words and use these underlying relationships to help you build your insurance quote classifier.</li>
<li>Reinforcement Learning - reward or penalty. An agent (algorithm) performs actions in an environment and is rewarded or penalized based on the whether the actions were favorable or not. For example, the agent could be a ChessPlayerX (a chess playing algorithm), the environment is a virtual chessboard and the actions are moving pieces. If a piece gets moved to a negative position, the aglorithm gets renalized, if it takes an opponents piеce it gets rewarded. The strategy an agent learns (based on the actions it gets rewarded for) is called a policy.</li>
</ul>
<h3 id="ml-process">ML Process</h3>
<ul>
<li>Data collection
<ul>
<li>What data exists?</li>
<li>Privacy?</li>
<li>Structured?
<ul>
<li>nomial/caregorical</li>
<li>numerical</li>
<li>ordinal</li>
<li>time series</li>
</ul>
</li>
</ul>
</li>
<li>Data preparation (EDA, preprocessing, splitting)</li>
<li>Train model on data
<ul>
<li>Choose an algorithm</li>
<li>Type of learning:
<ul>
<li>batch learning</li>
<li>online learning</li>
<li>transfer learning</li>
<li>active learning</li>
<li>ensembling</li>
</ul>
</li>
<li>Underfitting</li>
<li>Overfitting</li>
<li>Reduce overfitting with regularization</li>
</ul>
</li>
<li>Analysis/Evaluation</li>
<li>Serve model (deploying a model)</li>
<li>Retrain the model</li>
</ul>
<h3 id="ml-tools">ML Tools</h3>

<table>
<thead>
<tr>
<th>Libraries/code space</th>
<th>Experiment tracking</th>
<th>Pre-trained models</th>
<th>Data &amp; model tracking</th>
<th>Cloud compute service</th>
<th>Hardware</th>
<th>AutoML &amp; hyperparameter tuning</th>
<th>Explainability</th>
<th>ML Lifecycle</th>
<th>UI</th>
</tr>
</thead>
<tbody>
<tr>
<td>jupyter, tensorflow.js, pytorch, onnx, xgboost</td>
<td><a href="http://neptune.ai">neptune.ai</a>, dashboard by weights &amp; biases, tensorboard</td>
<td>detection2, tensorflow hub, pytorch hub, <ins>hugging face transformers</ins></td>
<td>artifacts by weights &amp; biases, data version control</td>
<td>aws, ms azure, colab, google cloud</td>
<td></td>
<td>sweeps by weights &amp; biases, google cloud automl, tpot, ms azure automl</td>
<td>shap</td>
<td>kubeflow, mlflow, seldon</td>
<td>streamlit</td>
</tr>
</tbody>
</table><h3 id="ml-mathematics">ML Mathematics</h3>
<ul>
<li>Linear Algebra</li>
<li>Matrix Manipulation</li>
<li>Multivariate Calculus</li>
<li>The Chain Rule</li>
<li>Probability + Distributions</li>
<li>Optimization</li>
</ul>

