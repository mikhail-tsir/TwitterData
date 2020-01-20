import React from "react";

//postToFlask = async(e) => {
 //   let xhttp = new XMLHttpRequest();

//}

const Form = props => (
    <div>
        <form method="POST" onSubmit={props.getWeather}>
            <input type="text" name="keyword" placeholder="Keyword..."/>
            <button /*onclick = {postToFlask}*/>Analysis</button>
        </form>
    </div>
);




export default Form;