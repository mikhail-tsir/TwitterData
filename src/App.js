import React from "react";

import Titles from "./components/Titles";
import Form from "./components/Form";
import Weather from "./components/Weather"





class App extends React.Component{
    state = {
        sentiment_avg: undefined,
        pos: undefined,
        neg: undefined,
        error: undefined
    }

    // links here
    getWeather = async(e) => {
        e.preventDefault();
        //keyword constant, use this
        const word = e.target.elements.keyword.value;
        //the following three lines should be to get POST request 
        let xhttp = new XMLHttpRequest();
        xhttp.open("GET", "http://127.0.0.1:8080/twitterkeyword?"+"keyword="+word, false);
        xhttp.send(word);
        var bob = JSON.parse(xhttp.responseText);

        if (word) {
            
            this.setState({
                sentiment_avg: bob.avg_sentiment,
                pos: bob.pos_keywords.join(", "),
                neg: bob.neg_keywords.join(", "),
                error: ""
            });
        } else {
            this.setState({
                sentiment_avg: undefined,
                pos: undefined,
                neg: undefined,
                error: "Please enter a keyword."
            });
        }
    }
    render(){
        return(
            <div>
                <div className="back">
                    <div className="main">
                        <div className="container">
                            <div className="row">
                                <div className="col-xs-7 form-box">
                                    <Form getWeather={this.getWeather}/>
                                    <Weather 
                                        sentiment_avg={this.state.sentiment_avg}
                                        pos={this.state.pos}
                                        neg={this.state.neg}
                                        error={this.state.error}
                                    />
                                </div>
                                <div className="col-xs-5 title-box">
                                    <Titles />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
};

export default App;