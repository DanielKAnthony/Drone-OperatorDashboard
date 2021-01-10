import { Route, BrowserRouter as Router, Switch, Redirect } from 'react-router-dom';
import NotFound from './components/NotFound';
import Homepage from './components/DashParent';

function App(){

  

  return (
    <Router forceRefresh={true}>
        <Switch>
          <Route exact path='/' component={Homepage}/>
          <Route exact path='' component={NotFound}/>
        </Switch>
      </Router>
  );
}

export default App;
