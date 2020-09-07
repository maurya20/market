import React from 'react';
import './Home.css'


class Home extends React.Component {
   constructor(props) {
      super(props);
      this.state = {
        data: [],
        loaded: false,
        placeholder: "Loading",
      };
    }
  
    componentDidMount() {
      fetch("http://127.0.0.1:8000/mapi")
        .then((response) => {
          if (response.status > 400) {
            return this.setState(() => {
              return { placeholder: "Something went wrong!" };
            });
          }
          return response.json();
        })
        .then((data) => {
          this.setState(() => {
            return {
              data,
              loaded: true,
            };
          });
        });
    }
  
    render() {
      return (
          <div className="container">
        <div className="row">
          {this.state.data.map((contact) => {
            return (
              <div className="col-md-4">
                <div className="thumbnail">
                  <img src={contact.pic} alt="Nature" style={{width:"100%"}}></img>
                  <div className="caption">
                    <p style={{color:"black"}}>{contact.heading}</p>
                    <p>Published on: {contact.date} </p>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
        </div>
      );
    }
  }
 export default Home;
 
 