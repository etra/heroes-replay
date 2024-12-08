import { Component, OnInit } from '@angular/core';
import { NonNullableFormBuilder, ReactiveFormsModule, Validators, FormGroup,AbstractControl, ValidationErrors} from '@angular/forms';
import { NzFormModule } from 'ng-zorro-antd/form';
import { NzButtonModule } from 'ng-zorro-antd/button';
import { NzModalModule } from 'ng-zorro-antd/modal';
import { NzLayoutModule } from 'ng-zorro-antd/layout';
import { NzCardModule } from 'ng-zorro-antd/card';
import { NzStepsModule } from 'ng-zorro-antd/steps';
import { NzDividerModule } from 'ng-zorro-antd/divider';

@Component({
  selector: 'app-create-player',
  standalone: true,
  imports: [NzFormModule, ReactiveFormsModule, NzButtonModule, NzModalModule, NzLayoutModule, NzCardModule, NzDividerModule, NzStepsModule],
  templateUrl: './create-player.component.html',
  styleUrl: './create-player.component.css'
})
export class CreatePlayerComponent {
  isVisible: boolean = false;
  playerForm: FormGroup;
  output: string = '';
  currentStep: number = 0;

  constructor(private fb: NonNullableFormBuilder) {
    this.playerForm = this.fb.group({
      id: this.fb.control('', [Validators.required]),
      name: this.fb.control('', [Validators.required]),
      youtube: this.fb.control('', [Validators.pattern(/^(https?\:\/\/)?(www\.)?(youtube\.com|youtu\.?be)\/.+/)]),
      twitch: this.fb.control('', [Validators.pattern(/^(https?\:\/\/)?(www\.)?(twitch\.tv)\/.+/)]),
      discord: this.fb.control('', ),
    });
  }
  changeStep(stepIndex: number): void {
    this.currentStep = stepIndex;
  }
  
  showModal(): void {
    this.isVisible = true;
  }
  
  handleCancel(): void {
    this.isVisible = false;
  }

  onSubmit(): void {
    if (this.playerForm.valid) {
      this.showModal();
      const playerData = this.playerForm.value;
      this.updateOutput(JSON.stringify(playerData, null, 2));
    }
  }

  updateOutput(json: string): void {
    this.output = json;
  }

  copyToClipboard(): void {
      navigator.clipboard.writeText(this.output);
  }

  downloadJson(): void {
    const playerData = this.playerForm.value;
    const dataStr = 'data:text/json;charset=utf-8,' + encodeURIComponent(JSON.stringify(playerData, null, 2));
    const downloadAnchorNode = document.createElement('a');
    downloadAnchorNode.setAttribute('href', dataStr);
    downloadAnchorNode.setAttribute('download', playerData['player_id'] + '.json');
    document.body.appendChild(downloadAnchorNode);
    downloadAnchorNode.click();
    downloadAnchorNode.remove();
  }
}
