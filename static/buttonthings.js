navigator.mediaDevices.getUserMedia({audio:true})
      .then(stream => {handlerFunction(stream)})


            function handlerFunction(stream) {
            rec = new MediaRecorder(stream);
            rec.ondataavailable = e => {
              audioChunks.push(e.data);
              if (rec.state == "inactive"){
                let blob = new Blob(audioChunks,{type:'audio/mp3'});
                recordedAudio.src = URL.createObjectURL(blob);
                recordedAudio.controls=true;
                
                sendData(blob)
              }
            }
          }
                function sendData(data) {}

        record.onclick = e => {
          console.log('I was clicked')
          record.disabled = true;
          record.style.backgroundColor = "blue"
          stopRecord.disabled=false;
          audioChunks = [];
          rec.start();
        }
        stopRecord.onclick = e => {
          console.log("I was clicked")
          record.disabled = false;
          stop.disabled=true;
          record.style.backgroundColor = "red"
          rec.stop();
        }

        // var ffmpeg = require('ffmpeg');
        // try{
        //   car process = new ffmpeg(recordedAudio)
        //   process.then(function(audio){
        //     audio.fxExtractSountToMP3('recording.mp3', function (error, file){
        //       if (!error)
        //         console.log('Audio file: ' + file);
        //     });
        //   }, function (err){
        //     console.log('Error: ' + err);
          
        //   });
        // }
        // catch(e){
        //   console.log(e.code);
        //   console.log(e.msg);
        // }






