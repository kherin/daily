import { useTheme, ThemeProvider } from "./ThemeContext";

const App = () => {
  const { theme, toggleTheme } = useTheme();
  return (
    <div className="App">
      <h1>{theme}</h1>
      <input type="checkbox" checked={theme === "light"} onChange={toggleTheme} />
    </div>
  );
};

export default App;
