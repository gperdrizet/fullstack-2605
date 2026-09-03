# GitHub repositories

You can find all of my public GitHub content here: [gperdrizet](https://github.com/gperdrizet).


## Unit 2: Data science fundamentals

<table>
  <thead>
    <tr><th>Lesson</th><th>Topic</th><th>Description</th><th>Repo</th></tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="1" style="vertical-align:top">Lesson 16</td>
      <td>Feature engineering</td>
      <td>Instructor solution for feature engineering challenge</td>
      <td><a href="https://github.com/gperdrizet/featurely" target="_blank">gperdrizet/featurely</a></td>
    </tr>
  </tbody>
</table>


## Unit 3: Machine learning

<table>
  <thead>
    <tr><th>Lesson</th><th>Topic</th><th>Description</th><th>Repo</th></tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="1" style="vertical-align:top">Lesson 19</td>
      <td>Supervised learning, regression</td>
      <td>Deployed web app for predicting concrete compressive strength from composition and age</td>
      <td><a href="https://github.com/gperdrizet/concrete-strength" target="_blank">gperdrizet/concrete-strength</a></td>
    </tr>
    <tr>
      <td rowspan="1" style="vertical-align:top">Lesson 20</td>
      <td>Supervised learning, classification</td>
      <td>Kaggle student health risk competition submission</td>
      <td><a href="https://github.com/gperdrizet/student-health-risk" target="_blank">gperdrizet/student-health-risk</a></td>
    </tr>
    <tr>
      <td rowspan="1" style="vertical-align:top">Lesson 23</td>
      <td>Recommendation systems, collaborative, content and hybrid filtering</td>
      <td>Deployed hybrid filtering movie recommendation app using the Movie Lens 100k dataset</td>
      <td><a href="https://github.com/gperdrizet/movie-lens-recommendations" target="_blank">gperdrizet/movie-lens-recommendations</a></td>
    </tr>
  </tbody>
</table>

## Unit 4: Deeplearning

<table>
  <thead>
    <tr><th>Lesson</th><th>Topic</th><th>Description</th><th>Repo</th></tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="1" style="vertical-align:top">Lesson 28</td>
      <td>PyTorch</td>
      <td>Demo & activity notebooks for PyTorch regression and image classification</td>
      <td><a href="https://github.com/gperdrizet/pytorch-demo" target="_blank">gperdrizet/pytorch-demo</a></td>
    </tr>
    <tr>
      <td rowspan="1" style="vertical-align:top">Lesson 29-33</td>
      <td>Image classification</td>
      <td>RSNA knee abnormality Kaggle competition solution: multiclass image classification</td>
      <td><a href="https://github.com/gperdrizet/RSNA-knee-abnormality" target="_blank">gperdrizet/RSNA-knee-abnormality</a></td>
    </tr>
    <tr>
      <td rowspan="1" style="vertical-align:top">Lesson 29-33</td>
      <td>Image classification</td>
      <td>CIFAR10 model training and optimization, image classification tools package</td>
      <td><a href="https://github.com/gperdrizet/CIFAR10" target="_blank">gperdrizet/CIFAR10</a></td>
    </tr>
  </tbody>
</table>

## DevOps/other

<table>
  <thead>
    <tr><th>Purpose</th><th>Description</th><th>Repo</th></tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="5" style="vertical-align:top">Containerized development environments</td>
      <td>General purpose data science</td>
      <td><a href="https://github.com/gperdrizet/datascience-devcontainer" target="_blank">gperdrizet/datascience-devcontainer</a></td>
    </tr>
    <tr>
      <td>Kaggle competitions</td>
      <td><a href="https://github.com/gperdrizet/kaggle-devcontainer" target="_blank">gperdrizet/kaggle-devcontainer</a></td>
    </tr>
    <tr>
      <td>Deeplearning & neural network development</td>
      <td><a href="https://github.com/gperdrizet/deeplearning-devcontainer" target="_blank">gperdrizet/deeplearning-devcontainer</a></td>
    </tr>
    <tr>
      <td>LLM hosting & application development</td>
      <td><a href="https://github.com/gperdrizet/llms-devcontainer" target="_blank">gperdrizet/llms-devcontainer</a></td>
    </tr>
    <tr>
      <td>Master repo for base Docker images</td>
      <td><a href="https://github.com/gperdrizet/docker-images" target="_blank">gperdrizet/docker-images</a></td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <td rowspan="3" style="vertical-align:top">Learning tools & course resources</td>
      <td>This GitHub pages site source</td>
      <td><a href="https://github.com/gperdrizet/fullstack-2605" target="_blank">gperdrizet/fullstack-2605</a></td>
    </tr>
    <tr>
      <td>Bug Hunter basic Python practice app </td>
      <td><a href="https://github.com/gperdrizet/bug-hunter" target="_blank">gperdrizet/bug-hunter</a></td>
    </tr>
    <tr>
      <td>Kaggle style leaderboard for feature engineering competition</td>
      <td><a href="https://github.com/gperdrizet/leaderboard" target="_blank">gperdrizet/leaderboard</a></td>
    </tr>
  </tbody>
</table>


## How to use GitHub repos

First, make a fork of the repo: click the 'fork' button in the upper right on the repository main page. Set yourself as the owner and click create. This gives you a copy of the original repository that you can make changes to. Then, to run the code or make changes you can work in a GitHub codespace, or clone your fork to work locally.


### GitHub codespaces

From your fork's main page on GitHub, click the green 'Code' dropdown button at the upper right of the file list, switch to the 'Codespaces' tab of the menu and click 'Create codespace on main'. This will spin up a containerized development environment and show you a clone of the repo via VS code running on a GiHub server.

Codespaces are best when the repo is configured with a `.devcontainer/devcontainer.json` file, meaning the developer set things to up to work well in VS Code via Microsoft's devcontainers extension (what codespaces use...), but it is possible to interact with any repo this way.


### Clone

You can also clone the repository locally or to another cloud development environment provider (like Vocareum). After you have made your fork, do the following:

1. Click the green 'Code' button at the upper right above the file list on the repo's GitHub page
2. Make sure you are on the 'Local' tab
3. Copy the URL shown under 'Clone'
4. Then clone the repo on whatever machine you are using with:

```
git clone git@github.com:USERNAME/REPONAME.git
```

Now you should have a local directory called `REPONAME/` with the repository's contents.

It is possible to clone a public GitHub repository that you don't own, but you will not be able to push changes back to GitHub. It's best to use a fork - even if you want to contribute to a project by adding/editing code to the original repo. This is usually done via pull request, but check the specific project's documentation to see what their preferred collaboration workflow is.