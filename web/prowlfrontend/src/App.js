// App.js
import React, { Component } from 'react';

class App extends Component {
  state = {
    courses: [],
    counter: 0
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://0.0.0.0:8000/api/v1/courses/');
      const courses = await res.json();
      this.setState({
        courses
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {

    let tigerStripeStyle = {
          backgroundColor: "#f2f2f2"
    }

    return (
      <div>
        {this.state.courses.map((item, i) => (
          <div
            style={(Object.assign({},
              i % 2 && tigerStripeStyle
            ))}
            key={item.id}>
              <h1>
              {item.title}
              </h1>
          </div>
        ))}
      </div>
    );
  }
}

export default App;
