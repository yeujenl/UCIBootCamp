# Module 21 Deep Learning Challenge

I did not cooperate with other students and no codes were sourced from outside of class material.</br>

</b>Overview of the analysis:</b> To create a binary classifier that can predict whether applicants will be successful if funded by Alphabet Soup and determine if we are succesful with our model.</br>

<b>Results:</b></br>
Data Processing
<ul>
<li><b>What variable(s) are the target(s) for your model?</b></br>
    The target of the model is the "Is Successful" column, as we are trying to determine if the organization is successful after receiving the funding.</li>
<li><b>What variable(s) are the features for your model?</b></br>
    The features of the model are application type, affiliated sector of industry, government organization classification, use case of funding, organization type, the active status of the organization, income classification, special considerations of application and the funding amount requested.</li>
<li><b>What variable(s) should be removed from the input data because they are neither targets nor features?</b></br>
    The EIN and Name of the organization as they have no bearing on the analysis.</li>
</ul>

<u>Compiling, Training, and Evaluating the Model</u>
<ul>
<li><b>How many neurons, layers, and activation functions did you select for your neural network model, and why?</b></br>
    I ended up choosing 2 layers, 3 neuron in first layer and 5 neurons in the second layer, as this was the optimial model parameters using keras_tuner. I also ran the tuner with 5 layers and the accuracy was also 73% and thus I utilized the result of the 3 layer tuner.</li>
<li><b>Were you able to achieve the target model performance?</b></br>
    No, it appears the model accuracy is limited to 72% and 55% loss, thus we are unable to achieve a 75% accuracy.</li>
<li><b>What steps did you take in your attempts to increase model performance?</b></br>
    Used keras tuner with 2 layers, 3 layers and 5 layers input to determine the best parameters.</li>
</ul>
</br>
<b>Summary:</b></br> Overall the model is able to achieve a 72% accuracy with a 55% data loss. The initial data has a lot of categorical data, and thus may have limited the performance of the model. I would recommend trying random forest with the data as we would not need to bin and convert categorical data to dummies and may preserve more data integrity.