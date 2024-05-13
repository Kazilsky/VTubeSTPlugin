const vts = require('vtubestudio')
const fs = require('fs')
const WebSocket = require('ws')

const apiClient = new vts.ApiClient({
    pluginName: 'VTubeTestEmulate',
    pluginDeveloper: 'by: Kazilsky',

    authTokenGetter: () => fs.readFileSync('./auth-token.txt', 'utf-8'),
    authTokenSetter: (authenticationToken) => fs.writeFileSync('./auth-token.txt', authenticationToken, { encoding: 'utf-8' }),
    webSocketFactory: url => new WebSocket(url),
})

apiClient.on('connect', async () => {
    const stats = await apiClient.statistics()
    apiClient.apiState();
    // console.log(apiClient.hotkeyTrigger());
    lp1 = await apiClient.currentModel();
    console.log(lp1);
    lp2 = await apiClient.hotkeysInCurrentModel();
    console.log(lp2);
    await apiClient.hotkeyTrigger('c7695e263334443282c7ec92b5f47d88', '6d6fc4a61c0d48f59d6c8f6cdaa68d10')



    console.log(`Connected to VTube Studio v${stats.vTubeStudioVersion}`)
    
    console.log('Getting list of available models')
    const { availableModels } = await apiClient.availableModels()
    console.log('Available Models: ' + availableModels.modelName);

    console.log('Adding event callback whenever a model is loaded')
    await apiClient.events.modelLoaded.subscribe((data) => {
        if (data.modelLoaded) {
            console.log('Model loaded, queuing up a random model switch')
            setTimeout(async () => {
                console.log('Switching to random model')
                const otherModels = availableModels.filter(m => m.modelID !== data.modelID)
                const randomModel = otherModels[Math.floor(otherModels.length * Math.random())]
                console.log('Switching to ' + randomModel.modelName)
                await apiClient.modelLoad({ modelID: randomModel.modelID })
            }, 3000)
        }
    })
})