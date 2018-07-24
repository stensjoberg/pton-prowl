import React, { Component } from 'react'
import { Link } from 'react-router-dom'
import Radium from 'radium'
import Helmet from 'react-helmet';
import { getCourse, getUser, getGroupsFromLinks } from './helper'
import NavBar from './NavBar'
import GroupItem from './GroupItem'
import Availability from './Availability'
import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';

const ENROLL = true
const UNENROLL = false

class CourseDetail extends Component {

    state = {
        course: {},
        user: {},
        searchString: '',
        availGroups: [],
        filteredAvailGroups: [],
        enrolledGroups: []
    }

    handleSearch = async (value) => {
        console.log("handling search...")
        const searchString = value.toLowerCase()
        let filteredAvailGroups = this.state.availGroups
        filteredAvailGroups = this.state.availGroups.filter(elem =>
            elem.id.toString().search(
                searchString) !== -1
        )
        console.log(searchString)
        this.setState({
            searchString,
            filteredAvailGroups
        })
    }

    handleChange = async (id, change) => {
        let availGroups = this.state.availGroups
        let enrolledGroups = this.state.enrolledGroups
        if(change === ENROLL) {
            enrolledGroups.unshift(availGroups.find(elem => elem.id === id))
            availGroups = availGroups.filter(elem => elem.id !== id)
        }
        else { // change is UNENROLL
            availGroups.unshift(enrolledGroups.find(elem => elem.id === id))
            enrolledGroups = enrolledGroups.filter(elem => elem.id !== id)
        }

        await this.setState({
            availGroups,
            enrolledGroups
        })

        this.handleSearch(this.state.searchString)

    }

    async componentDidMount() {
        const id = this.props.match.params.courseId
        const course = await getCourse({id: id})
        const user = await getUser()
        const userEnrolledGroups = await getGroupsFromLinks(user.groups)
        console.log(userEnrolledGroups)
        let enrolledGroups = []
        userEnrolledGroups.map((userGroup) => {
            if (userGroup.course === course.url) {
                enrolledGroups.push(userGroup)
            }
        })

        let availGroups = []
        course.groups.map((group) => {
            if (!enrolledGroups.some(eg => eg.id === group.id)) {
                availGroups.push(group)
            }
        })

        this.setState({
            course,
            user,
            availGroups,
            enrolledGroups,
            filteredAvailGroups: availGroups
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
            console.log(this.state.availGroups)
            console.log(this.state.filteredAvailGroups)
            console.log(this.state.enrolledGroups)
            return (
                <div>
                  <Helmet bodyAttributes={{style: 'background-color : #EAEAEA'}}/>
                    <NavBar user={this.state.user} history={this.props.history}/>
                    <div className="flexcontainer hor top">
                    <div className="flexcontainer vert" className="courseCenter">
                    <h1>{course.title}</h1>
                    <ul className="flexontainer hor">
                    {course.codes.map((code) => (
                        <li key={code.id}>{code.id}</li>
                    ))}
                    </ul>
                    <h4>Enrolled Groups</h4>
                    {this.state.enrolledGroups.map((item, i) => (
                        <Link to={'/group/'+item.id} key={item.id}>
                        <GroupItem
                        id={item.id}
                        i={i}
                        users={item.users}
                        change={UNENROLL}
                        onChange={this.handleChange}
                        />
                        </Link>
                    ))}
                    <h4>Available Groups</h4>
                    <form><fieldset>
                    <input type="text" placeholder="Search" onChange={(e) => this.handleSearch(e.target.value)}/>
                    </fieldset></form>
                    <ul>
                    {this.state.filteredAvailGroups.map((item, i) => (
                        <Link to={'/group/'+item.id} key={item.id}>
                        <GroupItem
                        id={item.id}
                        i={i}
                        users={item.users}
                        change={ENROLL}
                        onChange={this.handleChange}
                        />
                        </Link>
                    ))}
                    </ul>
                    </div>
                        <Availability data={this.state.user.availability}/>
                    </div>
                </div>
            );
        }
    }
}

export default Radium(CourseDetail)
