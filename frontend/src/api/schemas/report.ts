import { Schema } from "@/api/schemas/types";

export class Report implements Schema {
  constructor(json: {
    id: number;
    name: string;
    description: string | null;
    template: string;
  }) {
    this._id = json.id;
    this._name = json.name;
    this._description = json.description;
    this._template = json.template;
  }

  get id(): number {
    return this._id;
  }

  get template(): string {
    return this._template;
  }

  set template(value: string) {
    this._template = value;
  }

  get description(): string | null {
    return this._description;
  }

  set description(value: string | null) {
    this._description = value;
  }

  get name(): string {
    return this._name;
  }

  set name(value: string) {
    this._name = value;
  }

  public clone() {
    return new Report({
      id: this._id,
      name: this._name,
      description: this._description,
      template: this._template,
    });
  }

  private readonly _id: number;
  private _name: string;
  private _description: string | null;
  private _template: string;
}
