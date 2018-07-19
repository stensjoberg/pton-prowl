import React, { Component } from 'react'
import Radium from 'radium'
import { getCourse, getUser } from './helper'
import NavBar from './NavBar'
import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';

class CourseDetail extends Component {

    state = {
        course: {},
        user: {}
    }

    async componentDidMount() {
        const id = this.props.match.params.courseId
        const course = await getCourse({id: id})
        const user = await getUser()
        this.setState({
            course,
            user
        })
    }

    async componentDidUpdate(prevProps) {
        if ((prevProps.match.params.courseId === undefined && this.props.match.params.courseId !== undefined) ||
            (prevProps.match.params.courseId !== this.props.match.params.courseId)) {
            const id = this.props.match.params.courseId
            const course = await getCourse({id: id})
            this.setState({
                course
            })
        }
    }

    render() {
        const course = this.state.course
        if (course.codes === undefined) {
            return false
        }
        if (course.groups == undefined) {
            return false
        }
        else {
            console.log(course)
            return (
                <div>
                    <NavBar user={this.state.user} history={this.props.history}/>
                    <div className="flexcontainer vert top" >
                        <h1>{course.title}</h1>
                        <ul>
                        {course.codes.map((code) => (
                            <li key={code.id}>{code.id}</li>
                        ))}
                        </ul>

                        <h2>Groups</h2>
                        <ul>
                        {course.groups.map((group) => (
                            <li key={group.id}>{group.id}</li>
                        ))}
                        </ul>
                    </div>
                </div>
            );
        }
    }
}

export default Radium(CourseDetail)
