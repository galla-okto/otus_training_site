export function Button({ value, onButtonClick }) {
    return <button onClick={onButtonClick}>Click me to get {value + 1}</button>;
}