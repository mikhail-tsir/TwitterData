import React from "react";

const Form = props => (
    <div>
        <form onSubmit={props.getWeather}>
            <input type="text" name="keyword" placeholder="Keyword..."/>
            <button>Analysis</button>
        </form>
    </div>
);




export default Form;