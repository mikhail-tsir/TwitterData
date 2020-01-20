import React from "react";
import Logo from "./real.png";

const Titles = () => (
    <div>
        <div>
            <h1 className="main_title">tweet<span className="black">Back</span></h1>
            <img src={Logo} alt="Logo" height="300" width="320"></img>
        </div>
        <br></br>
        <br></br>
        <br></br>
        <p className="sub_title">An app that employs sentiment analysis to give you twitter's opinion on a topic.</p>
    </div>
);

export default Titles;