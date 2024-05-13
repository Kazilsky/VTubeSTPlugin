const { createCompletion, loadModel } = require('gpt4all')

const model = loadModel('ggml-vicuna-7b-1.1-q4_2', { verbose: true });

const response = createCompletion(model, [
    { role : 'system', content: 'You are meant to be annoying and unhelpful.'  },
    { role : 'user', content: 'What is 1 + 1?'  } 
]);
console.log(response);