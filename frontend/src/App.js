import './App.css';
import React from 'react';
function App() {

  const [name,setName] = React.useState("");
  const [power,setPower] = React.useState("");
  const [result,setResult] = React.useState("");
  const [file,setFile] = React.useState("");
  
  function handleUpload(event){
    setFile(event.target.files[0]);
  }
  async function submit(e) {
    
    setResult("abc");

    const data = new FormData();
    data.append('name', name);
    data.append('power', power);
    data.append('file', file);
  

    await fetch('http://localhost:5000/calculate',{
      method : 'POST',
      body: data
    })
    .then((response)=>{response.json().then(data =>{
      setResult(data.result);
    })})

    //alert(state);
    
    
    
}


  return (
    <div className="App">
      

    <div>
      <label for="pame">Name:-</label><br></br>
      <input name="name" value={name}  onChange={(e) => setName(e.target.value)} type="text" placeholder="0-120(Required)" />
    </div>
    <div>
      <label for="power">Power:-</label><br></br>
      <input name="power" value={power}  onChange={(e) => setPower(e.target.value)} type="text" placeholder="0-120(Required)" />
    </div>
    <div>
      <button onClick={submit} className="btn">Calculate</button>

   </div>
   <div id="upload-box">
   <label for="file-upload" class="custom-file-upload">
       Upload Here
   </label>
   <input id="file-upload" type="file" onChange={handleUpload}/>
   
   </div>
    
    <div>{result}</div>
    </div>
  );
}

export default App;
